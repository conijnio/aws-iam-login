import click
import boto3
from botocore.exceptions import ParamValidationError, ClientError
from click import Context

from aws_iam_login.actions.initialize_configuration import InitializeConfiguration
from aws_iam_login.observer import Observer
from aws_iam_login.temp_credentials import TempCredentials
from aws_iam_login.aws_config import AWSConfig
from aws_iam_login.actions.rotate_access_keys import RotateAccessKeys
from aws_iam_login.credentials import Credentials
from aws_iam_login.application_context import ApplicationContext, ApplicationMessages

__version__ = "0.3.6"


@click.group(invoke_without_command=True)  # type: ignore
@click.option("--debug/--no-debug")
@click.argument("profile")
@click.pass_context
def main(ctx: Context, debug: bool, profile: str) -> None:
    """
    aws-iam-login
    """
    ctx.obj = ApplicationContext(profile=profile, debug=debug)

    if ctx.invoked_subcommand is None:
        credentials(ctx=ctx.obj)


def credentials(ctx: ApplicationContext) -> None:
    config = AWSConfig(ctx.profile)
    session = boto3.Session(profile_name=ctx.profile)
    client = session.client("sts")

    try:
        response = client.get_session_token(
            SerialNumber=config.mfa_serial,
            TokenCode=input(f"Enter MFA code for {config.mfa_serial}: "),
        )

        config.write(
            f"{ctx.profile}-sts", TempCredentials(response.get("Credentials", {}))
        )
        click.echo(f"Login credentials stored in the {ctx.profile}-sts profile!")
    except ClientError as exc:
        click.echo(f"ClientError: {exc}")
        exit(1)
    except ParamValidationError as exc:
        click.echo(f"ValidationError: {exc}")
        exit(1)


@main.command()  # type: ignore
@click.pass_obj
def init(ctx: ApplicationContext) -> None:
    """
    Initialize your `.aws/configuration`
    """
    click.echo(f"Looking up additional required data...")

    action = InitializeConfiguration(profile=ctx.profile)
    action.subscribe_subject(ctx.subject)

    if not action.execute():
        click.echo(f"Failed to initialize the {ctx.profile} profile")
        exit(1)

    click.echo(f"The {ctx.profile} profile has been successfully initialized!")


@main.command()  # type: ignore
@click.pass_obj
def rotate(ctx: ApplicationContext) -> None:
    """
    Rotate your IAM User credentials
    """
    click.echo(f"Key rotation process in progress")

    action = RotateAccessKeys(profile=ctx.profile)
    action.subscribe_subject(ctx.subject)

    if not action.execute():
        click.echo(f"Failed to rotate the access keys for the {ctx.profile} profile")
        exit(1)

    click.echo(f"Keys successfully rotated for the {ctx.profile} profile")
