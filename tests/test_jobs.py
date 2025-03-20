def test_jobs_min_less_than_max(db_conn):
    """
    TC_JOBS_MIN_LESS_THAN_MAX:
    Verify that for each job, min_salary is less than max_salary.
    """
    cursor = db_conn.cursor()
    cursor.execute("SELECT job_id, min_salary, max_salary FROM hr.jobs;")
    rows = cursor.fetchall()
    cursor.close()

    for row in rows:
        min_sal = row[1]
        max_sal = row[2]
        assert min_sal < max_sal, f"min_salary {min_sal} not < max_salary {max_sal} for job_id {row[0]}"

def test_jobs_unique_titles(db_conn):
    """
    TC_JOBS_UNIQUE_TITLES:
    Verify that each job title is unique (no duplicates).
    """
    cursor = db_conn.cursor()
    cursor.execute("""
        SELECT job_title, COUNT(*) as title_count
        FROM hr.jobs
        GROUP BY job_title
        HAVING COUNT(*) > 1
    """)
    rows = cursor.fetchall()
    cursor.close()

    assert len(rows) == 0, f"Found duplicate job titles: {rows}"
