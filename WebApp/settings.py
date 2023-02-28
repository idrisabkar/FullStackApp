from pydantic import BaseSettings
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# Now you can access your environment variables using `os.getenv()` or `os.environ`


class Variables(BaseSettings):
    SECRET_KEY: str

    class Config:
        env_file = "./.env"


variables = Variables()
