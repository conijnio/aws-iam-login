from datetime import datetime
from typing import Dict, Union, Optional

from aws_iam_login.credentials import Credentials


class AccessKey:
    """
    Understands the AccessKey format of AWS
    """

    def __init__(self, data: Optional[dict]):
        sanitized_data = self.__sanitize_input(data)
        self.__data = sanitized_data if sanitized_data else {}
        self.__credentials = Credentials(data)

    @staticmethod
    def __sanitize_input(data: Optional[dict]) -> Optional[dict]:
        if not isinstance(data, dict):
            return None

        sanitized = {}

        for key in ["UserName", "Status", "CreateDate"]:
            if key in data:
                sanitized[key] = data[key]

        return sanitized

    @property
    def username(self) -> str:
        return str(self.__data.get("UserName", ""))

    @property
    def credentials(self) -> Credentials:
        return self.__credentials

    @property
    def status(self) -> str:
        return str(self.__data.get("Status", ""))

    @property
    def created(self) -> datetime:
        date = self.__data.get("CreateDate")
        return date if isinstance(date, datetime) else datetime.now()

    def __str__(self) -> str:
        postfix = ""
        if self.credentials.aws_secret_access_key:
            postfix = " (contains secret)"
        return f"{self.credentials.aws_access_key_id}, {self.status} {self.username} created at {self.created}{postfix}"

    def __repr__(self) -> str:
        return str(self)
