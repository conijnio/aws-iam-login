from datetime import datetime
from unittest.mock import patch
from click.testing import CliRunner
from aws_iam_login import main


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
    result = runner.invoke(main, "my-profile-1")

    assert result.exit_code == 0
