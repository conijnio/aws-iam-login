from typing import Optional, List


class Credentials:
    def __init__(self, credentials: Optional[dict]) -> None:
        self._credentials = {}

        if credentials:
            self._credentials = self.__sanitize_input(credentials)

    def __sanitize_input(self, credentials: dict):
        if all(map(lambda field: field in credentials, self._required_fields)):
            return dict((key, credentials[key]) for key in credentials)

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
