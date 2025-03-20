import pytest
import os
import sys

# Make sure Python can find db_connection.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db_connection import get_db_connection

@pytest.fixture(scope="session")
def db_conn():
    """
    Create a single DB connection for the entire test session.
    After all tests complete, the connection is closed.
    """
    conn = get_db_connection()
    yield conn
    conn.close()
