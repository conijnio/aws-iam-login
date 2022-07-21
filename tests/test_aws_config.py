from datetime import datetime
from typing import Any, Union
from unittest.mock import patch, mock_open, call

import pytest

from aws_iam_login import Credentials, TempCredentials
from aws_iam_login.aws_config import AWSConfig
from aws_iam_login.access_key import AccessKey


@pytest.mark.parametrize("profile", [None, ""])
def test_invalid_profile(profile: Any) -> None:
    assert AWSConfig(profile=profile).valid is False


@pytest.mark.parametrize(
    "profile, expect_valid",
    [
        ("my-profile-non-existing", False),
        ("my-profile-no-mfa-serial", False),
        ("my-profile", True),
    ],
)
def test_configuration(profile: str, expect_valid) -> None:
    assert AWSConfig(profile=profile).valid is expect_valid


@pytest.mark.parametrize("credentials", [None, {}])
def test_write_invalid_credentials(credentials: Any) -> None:
    with patch("configparser.open", mock_open(read_data="")) as mock:
        config = AWSConfig(profile="my-profile")

        with patch("builtins.open") as mock_file:
            config.write("my-profile-sts", credentials)
            assert mock_file.called is False


@pytest.mark.parametrize(
    "profile, credentials",
    [
        (
            "my-profile",
            Credentials(
                {
                    "AccessKeyId": "XXXXXXXXXXXXXXXX",
                    "SecretAccessKey": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                }
            ),
        ),
        (
            "my-profile",
            TempCredentials(
                {
                    "AccessKeyId": "XXXXXXXXXXXXXXXX",
                    "SecretAccessKey": "XXXXXXXXXXXXXXXX",
                    "SessionToken": "XXXXXXXXXXXXXXXX",
                    "Expiration": datetime.now(),
                }
            ),
        ),
        (
            "my-profile-no-mfa-serial",
            Credentials(
                {
                    "AccessKeyId": "XXXXXXXXXXXXXXXX",
                    "SecretAccessKey": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                }
            ),
        ),
        (
            "my-profile-no-mfa-serial",
            TempCredentials(
                {
                    "AccessKeyId": "XXXXXXXXXXXXXXXX",
                    "SecretAccessKey": "XXXXXXXXXXXXXXXX",
                    "SessionToken": "XXXXXXXXXXXXXXXX",
                    "Expiration": datetime.now(),
                }
            ),
        ),
    ],
)
def test_write_credentials(profile: str, credentials: Union[Credentials]) -> None:
    config = AWSConfig(profile=profile)

    with patch("aws_iam_login.aws_config.open") as mock_file:
        config.write(f"{profile}-sts", credentials)
        assert mock_file.called is True
        assert call().__enter__().write(f"[{profile}-sts]\n") in mock_file.mock_calls


@pytest.mark.parametrize(
    "profile, username, mfa_serial",
    [
        ("my-profile", "johndoe", "arn:aws:iam::111122223333:mfa/johndoe"),
        ("other-profile", "janedoe", "arn:aws:iam::111122223333:mfa/janedoe"),
    ],
)
def test_initialize(profile: str, username: str, mfa_serial: str) -> None:
    config = AWSConfig(profile=profile)

    with patch("aws_iam_login.aws_config.open") as mock_file:
        config.initialize(username=username, mfa_serial=mfa_serial)
        assert mock_file.called is True
        assert call().__enter__().write(f"[{profile}]\n") in mock_file.mock_calls
        assert (
            call().__enter__().write(f"username = {username}\n") in mock_file.mock_calls
        )
        assert (
            call().__enter__().write(f"mfa_serial = {mfa_serial}\n")
            in mock_file.mock_calls
        )
