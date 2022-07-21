from typing import Optional
from abc import ABC, abstractmethod
from aws_iam_login.application_context import ApplicationMessages


class Action(ABC):
    """
    Understands generic actions that are executed
    """

    __subject: Optional[ApplicationMessages] = None

    def subscribe_subject(self, subject: ApplicationMessages):
        self.__subject = subject

    def info(self, message: str) -> None:
        if self.__subject:
            self.__subject.send(message_type="INFO", message=message)

    def warning(self, message: str) -> None:
        if self.__subject:
            self.__subject.send(message_type="WARN", message=message)

    def error(self, message: str) -> None:
        if self.__subject:
            self.__subject.send(message_type="ERROR", message=message)

    def exception(self, message: str, exception: Exception) -> None:
        if self.__subject:
            self.__subject.send(
                message_type="ERROR", message=message, exception=exception
            )

    @abstractmethod
    def execute(self) -> bool:
        pass
