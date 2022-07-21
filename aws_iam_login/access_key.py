from datetime import datetime
from typing import Dict, Union

from aws_iam_login.credentials import Credentials


class AccessKey:
    """
    Understands the AccessKey format of AWS
    """

    def __init__(self, data: Dict[str, Union[str, datetime]]):
        self.__raw_data = data

        self.__credentials = Credentials(data)

    @property
    def username(self) -> str:
        return str(self.__raw_data.get("UserName", ""))

    @property
    def credentials(self) -> Credentials:
        return self.__credentials

    @property
    def status(self) -> str:
        return str(self.__raw_data.get("Status", ""))

    @property
    def created(self) -> datetime:
        date = self.__raw_data.get("CreateDate")
        return date if isinstance(date, datetime) else datetime.now()

    def __str__(self) -> str:
        postfix = ""
        if self.credentials.aws_secret_access_key:
            postfix = " (contains secret)"
        return f"{self.credentials.aws_access_key_id}, {self.status} {self.username} created at {self.created}{postfix}"

    def __repr__(self) -> str:
        return str(self)
