import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from db_connection import get_db_connection

def test_locations_not_null_city():
    """
    TC_LOCATIONS_NOT_NULL_CITY:
    Verify city is not NULL for any location.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM hr.locations WHERE city IS NULL;")
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    assert row[0] == 0, f"Found {row[0]} locations with NULL city"

def test_locations_country_id_length():
    """
    TC_LOCATIONS_COUNTRY_ID_LENGTH:
    Verify country_id is exactly 2 characters long.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM hr.locations WHERE LEN(country_id) <> 2;")
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    assert row[0] == 0, f"Found {row[0]} locations with invalid country_id length"
