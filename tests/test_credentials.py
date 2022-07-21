import pytest
from aws_iam_login.credentials import Credentials


def test_none() -> None:
    assert Credentials(None).valid is False


@pytest.mark.parametrize(
    "credentials",
    [
        {},
        {"Foo": "Bar"},
        {
            "SecretAccessKey": "MyValue",
        },
        {
            "SecretAccessKey": "MyValue",
        },
    ],
)
def test_wrong_dict(credentials: dict) -> None:
    assert Credentials(credentials=credentials).valid is False


def test_valid_dict() -> None:
    credentials = Credentials(
        credentials={"AccessKeyId": "MyValue", "SecretAccessKey": "MyValue"}
    )
    assert credentials.valid is True
    assert dict(credentials) == {
        "aws_access_key_id": "MyValue",
        "aws_secret_access_key": "MyValue",
    }
