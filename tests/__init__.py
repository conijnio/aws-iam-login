import os

os.environ["AWS_SHARED_CREDENTIALS_FILE"] = os.path.join(
    os.path.dirname(__file__), "credentials"
)
