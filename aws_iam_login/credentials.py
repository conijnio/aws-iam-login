from typing import Optional, List, Dict


class Credentials:
    def __init__(self, data: Optional[dict]) -> None:
        sanitized_data = self.__sanitize_input(data)
        self._credentials = sanitized_data if sanitized_data else {}

    def __sanitize_input(self, data: Optional[dict]) -> Optional[dict]:
        if not isinstance(data, dict):
            return None

        sanitized = {}

        for key in self._required_fields:
            if key not in data:
                return None

            sanitized[key] = data[key]

        return sanitized

    @property
    def _required_fields(self) -> List[str]:
        return ["AccessKeyId", "SecretAccessKey"]

    @property
    def valid(self) -> bool:
        return bool(self._credentials)

    def __iter__(self):
        yield "aws_access_key_id", self.aws_access_key_id
        yield "aws_secret_access_key", self.aws_secret_access_key

    @property
    def aws_access_key_id(self) -> str:
        return self._credentials.get("AccessKeyId", "")

    @property
    def aws_secret_access_key(self) -> str:
        return self._credentials.get("SecretAccessKey", "")

    @aws_secret_access_key.setter
    def aws_secret_access_key(self, value: str):
        self._credentials["SecretAccessKey"] = value
