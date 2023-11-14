from os import environ

from dotenv import load_dotenv

load_dotenv(".env")


REPOSITORY_LINK = environ.get("REPOSITORY_LINK")
