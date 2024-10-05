import os
from dotenv import load_dotenv

load_dotenv()


class DBConfigError(Exception):
    pass


class DBConfig:
    DB_HOST_IP: str
    DB_NAME: str
    DB_USER_NAME: str
    DB_USER_PASSWORD: str

    def __init__(self, env):

        for field in self.__annotations__:

            if not field.isupper():
                continue

            default_value = getattr(self, field, None)
            if default_value is None and env.get(field) is None:
                raise DBConfigError("The {} field is required".format(field))

            value = env.get(field, default_value)
            self.__setattr__(field, value)

    def __repr__(self):

        return str(self.__dict__)


db_config = DBConfig(os.environ)
