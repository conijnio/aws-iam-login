from typing import Optional
import time
import boto3
from aws_iam_login import AWSConfig
from aws_iam_login.application_context import ApplicationMessages
from aws_iam_login.access_key import AccessKey
from functools import lru_cache


class RotateAccessKeys:
    """
    Understands how to rotate access keys
    """

    __cached_client: Optional[boto3.Session.client] = None

    def __init__(
        self, profile: str, username: str, subject: ApplicationMessages
    ) -> None:
        super().__init__()
        self.__subject = subject
        self.__profile = profile
        self.__config = AWSConfig(profile)
        self.__username = username

    def __message(
        self, message_type: str, message: str, exception: Optional[Exception] = None
    ) -> None:
        self.__subject.send(
            message_type=message_type, message=message, exception=exception
        )

    @lru_cache()
    def current_key(self) -> Optional[AccessKey]:
        try:
            response = self.__client.list_access_keys(UserName=self.__username)

            if len(response["AccessKeyMetadata"]) != 1:
                raise Exception(
                    f"There are {len(response['AccessKeyMetadata'])} keys available, 1 is expected!"
                )

            key = AccessKey(response["AccessKeyMetadata"][0])
            key.secret_access_key = self.__config.key.secret_access_key
            key.profile = self.__config.key.profile
            return key

        except Exception as exc:
            self.__message(
                message_type="exception",
                message=f"Failed to list access keys for the user: {self.__username}",
                exception=exc,
            )

        return None

    @lru_cache()
    def new_key(self) -> Optional[AccessKey]:
        try:
            response = self.__client.create_access_key(UserName=self.__username)
            self.__message(
                message_type="info",
                message="Sleep for 10 seconds to make sure the credentials are active.",
            )
            time.sleep(10)
            return AccessKey(response["AccessKey"])
        except Exception as exc:
            self.__message(
                message_type="exception",
                message=f"Failed to create a new access key for the user: {self.__username}",
                exception=exc,
            )

        return None

    def rotate(self) -> bool:
        if not self.__rotation_possible():
            return False

        current_key = self.current_key()
        new_key = self.new_key()

        if current_key and new_key:
            try:
                self.__flush_client()
                self.__disable_key(current_key)
                self.__config.write(f"{self.__profile}", new_key)
                self.__delete_key(current_key)

                return True
            except Exception as exc:
                self.__message(
                    message_type="exception",
                    message=f"Failed to rotate the credentials for the user: {self.__username}",
                    exception=exc,
                )

        return False

    def __flush_client(self) -> None:
        self.__cached_client = None

    @property
    def __client(self) -> boto3.Session.client:
        if not self.__cached_client:
            session = boto3.Session(profile_name=self.__profile)
            self.__cached_client = session.client("iam")

        return self.__cached_client

    def __rotation_possible(self) -> bool:
        return bool(self.__config.valid and self.current_key())

    def __disable_key(self, key: AccessKey) -> None:
        self.__client.update_access_key(
            UserName=self.__username, AccessKeyId=key.access_key, Status="Inactive"
        )

    def __delete_key(self, key: AccessKey) -> None:
        self.__client.delete_access_key(
            UserName=self.__username, AccessKeyId=key.access_key
        )
