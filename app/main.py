from database.PostgresConnection import PostgresConnection
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text
load_dotenv()

def test_engine_connection(engine):
    """
    Tests if the SQLAlchemy engine is connected to the PostgreSQL database.
    
    Args:
        engine (Engine): The SQLAlchemy engine to test.

    Returns:
        bool: True if the connection is successful, False otherwise.
    """
    try:
        # Try to execute a simple query to check if the connection is valid
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            # Fetch result to ensure the query was successful
            return result.scalar() == 1
    except Exception as e:
        # Print exception and return False if any error occurs
        print(f"Connection test failed: {e}")
        return False

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_DATABASE = os.getenv('DB_DATABASE')
if __name__ == '__main__':
    pc: PostgresConnection = PostgresConnection(DB_USER,DB_PASSWORD,DB_HOST,DB_DATABASE)
    engine = pc.get_engine()
    print(test_engine_connection(engine))
    