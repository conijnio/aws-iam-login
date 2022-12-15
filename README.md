# AWS IAM Login

`aws-iam-login` allows you to login using MFA as the IAM user itself. Once logged in your temporary credentials are
stored in the `~/.aws/credentials` file for re-use.

## Configuration

You will need to configure your roles and IAM User credentials in the same places as you are used to. So in your
`~/.aws/credentials` file. To make this process as easy as possible you could use the following command:

```bash
aws-iam-login my-profile init
```

This command will fetch the ARN of the caller identity. Based on this identity we will determin the `username` and
`mfa_serial` of the IAM User. These will then be stored in the `~/.aws/credentials` file. For example:

```ini
[my-profile]
aws_access_key_id = XXXXXXX
aws_secret_access_key = XXXXXXXXXXXXXXXXXXXXXXXXXXXX
mfa_serial = arn:aws:iam::111122223333:mfa/my-iam-user
username = my-iam-user
```

The only addition is the `username` and `mfa_serial` fields.

### AWS Least privileged

Assuming you have an IAM User that is already configured you will need the following permissions to use `aws-iam-login`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowSessionTokeUsingMFA",
      "Effect": "Allow",
      "Action": [
        "sts:GetSessionToken"
      ],
      "Resource": "*",
      "Condition": {
        "BoolIfExists": {
          "aws:MultiFactorAuthPresent": "true"
        }
      }
    },
    {
      "Sid": "AllowAccessKeyRotation",
      "Effect": "Allow",
      "Action": [
        "iam:ListAccessKeys",
        "iam:CreateAccessKey",
        "iam:UpdateAccessKey",
        "iam:DeleteAccessKey"
      ],
      "Resource": [
        "arn:aws:iam::111122223333:user/${aws:username}"
      ]
    }
  ]
}
```

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

### Rotating your AccessKey and SecretAccessKey

It is advised to rotate your credentials regularly. `aws-iam-login` can help with that! By executing the following command:

```bash
aws-iam-login my-profile rotate
```

This command will execute the following actions:

1. List all available keys for the user, when 1 key is active rotation is possible!
2. Create a new AccessKey and SecretAccessKey.
3. Use the newly created keys to deactivate the old keys.
4. Write the new keys to the `~/.aws/configuration` file.
5. Delete the old keys.
