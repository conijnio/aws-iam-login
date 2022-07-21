from typing import Callable

import pytest

from aws_iam_login import ApplicationMessages
from aws_iam_login.actions.action import Action
from aws_iam_login.observer import Observer, Subject


class CustomAction(Action):
    def execute(self) -> bool:
        return True


class CustomObserver(Observer):
    def __init__(self, callback: Callable[[ApplicationMessages], None]) -> None:
        self.__callback = callback

    def update(self, subject: Subject) -> None:
        if isinstance(subject, ApplicationMessages):
            self.__callback(subject)


@pytest.mark.parametrize(
    "message",
    [
        "My info message",
        "My other info message",
    ],
)
def test_info_messages(message: str) -> None:
    def validate(subject: ApplicationMessages) -> None:
        assert subject.type == "INFO"
        assert subject.message == message

    observer = CustomObserver(callback=validate)
    subject = ApplicationMessages()
    subject.attach(observer)

    action = CustomAction()
    action.info("Uncaught message")
    action.subscribe_subject(subject)
    action.info(message)
    subject.detach(observer)
    action.info("Uncaught message")


@pytest.mark.parametrize(
    "message",
    [
        "My warning message",
        "My other warning message",
    ],
)
def test_warning_messages(message: str) -> None:
    def validate(subject: ApplicationMessages) -> None:
        assert subject.type == "WARN"
        assert subject.message == message

    observer = CustomObserver(callback=validate)
    subject = ApplicationMessages()
    subject.attach(observer)

    action = CustomAction()
    action.warning("Uncaught message")
    action.subscribe_subject(subject)
    action.warning(message)
    subject.detach(observer)
    action.warning("Uncaught message")


@pytest.mark.parametrize(
    "message",
    [
        "My error message",
        "My other error message",
    ],
)
def test_error_messages(message: str) -> None:
    def validate(subject: ApplicationMessages) -> None:
        assert subject.type == "ERROR"
        assert subject.message == message

    observer = CustomObserver(callback=validate)
    subject = ApplicationMessages()
    subject.attach(observer)

    action = CustomAction()
    action.error("Uncaught message")
    action.subscribe_subject(subject)
    action.error(message)
    subject.detach(observer)
    action.error("Uncaught message")


@pytest.mark.parametrize(
    "message, exception",
    [
        ("Something went wrong", Exception("My Exception message")),
        ("Something else went wrong", Exception("My Exception message")),
    ],
)
def test_exception_messages(message: str, exception: Exception) -> None:
    def validate(subject: ApplicationMessages) -> None:
        assert subject.type == "ERROR"
        assert subject.message == message
        assert subject.exception == exception

    observer = CustomObserver(callback=validate)
    subject = ApplicationMessages()
    subject.attach(observer)

    action = CustomAction()
    action.exception("Uncaught message", exception)
    action.subscribe_subject(subject)
    action.exception(message, exception)
    subject.detach(observer)
    action.exception("Uncaught message", exception)
