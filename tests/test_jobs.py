import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from db_connection import get_db_connection

def test_jobs_min_less_than_max():
    """
    TC_JOBS_MIN_LESS_THAN_MAX:
    Verify min_salary < max_salary for each job.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT job_id, min_salary, max_salary FROM hr.jobs;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    for row in rows:
        min_sal = row[1]
        max_sal = row[2]
        assert min_sal < max_sal, f"min_salary {min_sal} not < max_salary {max_sal} for job_id {row[0]}"

def test_jobs_unique_titles():
    """
    TC_JOBS_UNIQUE_TITLES:
    Verify that each job title is unique.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT job_title, COUNT(*) as title_count
        FROM hr.jobs
        GROUP BY job_title
        HAVING COUNT(*) > 1
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    assert len(rows) == 0, f"Found duplicate job titles: {rows}"
