from typing import Optional
import boto3

from aws_iam_login.actions.action import Action
from aws_iam_login.aws_config import AWSConfig


class InitializeConfiguration(Action):
    """
    Understands how to configure the AWS profiles to be used by aws-iam-login.
    """

    __cached_client: Optional[boto3.Session.client] = None

    def __init__(self, profile: str) -> None:
        self.__profile = profile

        self.__config = AWSConfig(profile)
        self.__client = boto3.Session(profile_name=profile).client("sts")

    def execute(self) -> bool:
        if self.__config.mfa_serial and self.__config.username:
            self.info(f"The {self.__profile} profile is already initialized.")
            return True

        try:
            data = self.__client.get_caller_identity()
            mfa_serial = data["Arn"].replace(":user/", ":mfa/")
            username = mfa_serial.split("/")[-1]
            self.info(f"Determined MFA ARN: {mfa_serial}")
            self.info(f"Determined IAM Username: {username}")
            self.__config.initialize(username=username, mfa_serial=mfa_serial)

            return True
        except Exception as exc:
            message = (
                f"Failed to get the caller identity for the {self.__profile} profile."
            )
            self.exception(message=message, exception=exc)

        return False
