from datetime import datetime, timedelta

from aws_iam_login.access_key import AccessKey


def test_none_input() -> None:
    key = AccessKey(None)

    assert key.username == ""
    assert key.status == ""
    assert (key.created - datetime.now()) <= timedelta(hours=1)
    assert key.credentials.valid is False
