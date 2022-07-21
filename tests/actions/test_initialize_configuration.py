import boto3
import botocore
import pytest

from unittest.mock import patch, MagicMock
from botocore.stub import Stubber
from aws_iam_login.aws_config import AWSConfig
from aws_iam_login.actions.initialize_configuration import InitializeConfiguration


@patch.object(boto3.Session, "client")
@patch.object(AWSConfig, "_AWSConfig__save_configuration")
@pytest.mark.parametrize(
    "profile, username",
    [
        ("my-profile-no-mfa-serial", "no-mfa-serial"),
        ("my-profile-no-username", "no-username"),
        ("my-profile-no-username-and-mfa-serial", "no-username-and-mfa-serial"),
    ],
)
def test_successful_initialize(
    mock_config: MagicMock,
    mock_client: MagicMock,
    profile: str,
    username: str,
) -> None:
    mock_client.return_value = botocore.session.get_session().create_client("sts")

    with Stubber(mock_client.return_value) as stubber:
        stubber.add_response(
            method="get_caller_identity",
            service_response={
                "UserId": "AKIAI44QH8DHBEXAMPLE",
                "Account": "111122223333",
                "Arn": f"arn:aws:iam::111122223333:mfa/{username}",
            },
            expected_params={},
        )

        action = InitializeConfiguration(profile=profile)
        assert action.execute() is True
        assert mock_config.called is True
        stubber.assert_no_pending_responses()


@patch.object(boto3.Session, "client")
@patch.object(AWSConfig, "_AWSConfig__save_configuration")
@pytest.mark.parametrize(
    "profile, username",
    [
        ("my-profile", "johndoe"),
        ("other-profile", "janedoe"),
    ],
)
def test_initialize_already_initialized(
    mock_config: MagicMock,
    mock_client: MagicMock,
    profile: str,
    username: str,
) -> None:
    mock_client.return_value = botocore.session.get_session().create_client("sts")

    with Stubber(mock_client.return_value) as stubber:
        action = InitializeConfiguration(profile=profile)
        assert action.execute() is True
        assert mock_config.called is False
        stubber.assert_no_pending_responses()


@patch.object(boto3.Session, "client")
@patch.object(AWSConfig, "_AWSConfig__save_configuration")
@pytest.mark.parametrize(
    "profile, username",
    [
        ("my-profile-no-mfa-serial", "no-mfa-serial"),
        ("my-profile-no-username", "no-username"),
        ("my-profile-no-username-and-mfa-serial", "no-username-and-mfa-serial"),
    ],
)
def test_initialize_get_caller_identity_failure(
    mock_config: MagicMock,
    mock_client: MagicMock,
    profile: str,
    username: str,
) -> None:
    mock_client.return_value = botocore.session.get_session().create_client("sts")

    with Stubber(mock_client.return_value) as stubber:
        stubber.add_client_error(
            method="get_caller_identity",
            service_error_code="AccessDenied",
            service_message="Forbidden",
            http_status_code=403,
        )

        action = InitializeConfiguration(profile=profile)
        assert action.execute() is False
        assert mock_config.called is False
        stubber.assert_no_pending_responses()
