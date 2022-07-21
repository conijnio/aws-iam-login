import time
from typing import List
import boto3
import botocore
import pytest
from unittest.mock import patch, MagicMock
from botocore.stub import Stubber
from aws_iam_login.aws_config import AWSConfig
from aws_iam_login.actions.rotate_access_keys import RotateAccessKeys
from tests.test_key import generate_key_data

TEST_SET_FIELDS = ",".join(
    ["profile", "username", "current_access_key", "new_access_key"]
)
TEST_SET_DATA = [
    ("my-profile", "johndoe", "XXXXXXXXXXXXXXX1", "XXXXXXXXXXXXXXX2"),
    ("other-profile", "janedoe", "XXXXXXXXXXXXXXX2", "XXXXXXXXXXXXXXX3"),
]


def catch_list_access_keys(username: str, keys: List[dict]) -> dict:
    return {
        "method": "list_access_keys",
        "service_response": {"AccessKeyMetadata": keys},
        "expected_params": {"UserName": username},
    }


def catch_create_access_key(username: str, key: dict) -> dict:
    return {
        "method": "create_access_key",
        "service_response": {"AccessKey": key},
        "expected_params": {"UserName": username},
    }


def catch_update_access_key(username: str, key_id: str) -> dict:
    return {
        "method": "update_access_key",
        "service_response": {},
        "expected_params": {
            "UserName": username,
            "AccessKeyId": key_id,
            "Status": "Inactive",
        },
    }


def catch_delete_access_key(username: str, key_id: str) -> dict:
    return {
        "method": "delete_access_key",
        "service_response": {},
        "expected_params": {"UserName": username, "AccessKeyId": key_id},
    }


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
        stubber.add_response(
            **catch_list_access_keys(
                username=username,
                keys=[
                    generate_key_data(access_key=current_access_key, username=username)
                ],
            )
        )
        stubber.add_response(
            **catch_create_access_key(
                username=username,
                key=generate_key_data(
                    access_key=new_access_key, username=username, include_secret=True
                ),
            )
        )
        stubber.add_response(
            **catch_update_access_key(username=username, key_id=current_access_key)
        )
        stubber.add_response(
            **catch_delete_access_key(username=username, key_id=current_access_key)
        )

        action = RotateAccessKeys(profile=profile)
        assert action.execute() is True
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
        stubber.add_response(
            **catch_list_access_keys(
                username=username,
                keys=[
                    generate_key_data(access_key=current_access_key, username=username),
                    generate_key_data(access_key=new_access_key, username=username),
                ],
            )
        )

        action = RotateAccessKeys(profile=profile)
        assert action.execute() is False
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
            **catch_list_access_keys(
                username=username,
                keys=[
                    generate_key_data(access_key=current_access_key, username=username)
                ],
            )
        )

        stubber.add_client_error(
            method="create_access_key",
            service_error_code="AccessDenied",
            service_message="Forbidden",
            http_status_code=403,
        )

        action = RotateAccessKeys(profile=profile)
        assert action.execute() is False
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
        stubber.add_response(
            **catch_list_access_keys(
                username=username,
                keys=[],
            )
        )

        action = RotateAccessKeys(profile=profile)
        assert action.execute() is False
        stubber.assert_no_pending_responses()


@patch.object(boto3.Session, "client")
@patch.object(AWSConfig, "write")
@patch.object(time, "sleep")
@pytest.mark.parametrize(TEST_SET_FIELDS, TEST_SET_DATA)
def test_rotate_list_access_keys_fails(
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
        stubber.add_client_error(
            method="list_access_keys",
            service_error_code="AccessDenied",
            service_message="Forbidden",
            http_status_code=403,
        )

        action = RotateAccessKeys(profile=profile)
        assert action.execute() is False
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
        stubber.add_response(
            **catch_list_access_keys(
                username=username,
                keys=[
                    generate_key_data(access_key=current_access_key, username=username)
                ],
            )
        )
        stubber.add_response(
            **catch_create_access_key(
                username=username,
                key=generate_key_data(
                    access_key=new_access_key, username=username, include_secret=True
                ),
            )
        )
        stubber.add_client_error(
            method="update_access_key",
            service_error_code="AccessDenied",
            service_message="Forbidden",
            http_status_code=403,
        )

        action = RotateAccessKeys(profile=profile)
        assert action.execute() is False
        stubber.assert_no_pending_responses()


@patch.object(boto3.Session, "client")
@patch.object(AWSConfig, "write")
@patch.object(time, "sleep")
@pytest.mark.parametrize(TEST_SET_FIELDS, TEST_SET_DATA)
def test_deletion_fails(
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
        stubber.add_response(
            **catch_list_access_keys(
                username=username,
                keys=[
                    generate_key_data(access_key=current_access_key, username=username)
                ],
            )
        )
        stubber.add_response(
            **catch_create_access_key(
                username=username,
                key=generate_key_data(
                    access_key=new_access_key, username=username, include_secret=True
                ),
            )
        )
        stubber.add_response(
            **catch_update_access_key(username=username, key_id=current_access_key)
        )
        stubber.add_client_error(
            method="delete_access_key",
            service_error_code="AccessDenied",
            service_message="Forbidden",
            http_status_code=403,
        )

        action = RotateAccessKeys(profile=profile)
        assert action.execute() is False
        stubber.assert_no_pending_responses()
