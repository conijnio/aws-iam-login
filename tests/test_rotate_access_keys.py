import time
import boto3
import botocore
import pytest

from unittest.mock import patch, MagicMock

from botocore.stub import Stubber

from aws_iam_login import RotateAccessKeys, AWSConfig
from tests.test_key import generate_key_data

TEST_SET_FIELDS = ",".join(
    ["profile", "username", "current_access_key", "new_access_key"]
)
TEST_SET_DATA = [
    ("my-profile", "johndoe", "XXXXXXXXXXXXXXX1", "XXXXXXXXXXXXXXX2"),
    ("other-profile", "janedoe", "XXXXXXXXXXXXXXX2", "XXXXXXXXXXXXXXX3"),
]


@patch.object(boto3.Session, "client")
@patch.object(AWSConfig, "write")
@patch.object(time, "sleep")
@pytest.mark.parametrize(TEST_SET_FIELDS, TEST_SET_DATA)
def test_successful_rotate(
    mock_sleep: MagicMock,
    mock_config: MagicMock,
    mock_client: MagicMock,
    profile: str,
    username: str,
    current_access_key: str,
    new_access_key: str,
) -> None:
    stubbed_client = botocore.session.get_session().create_client("iam")
    mock_client.return_value = stubbed_client

    with Stubber(stubbed_client) as stubber:
        # Prepare client for API calls
        stubber.add_response(
            "list_access_keys",
            {
                "AccessKeyMetadata": [
                    generate_key_data(access_key=current_access_key, username=username)
                ]
            },
            {"UserName": username},
        )
        stubber.add_response(
            "create_access_key",
            {
                "AccessKey": generate_key_data(
                    access_key=new_access_key, username=username, include_secret=True
                )
            },
            {"UserName": username},
        )
        stubber.add_response(
            "update_access_key",
            {},
            {
                "UserName": username,
                "AccessKeyId": current_access_key,
                "Status": "Inactive",
            },
        )
        stubber.add_response(
            "delete_access_key",
            {},
            {"UserName": username, "AccessKeyId": current_access_key},
        )

        action = RotateAccessKeys(
            profile=profile, username=username, subject=MagicMock()
        )
        assert action.rotate() is True
        stubber.assert_no_pending_responses()


@patch.object(boto3.Session, "client")
@patch.object(AWSConfig, "write")
@patch.object(time, "sleep")
@pytest.mark.parametrize(TEST_SET_FIELDS, TEST_SET_DATA)
def test_rotate_while_2_access_keys_are_available(
    mock_sleep: MagicMock,
    mock_config: MagicMock,
    mock_client: MagicMock,
    profile: str,
    username: str,
    current_access_key: str,
    new_access_key: str,
) -> None:
    stubbed_client = botocore.session.get_session().create_client("iam")
    mock_client.return_value = stubbed_client

    with Stubber(stubbed_client) as stubber:
        # Prepare client for API calls
        stubber.add_response(
            method="list_access_keys",
            service_response={
                "AccessKeyMetadata": [
                    generate_key_data(access_key=current_access_key, username=username),
                    generate_key_data(access_key=new_access_key, username=username),
                ]
            },
            expected_params={"UserName": username},
        )

        action = RotateAccessKeys(
            profile=profile, username=username, subject=MagicMock()
        )
        assert action.rotate() is False
        stubber.assert_no_pending_responses()


@patch.object(boto3.Session, "client")
@patch.object(AWSConfig, "write")
@patch.object(time, "sleep")
@pytest.mark.parametrize(TEST_SET_FIELDS, TEST_SET_DATA)
def test_rotate_new_key_creation_failed(
    mock_sleep: MagicMock,
    mock_config: MagicMock,
    mock_client: MagicMock,
    profile: str,
    username: str,
    current_access_key: str,
    new_access_key: str,
) -> None:
    stubbed_client = botocore.session.get_session().create_client("iam")
    mock_client.return_value = stubbed_client

    with Stubber(stubbed_client) as stubber:
        # Prepare client for API calls
        stubber.add_response(
            method="list_access_keys",
            service_response={
                "AccessKeyMetadata": [
                    generate_key_data(access_key=current_access_key, username=username)
                ]
            },
            expected_params={"UserName": username},
        )

        stubber.add_client_error(
            method="create_access_key",
            service_error_code="AccessDenied",
            service_message="Forbidden",
            http_status_code=403,
        )

        action = RotateAccessKeys(
            profile=profile, username=username, subject=MagicMock()
        )
        assert action.rotate() is False
        stubber.assert_no_pending_responses()


@patch.object(boto3.Session, "client")
@patch.object(AWSConfig, "write")
@patch.object(time, "sleep")
@pytest.mark.parametrize(TEST_SET_FIELDS, TEST_SET_DATA)
def test_rotate_no_keys_available(
    mock_sleep: MagicMock,
    mock_config: MagicMock,
    mock_client: MagicMock,
    profile: str,
    username: str,
    current_access_key: str,
    new_access_key: str,
) -> None:
    stubbed_client = botocore.session.get_session().create_client("iam")
    mock_client.return_value = stubbed_client

    with Stubber(stubbed_client) as stubber:
        # Prepare client for API calls
        stubber.add_response(
            method="list_access_keys",
            service_response={"AccessKeyMetadata": []},
            expected_params={"UserName": username},
        )

        action = RotateAccessKeys(
            profile=profile, username=username, subject=MagicMock()
        )
        assert action.rotate() is False
        stubber.assert_no_pending_responses()


@patch.object(boto3.Session, "client")
@patch.object(AWSConfig, "write")
@patch.object(time, "sleep")
@pytest.mark.parametrize(TEST_SET_FIELDS, TEST_SET_DATA)
def test_deactivation_fails(
    mock_sleep: MagicMock,
    mock_config: MagicMock,
    mock_client: MagicMock,
    profile: str,
    username: str,
    current_access_key: str,
    new_access_key: str,
) -> None:
    stubbed_client = botocore.session.get_session().create_client("iam")
    mock_client.return_value = stubbed_client

    with Stubber(stubbed_client) as stubber:
        # Prepare client for API calls
        stubber.add_response(
            "list_access_keys",
            {
                "AccessKeyMetadata": [
                    generate_key_data(access_key=current_access_key, username=username)
                ]
            },
            {"UserName": username},
        )
        stubber.add_response(
            "create_access_key",
            {
                "AccessKey": generate_key_data(
                    access_key=new_access_key, username=username, include_secret=True
                )
            },
            {"UserName": username},
        )

        stubber.add_client_error(
            method="update_access_key",
            service_error_code="AccessDenied",
            service_message="Forbidden",
            http_status_code=403,
        )

        action = RotateAccessKeys(
            profile=profile, username=username, subject=MagicMock()
        )
        assert action.rotate() is False
        stubber.assert_no_pending_responses()
