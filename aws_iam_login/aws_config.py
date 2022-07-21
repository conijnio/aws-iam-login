from typing import Optional, Union
import os
import configparser


from .credentials import Credentials
from .access_key import AccessKey


class AWSConfig:
    __cached_config: Optional[configparser.ConfigParser]
    __cached_key: Optional[AccessKey]

    def __init__(self, profile: str) -> None:
        self.__cached_config = None
        self.__cached_key = None
        self.__credential_file = os.environ.get(
            "AWS_SHARED_CREDENTIALS_FILE", os.path.expanduser("~/.aws/credentials")
        )
        self.__profile_name = profile

    @property
    def valid(self) -> bool:
        return bool(
            self.__profile_name
            and self.__profile_name in self.__config
            and self.mfa_serial
            and self.username
        )

    @property
    def __config(self) -> configparser.ConfigParser:
        if not self.__cached_config:
            self.__cached_config = configparser.ConfigParser()
            self.__cached_config.read(self.__credential_file)

        return self.__cached_config

    @property
    def __profile(self) -> configparser.SectionProxy:
        return self.__config[self.__profile_name]

    @property
    def mfa_serial(self) -> str:
        return self.__profile.get("mfa_serial", "")

    @property
    def username(self) -> str:
        return self.__profile.get("username", "")

    @property
    def key(self) -> AccessKey:
        if not self.__cached_key:
            existing_profile = self.__config[self.__profile_name]
            self.__cached_key = AccessKey(
                {
                    "Profile": self.__profile_name,
                    "AccessKeyId": existing_profile["aws_access_key_id"],
                    "SecretAccessKey": existing_profile["aws_secret_access_key"],
                }
            )

        return self.__cached_key

    def initialize(self, username: str, mfa_serial: str) -> None:
        self.__profile["username"] = username
        self.__profile["mfa_serial"] = mfa_serial
        self.__save_configuration()

    def __save_configuration(self):
        with open(self.__credential_file, "w") as fh:
            self.__config.write(fh)

    def write(
        self, profile: str, credentials: Union[None, Credentials, AccessKey]
    ) -> None:
        if not credentials:
            return

        for key, value in dict(credentials).items():
            if profile not in self.__config:
                self.__config[profile] = {}

            self.__config[profile][key] = value

        self.__save_configuration()
