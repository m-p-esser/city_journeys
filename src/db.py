from mysql.connector import connect
from typing import Literal


class DatabaseClient:

    allowed_dialects = ["MySQL", "PostgreSQL", "SQLite"]

    def __init__(
        self, host: str, port: str, database: str, user: str, password: str
    ) -> None:
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def create_connection_uri(self, dialect: Literal["MySQL", "PostgreSQL", "SQLite"]):

        connection_uri = None

        if dialect not in self.allowed_dialects:
            raise TypeError(
                f"Not allowed. Only the following dialects are allowed: {self.allowed_dialects}"
            )

        if dialect in ["MySQL"]:

            dialect_driver_mapping = {"MySQL": "mysql+mysqlconnector"}
            dialect_driver = dialect_driver_mapping[dialect]

            connection_uri = f"{dialect_driver}://{self.user}:{self.password}@{self.host}/{self.database}"
            return connection_uri

        if dialect == "SQLite":
            raise NotImplementedError

    def open_connection(self):
        self.conn = connect(
            user=self.user, password=self.password, host=self.host, database="mysql"
        )

    def close_connection(self):
        self.conn.close()

    def create_database(self, database):
        self.open_connection()
        self.run_query(f"CREATE DATABASE IF NOT EXISTS {database}")
        self.close_connection()

    def run_query(self, query_string):
        result = self.conn.cmd_query(query_string)
        return result
