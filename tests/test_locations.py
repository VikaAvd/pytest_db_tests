def test_locations_not_null_city(db_conn):
    """
    TC_LOCATIONS_NOT_NULL_CITY:
    Verify that the city column in the hr.locations table is not NULL for any location.
    """
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM hr.locations WHERE city IS NULL;")
    row = cursor.fetchone()
    cursor.close()

    assert row[0] == 0, f"Found {row[0]} locations with NULL city"


def test_locations_country_id_length(db_conn):
    """
    TC_LOCATIONS_COUNTRY_ID_LENGTH:
    Verify that the country_id in the hr.locations table is exactly 2 characters long.
    """
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM hr.locations WHERE LEN(country_id) <> 2;")
    row = cursor.fetchone()
    cursor.close()

    assert row[0] == 0, f"Found {row[0]} locations with invalid country_id length"
