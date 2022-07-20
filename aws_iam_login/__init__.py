import click
import boto3
from botocore.exceptions import ParamValidationError, ClientError
from click import Context

from aws_iam_login.observer import Observer
from .aws_config import AWSConfig
from .rotate_access_keys import RotateAccessKeys
from .credentials import Credentials
from .application_context import ApplicationContext, ApplicationMessages


@click.group(invoke_without_command=True)
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

        config.write(f"{ctx.profile}-sts", Credentials(response.get("Credentials", {})))
        click.echo(f"Login credentials stored in the {ctx.profile}-sts profile!")
    except ClientError as exc:
        click.echo(f"ClientError: {exc}")
        exit(1)
    except ParamValidationError as exc:
        click.echo(f"ValidationError: {exc}")
        exit(1)


@main.command()
@click.argument("username")
@click.pass_obj
def rotate(ctx: ApplicationContext, username: str) -> None:
    """
    Rotate your IAM User credentials
    """
    click.echo(f"Key rotation process in progress")

    action = RotateAccessKeys(
        profile=ctx.profile, username=username, subject=ctx.subject
    )

    if not action.rotate():
        click.echo(f"Failed to rotate the access keys for the {ctx.profile} profile")
        exit(1)

    click.echo(f"Keys successfully rotated for the {ctx.profile} profile")


if __name__ == "__main__":
    main(obj={})
