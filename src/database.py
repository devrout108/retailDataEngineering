import os
from loguru import logger
import mysql.connector
from dotenv import load_dotenv


load_dotenv()


class DatabaseConnection:

    def __init__(self):
        self.connection = None

    def connect(self):

        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        logger.info("MySQL connected successfully")

        return self.connection

    def close(self):

        if self.connection:
            self.connection.close()
            print("MySQL connection closed")


if __name__ == "__main__":

    db = DatabaseConnection()

    connection = db.connect()

    db.close()            