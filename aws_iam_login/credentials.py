from typing import Optional


class Credentials:
    def __init__(self, credentials: Optional[dict]) -> None:
        self.__credentials = {}

        if credentials:
            self.__credentials = self.__sanitize_input(credentials)

    @staticmethod
    def __sanitize_input(credentials: dict):
        fields = ["AccessKeyId", "SecretAccessKey", "SessionToken", "Expiration"]

        if all(map(lambda field: field in credentials, fields)):
            return dict((key, credentials[key]) for key in credentials)

    @property
    def valid(self) -> bool:
        return bool(self.__credentials)

    def __iter__(self):
        yield "aws_access_key_id", self.aws_access_key_id
        yield "aws_secret_access_key", self.aws_secret_access_key
        yield "aws_session_token", self.aws_session_token
        yield "expiration", self.expiration

    @property
    def aws_access_key_id(self) -> str:
        return self.__credentials.get("AccessKeyId", "")

    @property
    def aws_secret_access_key(self) -> str:
        return self.__credentials.get("SecretAccessKey", "")

    @property
    def aws_session_token(self) -> str:
        return self.__credentials.get("SessionToken", "")

    @property
    def expiration(self) -> str:
        return str(self.__credentials.get("Expiration", ""))
