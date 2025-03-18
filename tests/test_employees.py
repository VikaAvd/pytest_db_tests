import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from db_connection import get_db_connection

def test_employee_count():
    """
    TC_EMPLOYEE_COUNT:
    Verify total number of employees is greater than zero.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM hr.employees;")
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    assert row[0] > 0, f"Expected employee count > 0, got {row[0]}"

def test_employee_avg_salary():
    """
    TC_EMPLOYEE_AVG_SALARY:
    Verify the average salary is between 1000 and 20000.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(salary) FROM hr.employees;")
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    avg_salary = row[0]
    assert 1000 <= avg_salary <= 20000, f"Average salary out of range: {avg_salary}"
