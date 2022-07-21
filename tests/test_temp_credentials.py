import pytest
from datetime import datetime
from aws_iam_login.temp_credentials import TempCredentials


def test_none() -> None:
    assert TempCredentials(None).valid is False


@pytest.mark.parametrize(
    "credentials",
    [
        {},
        {"Foo": "Bar"},
        {
            "SecretAccessKey": "MyValue",
            "SessionToken": "MyValue",
            "Expiration": datetime.now(),
        },
        {
            "AccessKeyId": "MyValue",
            "SessionToken": "MyValue",
            "Expiration": datetime.now(),
        },
        {
            "AccessKeyId": "MyValue",
            "SecretAccessKey": "MyValue",
            "Expiration": datetime.now(),
        },
        {
            "AccessKeyId": "MyValue",
            "SecretAccessKey": "MyValue",
            "SessionToken": "MyValue",
        },
    ],
)
def test_wrong_dict(credentials: dict) -> None:
    assert TempCredentials(credentials=credentials).valid is False


def test_valid_dict() -> None:
    expire = datetime.now()
    credentials = TempCredentials(
        credentials={
            "AccessKeyId": "MyValue",
            "SecretAccessKey": "MyValue",
            "SessionToken": "MyValue",
            "Expiration": expire,
        }
    )
    assert credentials.valid is True
    assert dict(credentials) == {
        "aws_access_key_id": "MyValue",
        "aws_secret_access_key": "MyValue",
        "aws_session_token": "MyValue",
        "expiration": str(expire),
    }
