from datetime import datetime
from typing import Dict, Union


class AccessKey:
    """
    Understands the AccessKey format of AWS
    """

    def __init__(self, data: Dict[str, Union[str, datetime]]):
        self.__raw_data = data

    def __iter__(self):
        yield "aws_access_key_id", self.access_key
        yield "aws_secret_access_key", self.secret_access_key

    @property
    def profile(self) -> str:
        return str(self.__raw_data.get("Profile", ""))

    @profile.setter
    def profile(self, value: str) -> None:
        self.__raw_data["Profile"] = value

    @property
    def username(self) -> str:
        return str(self.__raw_data.get("UserName", ""))

    @property
    def access_key(self) -> str:
        return str(self.__raw_data.get("AccessKeyId", ""))

    @property
    def secret_access_key(self) -> str:
        return str(self.__raw_data.get("SecretAccessKey", ""))

    @secret_access_key.setter
    def secret_access_key(self, value) -> None:
        self.__raw_data["SecretAccessKey"] = value

    @property
    def status(self) -> str:
        return str(self.__raw_data.get("Status", ""))

    @property
    def created(self) -> datetime:
        date = self.__raw_data.get("CreateDate")
        return date if isinstance(date, datetime) else datetime.now()

    def __str__(self) -> str:
        postfix = ""
        if self.secret_access_key:
            postfix = " (contains secret)"
        return f"{self.access_key}, {self.status} {self.username} created at {self.created}{postfix}"

    def __repr__(self) -> str:
        return str(self)
