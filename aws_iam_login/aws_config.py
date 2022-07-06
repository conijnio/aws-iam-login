import os
from configparser import ConfigParser, SectionProxy
from typing import Optional
from .credentials import Credentials


class AWSConfig:
    __cached_config: Optional[ConfigParser]

    def __init__(self, profile: str) -> None:
        self.__cached_config = None
        self.__credential_file = os.path.expanduser("~/.aws/credentials")
        self.__profile_name = profile

    @property
    def valid(self) -> bool:
        return bool(
            self.__profile_name
            and self.__profile_name in self.__config
            and self.mfa_serial
        )

    @property
    def __config(self) -> ConfigParser:
        if not self.__cached_config:
            self.__cached_config = ConfigParser()
            self.__cached_config.read(self.__credential_file)

        return self.__cached_config

    @property
    def __profile(self) -> SectionProxy:
        return self.__config[self.__profile_name]

    @property
    def mfa_serial(self) -> Optional[str]:
        return self.__profile.get("mfa_serial", None)

    def write(self, profile: str, credentials: Credentials) -> None:
        if not credentials:
            return

        self.__config[profile] = dict(credentials)

        with open(self.__credential_file, "w") as fh:
            self.__config.write(fh)
