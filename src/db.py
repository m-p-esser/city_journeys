from typing import Literal
import csv
from mysql.connector import connect
import pandas as pd
from sqlalchemy import create_engine
from config.config import db_config
from src.utils import find_root, recursively_find_file


class DatabaseClient:

    allowed_dialects = ["MySQL", "PostgreSQL", "SQLite"]

    def __init__(self) -> None:
        self.conn = None
        self.config = db_config

    def create_connection_uri(
        self,
        dialect: Literal["MySQL", "PostgreSQL", "SQLite"],
    ):
        connection_uri = None

        if dialect not in self.allowed_dialects:
            raise TypeError(
                f"Not allowed. Only the following dialects are allowed: {self.allowed_dialects}"
            )

        if dialect in ["MySQL"]:

            dialect_driver_mapping = {"MySQL": "mysql+mysqlconnector"}
            dialect_driver = dialect_driver_mapping[dialect]

            connection_uri = f"{dialect_driver}://{db_config.DB_USER_NAME}:{db_config.DB_USER_PASSWORD}@{db_config.DB_HOST_IP}/{db_config.DB_NAME}"
            return connection_uri

        if dialect == "SQLite":
            raise NotImplementedError

    def create_engine(self, dialect: Literal["MySQL", "PostgreSQL", "SQLite"]):
        connection_uri = self.create_connection_uri(dialect)
        engine = create_engine(connection_uri)
        return engine

    def open_connection(self):
        self.conn = connect(
            user=db_config.DB_USER_NAME,
            password=db_config.DB_USER_PASSWORD,
            host=db_config.DB_HOST_IP,
            database="mysql",
        )

    def close_connection(self):
        self.conn.close()

    def create_database(self, database):
        self.open_connection()
        self.run_query(f"CREATE DATABASE IF NOT EXISTS {database}")
        self.close_connection()

    def run_query(self, query_string):
        self.open_connection()
        result = self.conn.cmd_query(query_string)
        self.close_connection()
        return result

    def insert_from_csv(self, file_name, table_name, database, chunk_size):
        file_type = file_name.split(".")[-1]

        if file_type != "csv":
            raise NotImplementedError

        root_dir = find_root()
        csv_file_path = recursively_find_file(root_dir, file_name)

        engine = self.create_engine("MySQL")

        df = pd.read_csv(csv_file_path, sep=",")
        df.to_sql(
            name=table_name,
            con=engine,
            schema=database,
            if_exists='append',
            chunksize=chunk_size,
            index=False
        )

        # self.open_connection()

        # cur = self.conn.cursor()
        # with open(csv_file_path) as fp:
        #     reader = csv.reader(fp, delimiter=",")
        #     for idx, row in enumerate(reader):
        #         if idx == 0:
        #             header_columns = row
        #             value_placeholders = ",".join(["%s"] * len(header_columns))
        #             # print(value_placeholders)
        #             header_columns = ",".join(header_columns)
        #         if idx > 0 & idx < 10:
        #             # row = ",".join(f"'{c}'" for c in row)
        #             sql = f"INSERT INTO {database}.{table_name} ({header_columns}) VALUES ({value_placeholders})"
        #             cur.execute(sql, row)
        #             # self.run_query(sql)
        # cur.close()

        # self.close_connection()
