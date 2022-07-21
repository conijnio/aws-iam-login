from datetime import datetime

import pytest

from aws_iam_login.access_key import AccessKey


#  TODO: SYNC WITH test_credentials


def generate_key_data(
    index: int = 1,
    access_key: str = "",
    username: str = "johndoe",
    status: str = "Active",
    created: datetime = datetime.now(),
    include_secret: bool = False,
) -> dict:
    data = {
        "UserName": username,
        "AccessKeyId": access_key if access_key else f"XXXXXXXXXXXXXXX{index}",
        "Status": status,
        "CreateDate": created,
    }

    if include_secret:
        data["SecretAccessKey"] = "XXXXXXXXXXXXXXXX"

    return data


@pytest.mark.parametrize(
    "kwargs, expected_repr",
    [
        (
            {"index": 1},
            "XXXXXXXXXXXXXXX1, Active johndoe created at 2022-07-20 00:00:00 (contains secret)",
        ),
        (
            {"index": 2, "username": "janedoe"},
            "XXXXXXXXXXXXXXX2, Active janedoe created at 2022-07-20 00:00:00 (contains secret)",
        ),
        (
            {"index": 3, "status": "Inactive"},
            "XXXXXXXXXXXXXXX3, Inactive johndoe created at 2022-07-20 00:00:00 (contains secret)",
        ),
        (
            {"index": 4, "username": "janedoe", "status": "Inactive"},
            "XXXXXXXXXXXXXXX4, Inactive janedoe created at 2022-07-20 00:00:00 (contains secret)",
        ),
    ],
)
def test_access_key(kwargs, expected_repr) -> None:
    create_stamp = datetime(2022, 7, 20)
    raw_data = generate_key_data(created=create_stamp, include_secret=True, **kwargs)
    key = AccessKey(raw_data)
    assert key.created == raw_data["CreateDate"]
    assert str(key) == expected_repr
    assert repr(key) == expected_repr


def test_access_key_set_secret_access_key() -> None:
    create_stamp = datetime(2022, 7, 20)
    key = AccessKey(
        generate_key_data(index=1, created=create_stamp, include_secret=True)
    )
    key.credentials.aws_secret_access_key = ""
    assert key.credentials.aws_secret_access_key == ""
    assert str(key) == "XXXXXXXXXXXXXXX1, Active johndoe created at 2022-07-20 00:00:00"
    key.credentials.aws_secret_access_key = "MySecret"
    assert key.credentials.aws_secret_access_key == "MySecret"
    assert (
        str(key)
        == "XXXXXXXXXXXXXXX1, Active johndoe created at 2022-07-20 00:00:00 (contains secret)"
    )
    assert (
        repr(key)
        == "XXXXXXXXXXXXXXX1, Active johndoe created at 2022-07-20 00:00:00 (contains secret)"
    )
