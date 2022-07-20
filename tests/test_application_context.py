from typing import Optional, List
from unittest.mock import patch, MagicMock, call

import click
import pytest

from aws_iam_login import ApplicationMessages
from aws_iam_login.application_context import CliObserver


@patch.object(click, "echo")
def test_cli_observer_unsupported_subject(mock_echo: MagicMock) -> None:
    CliObserver(debug=False).update(MagicMock())
    assert mock_echo.called is False


@patch.object(click, "echo")
@pytest.mark.parametrize(
    "message_type, message, exception, expected_echo",
    [
        ("info", "my info message", None, "[INFO] my info message"),
        ("warning", "my warning message", None, "[WARNING] my warning message"),
        (
            "exception",
            "my exception message",
            Exception("My Exception"),
            "[EXCEPTION] my exception message",
        ),
    ],
)
def test_cli_observer_no_debug(
    mock_echo: MagicMock,
    message_type: str,
    message: str,
    exception: Optional[Exception],
    expected_echo: str,
) -> None:
    observer = CliObserver(debug=False)
    subject = ApplicationMessages()
    subject.attach(observer)
    subject.send(message_type=message_type, message=message, exception=exception)
    assert mock_echo.called is True
    mock_echo.assert_called_with(expected_echo)

    mock_echo.reset_mock()
    subject.detach(observer)
    subject.send(message_type=message_type, message=message, exception=exception)
    assert mock_echo.called is False


@patch.object(click, "echo")
@pytest.mark.parametrize(
    "message_type, message, exception, expected_echo",
    [
        ("info", "my info message", None, ["[INFO] my info message"]),
        ("warning", "my warning message", None, ["[WARNING] my warning message"]),
        (
            "exception",
            "my exception message",
            Exception("My Exception"),
            ["[EXCEPTION] my exception message", "Exception: My Exception"],
        ),
    ],
)
def test_cli_observer_debug(
    mock_echo: MagicMock,
    message_type: str,
    message: str,
    exception: Optional[Exception],
    expected_echo: List[str],
) -> None:
    observer = CliObserver(debug=False)
    subject = ApplicationMessages()
    subject.attach(observer)
    subject.send(message_type=message_type, message=message, exception=exception)
    CliObserver(debug=True).update(subject)
    mock_echo.assert_has_calls(list(map(call, expected_echo)))
