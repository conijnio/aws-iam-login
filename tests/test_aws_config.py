from typing import Any
from unittest.mock import patch, mock_open, MagicMock

import pytest

from aws_iam_login.aws_config import AWSConfig


@pytest.mark.parametrize("profile", [None, ""])
def test_invalid_profile(profile: Any) -> None:
    assert AWSConfig(profile=profile).valid is False


@pytest.mark.parametrize(
    "profile, expect_valid",
    [
        ("my-profile-non-existing", False),
        ("my-profile-no-mfa-serial", False),
        ("my-profile-with-mfa-serial", True),
    ],
)
@patch(
    "configparser.open",
    mock_open(
        read_data="""
[my-profile-no-mfa-serial]
aws_access_key_id = XXXX
aws_secret_access_key = XXXXXXXXXXXXXXXX

[my-profile-with-mfa-serial]
aws_access_key_id = XXXX
aws_secret_access_key = XXXXXXXXXXXXXXXX
mfa_serial = arn:aws:iam::111122223333:mfa/my-iam-user
"""
    ),
)
def test_configuration(profile: str, expect_valid) -> None:
    assert AWSConfig(profile=profile).valid is expect_valid


@pytest.mark.parametrize("credentials", [None, {}])
def test_write_empty_credentials(credentials: Any) -> None:
    with patch("configparser.open", mock_open(read_data="")) as mock:
        config = AWSConfig(profile="my-profile")

    with patch("aws_iam_login.aws_config.open") as mock:
        config.write("my-profile-sts", credentials)

    assert mock.called is False


def test_write_sts_credentials() -> None:
    with patch(
        "configparser.open",
        mock_open(
            read_data="""
[my-profile]
aws_access_key_id = XXXX
aws_secret_access_key = XXXXXXXXXXXXXXXX
mfa_serial = arn:aws:iam::111122223333:mfa/my-iam-user
"""
        ),
    ):
        config = AWSConfig(profile="my-profile")

    with patch("aws_iam_login.aws_config.open") as mock:
        config.write("my-profile-sts", MagicMock())

    assert mock.called is True
