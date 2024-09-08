from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.pool import StaticPool
from typing import Optional

class PostgresConnection:
    """
    A class to manage PostgreSQL database connection using SQLAlchemy.

    Attributes:
        url (str): The database URL constructed from environment variables.
        engine (Optional[Engine]): The SQLAlchemy engine connected to the database.
    """

    def __init__(self,db_user:str,db_password:str,db_host:str,db_database:str) -> None:
        """
        Initializes the PostgresConnection with the database URL.

        The database URL is constructed using environment variables: DB_USER, DB_PASSWORD, DB_HOST, and DB_DATABASE.
        """
        #self.url: str = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_DATABASE')}"
        self.url: str = f"postgresql://{db_user}:{db_password}@{db_host}/{db_database}"
        self.engine: Optional[Engine] = None

    def get_engine(self) -> Engine:
        """
        Creates and returns a SQLAlchemy engine for the PostgreSQL database.

        Returns:
            Engine: The SQLAlchemy engine connected to the PostgreSQL database.
        """
        self.engine = create_engine(self.url, poolclass=StaticPool)
        return self.engine
