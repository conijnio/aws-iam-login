# AWS IAM Login

`aws-iam-login` allows you to login using MFA as the IAM user itself. Once logged in your temporary credentials are
stored in the `~/.aws/credentials` file for re-use.

## Configuration

You will need to configure your roles and IAM User credentials in the same places as you are used to. So in your
`~/.aws/credentials` file you will need to have the following:

```ini
[my-profile]
aws_access_key_id = XXXXXXX
aws_secret_access_key = XXXXXXXXXXXXXXXXXXXXXXXXXXXX
mfa_serial = arn:aws:iam::111122223333:mfa/my-iam-user
```

The only addition is the `mfa_serial` field.

## Usage

When you want to make use of the MFA authenticated session of a configured profile. You will need to configure the
following:

```ini
[profile my-role-1]
role_arn = arn:aws:iam::111122223333:role/my-role-1
source_profile = my-profile-sts
region = eu-west-1
```

Then when you perform your AWS cli calls you can use the `AWS_PROFILE=my-role-1` as you are used to. But the first time  it will fail. The reason for this is that the `my-profile-sts` source profile does not exist (or the credentials are expired).
Perform the following command to login, this command will ask for your MFA Token:

```bash
aws-iam-login my-profile
```

This authenticates against the AWS API and request temporary credentials from AWS using your MFA Token. These credentials are then stored as `<profile-name>-sts`.
So the next time you use `AWS_PROFILE=my-role-1` the credentials will be present and not expired.

Because you are already authenticated using MFA there is no need to provide an MFA token when you assume the role.
When you switch a lot between roles you really benefit from not having to type your MFA token each time you switch.
