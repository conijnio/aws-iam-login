from typing import Optional, List
import time
import boto3
from functools import lru_cache
from aws_iam_login import AWSConfig
from aws_iam_login.actions.action import Action
from aws_iam_login.access_key import AccessKey


class RotateAccessKeys(Action):
    """
    Understands how to rotate access keys
    """

    __cached_client: Optional[boto3.Session.client] = None

    def __init__(self, profile: str) -> None:
        self.__profile = profile
        self.__config = AWSConfig(profile)

    @lru_cache()
    def new_key(self) -> Optional[AccessKey]:
        try:
            response = self.__client.create_access_key(UserName=self.__config.username)
            self.info(
                message="Sleep for 10 seconds to make sure the credentials are active."
            )
            time.sleep(10)
            return AccessKey(response["AccessKey"])
        except Exception as exc:
            message = f"Failed to create a new access key for the user: {self.__config.username}"
            self.exception(message=message, exception=exc)

        return None

    def execute(self) -> bool:
        if not self.__rotation_possible():
            return False

        new_key = self.new_key()

        if self.__config.key and new_key:
            try:
                self.__flush_client()
                self.__disable_key(self.__config.key)
                self.__config.write(f"{self.__profile}", new_key.credentials)
                self.__delete_key(self.__config.key)

                return True
            except Exception as exc:
                message = f"Failed to rotate the credentials for the user: {self.__config.username}"
                self.exception(message=message, exception=exc)

        return False

    def __flush_client(self) -> None:
        self.__cached_client = None

    @property
    def __client(self) -> boto3.Session.client:
        if not self.__cached_client:
            session = boto3.Session(profile_name=self.__profile)
            self.__cached_client = session.client("iam")

        return self.__cached_client

    def __get_current_keys(self) -> List[dict]:
        try:
            response = self.__client.list_access_keys(UserName=self.__config.username)
            return response["AccessKeyMetadata"]
        except Exception as exc:
            message = (
                f"Failed to list access keys for the user: {self.__config.username}"
            )
            self.exception(message=message, exception=exc)

        return []

    def __rotation_possible(self) -> bool:
        if not self.__config.valid:
            self.warning(
                f"The configuration for the {self.__profile} is invalid, please try `aws-iam-login {self.__profile} init` first!"
            )
            return False

        if len(self.__get_current_keys()) != 1:
            self.error(f"There needs to be only 1 AccessKey present!")
            return False

        return True

    def __disable_key(self, key: AccessKey) -> None:
        self.__client.update_access_key(
            UserName=self.__config.username,
            AccessKeyId=key.credentials.aws_access_key_id,
            Status="Inactive",
        )

    def __delete_key(self, key: AccessKey) -> None:
        self.__client.delete_access_key(
            UserName=self.__config.username,
            AccessKeyId=key.credentials.aws_access_key_id,
        )
