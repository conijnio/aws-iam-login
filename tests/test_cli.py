import pytest
from datetime import datetime
from unittest.mock import patch, MagicMock
from botocore.exceptions import ParamValidationError, ClientError
from click.testing import CliRunner
from aws_iam_login import main, RotateAccessKeys, InitializeConfiguration


@patch("aws_iam_login.AWSConfig")
@patch("builtins.input")
@patch("boto3.Session")
def test_main(mock_session, mock_input, mock_config) -> None:
    mock_session.return_value.client.return_value.get_session_token.return_value = {
        "Credentials": {
            "AccessKeyId": "XXXXXXXXXXXXXXXX",
            "SecretAccessKey": "XXXXXXXXXXXXXXXX",
            "SessionToken": "XXXXXXXXXXXXXXXX",
            "Expiration": datetime.now(),
        }
    }

    runner = CliRunner()
    result = runner.invoke(main, ["my-profile-1"])

    assert result.exit_code == 0


@patch("aws_iam_login.AWSConfig")
@patch("builtins.input")
@patch("boto3.Session")
@pytest.mark.parametrize(
    "exception",
    [
        ParamValidationError(report={}),
        ClientError({}, "STS"),
        Exception("My exception message"),
    ],
)
def test_exceptions(mock_session, mock_input, mock_config, exception) -> None:
    mock_session.return_value.client.return_value.get_session_token.side_effect = (
        exception
    )

    runner = CliRunner()
    result = runner.invoke(main, ["my-profile-1"])
    assert result.exit_code == 1


def test_rotate_no_username_and_mfa_device() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["my-profile-no-mfa-serial", "rotate"])
    assert result.exit_code == 1


@patch.object(RotateAccessKeys, "execute", return_value=False)
def test_rotate_failure(mock_rotate: MagicMock) -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["my-profile", "rotate"])
    assert result.exit_code == 1


@patch.object(RotateAccessKeys, "execute", return_value=True)
def test_rotate_success(mock_rotate: MagicMock) -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["my-profile", "rotate"])
    assert result.exit_code == 0


@patch.object(InitializeConfiguration, "execute", return_value=False)
def test_init_failure(mock_rotate: MagicMock) -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["my-profile", "init"])
    assert result.exit_code == 1


@patch.object(InitializeConfiguration, "execute", return_value=True)
def test_init_success(mock_rotate: MagicMock) -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["my-profile", "init"])
    assert result.exit_code == 0
