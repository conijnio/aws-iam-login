from typing import Optional, List

from aws_iam_login.credentials import Credentials


class TempCredentials(Credentials):
    def __init__(self, credentials: Optional[dict]) -> None:
        self._required_fields.extend(["SessionToken", "Expiration"])
        super().__init__(credentials)

    def __iter__(self):
        yield "aws_access_key_id", self.aws_access_key_id
        yield "aws_secret_access_key", self.aws_secret_access_key
        yield "aws_session_token", self.aws_session_token
        yield "expiration", self.expiration

    @property
    def _required_fields(self) -> List[str]:
        return super()._required_fields + ["SessionToken", "Expiration"]

    @property
    def aws_session_token(self) -> str:
        return self._credentials.get("SessionToken", "")

    @property
    def expiration(self) -> str:
        return str(self._credentials.get("Expiration", ""))
