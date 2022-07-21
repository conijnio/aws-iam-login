from typing import List, Optional
import click

from aws_iam_login.observer import Observer, Subject


class ApplicationMessages(Subject):
    __observers: List[Observer] = []
    message: str
    type: str
    exception: Optional[Exception]

    def attach(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def notify(self) -> None:
        for observer in self.__observers:
            observer.update(self)

    def send(
        self, message_type: str, message: str, exception: Optional[Exception] = None
    ) -> None:
        self.message = message
        self.type = message_type
        self.exception = exception
        self.notify()


class CliObserver(Observer):
    def __init__(self, debug: bool) -> None:
        self.__debug = debug

    def update(self, subject: Subject) -> None:
        if not isinstance(subject, ApplicationMessages):
            return

        click.echo(f"[{subject.type.upper()}] {subject.message}")

        if subject.exception and self.__debug:
            click.echo(f"Exception: {subject.exception}")


class ApplicationContext:
    def __init__(self, profile: str, debug: bool) -> None:
        self.__subject = ApplicationMessages()
        self.__subject.attach(CliObserver(debug=debug))
        self.profile = profile

    @property
    def subject(self) -> ApplicationMessages:
        return self.__subject
