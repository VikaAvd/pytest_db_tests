def test_employee_count(db_conn):
    """
    TC_EMPLOYEE_COUNT:
    Verify total number of employees is greater than zero.
    """
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM hr.employees;")
    row = cursor.fetchone()
    cursor.close()

    assert row[0] > 0, f"Expected employee count > 0, got {row[0]}"


def test_employee_avg_salary(db_conn):
    """
    TC_EMPLOYEE_AVG_SALARY:
    Verify the average salary is between 1000 and 20000.
    """
    cursor = db_conn.cursor()
    cursor.execute("SELECT AVG(salary) FROM hr.employees;")
    row = cursor.fetchone()
    cursor.close()

    avg_salary = row[0]
    assert 1000 <= avg_salary <= 20000, f"Average salary out of range: {avg_salary}"

