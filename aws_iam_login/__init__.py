import click
import boto3
from .aws_config import AWSConfig
from .credentials import Credentials


@click.command()
@click.argument("profile")
def main(profile: str) -> None:
    """
    aws-iam-login
    """
    config = AWSConfig(profile)
    session = boto3.Session(profile_name=profile)
    client = session.client("sts")

    response = client.get_session_token(
        SerialNumber=config.mfa_serial,
        TokenCode=input(f"Enter MFA code for {config.mfa_serial}: "),
    )

    config.write(f"{profile}-sts", Credentials(response.get("Credentials", {})))
    click.echo(f"Login credentials stored in the {profile}-sts profile!")


if __name__ == "__main__":
    main()
