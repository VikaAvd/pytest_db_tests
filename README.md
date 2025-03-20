# PyTest MSSQL Database Tests

This project contains automated tests using **PyTest** to verify data in a Microsoft SQL Server database. The tests validate data in the `[TRN]` database under the `hr` schema by executing SQL queries against three tables.

## Table of Contents
- [Overview](#overview)
- [Test Cases Description](#test-cases-description)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Tests](#running-the-tests)
- [Test Reports](#test-reports)
- [Troubleshooting](#troubleshooting)

## Overview
This project uses **PyTest** along with **pyodbc** to connect to a SQL Server instance, execute queries, and validate data from the following tables:
- `[TRN].[hr].[employees]`
- `[TRN].[hr].[jobs]`
- `[TRN].[hr].[locations]`

## Test Cases Description
The project implements six test cases (two per table):

**Employees Table:**
- **TC_EMPLOYEE_COUNT:** Verifies that the total number of employees in the `[hr].[employees]` table is greater than zero.
- **TC_EMPLOYEE_AVG_SALARY:** Verifies that the average salary in the `[hr].[employees]` table is within an expected range (e.g., between 1000 and 20000).

**Jobs Table:**
- **TC_JOBS_MIN_LESS_THAN_MAX:** Confirms that for each job in `[hr].[jobs]`, the `min_salary` is less than the `max_salary`.
- **TC_JOBS_UNIQUE_TITLES:** Ensures that every job title in `[hr].[jobs]` is unique (i.e., no duplicate titles).

**Locations Table:**
- **TC_LOCATIONS_NOT_NULL_CITY:** Validates that the `city` column in the `[hr].[locations]` table does not contain NULL values.
- **TC_LOCATIONS_COUNTRY_ID_LENGTH:** Checks that the `country_id` in the `[hr].[locations]` table is exactly 2 characters long.

## Prerequisites
- **Python 3.8+** (Tested with Python 3.12)
- **PyTest**
- **pyodbc**
- **pytest-html** (for generating an HTML report)
- A running **Microsoft SQL Server** instance with the `TRN` database and `hr` schema.
- The correct **ODBC Driver 17 for SQL Server** or **ODBC Driver 18 for SQL Server** installed (64-bit recommended).
- A database login (e.g., `robot`) with appropriate permissions on the `TRN` database (more details in the `SQL Server User Setup` section below)

## Project Structure
```bash
pytest_db_tests/
├── tests/
│   ├── conftest.py          # PyTest fixture for DB connection
│   ├── test_employees.py    # Tests for the employees table
│   ├── test_jobs.py         # Tests for the jobs table
│   └── test_locations.py    # Tests for the locations table
├── db_connection.py         # Contains the database connection helper function
├── requirements.txt         # List of required Python packages
├── README.md                # Project instructions
└── output/                  # Folder where test reports (e.g., HTML) are generated
```

## Installation
1. **Clone the Repository**  
- `git clone https://github.com/VikaAvd/pytest_db_tests.git`
- `cd pytest_db_tests`

2. **Install Python Dependencies:** 
Ensure you have Python installed, then run:
- `pip install -r requirements.txt`

## Configuration
1. **Database Connection**
Open the file `db_connection.py` and update the connection string parameters with your values:
- SERVER: e.g., EPUALVIW059D\\SQLEXPRESS01 
- DATABASE: TRN
- UID: robot
- PWD: Vika_password123
- ODBC Driver: The connection string uses `ODBC Driver 17 for SQL Server` and includes additional parameters:`Encrypt=no;TrustServerCertificate=yes;` for the 18 version.
- Note: If your SQL Server uses dynamic ports, update the connection settings in db_connection.py accordingly. Ensure that the port specified matches your SQL Server’s configuration.


2. **SQL Server User Setup:**  
  NOTE: do not create the user 'robot' if it's already exist!
  
  To create the `robot` login and give it the necessary permissions on the `TRN` database, you can run the following T-SQL commands in SQL Server Management Studio (SSMS) as an administrator:

   ```sql
   --Creating a user if it doesn't already exist (you may use your own login and password - just update the corresponding settings in db_connection.robot).
   USE [TRN];
   GO
   -- Create a login at the server level 
   CREATE LOGIN robot WITH PASSWORD = 'Vika_password123';
   GO

   -- Create a user in TRN database mapped to that login
   CREATE USER robot FOR LOGIN robot WITH DEFAULT_SCHEMA = hr;
   GO

   -- Grant the necessary permissions (read, etc.)
   GRANT SELECT ON SCHEMA::hr TO robot;
   GO
   ```

3. **SQL Server Requirements**
- Ensure TCP/IP is enabled for your SQL Server instance.
- The SQL Server Browser service should be running.
- The robot login must have proper permissions on the TRN database (connect as an admin, navigate to TRN > Security > Users, right-click "robot", open Properties, and confirm in the Membership tab that db_datareader is checked).

## Running the Tests
- To run all tests from the project root use one of the options below:
   - `pytest`
   - `pytest -rbA`
   - `pytest -vv`
 
- To generate an HTML report, run:
   - `pytest --html=output/report.html --self-contained-html`
   - After running the tests with `pytest --html=output/report.html --self-contained-html`, open output/report.html in your web browser to view the detailed test report.

## Test Reports
After running the tests, the following will be generated:
- Console output: A summary of test results.
- HTML Report: If using pytest-html, open output/report.html in your browser to view detailed results.
- Other formats: PyTest can generate additional report types if configured.

## Troubleshooting
Connection Issues:
If you receive errors verify that:
- ODBC Driver: The correct ODBC driver is installed and visible to Python.
- SQL Server Connectivity: Ensure TCP/IP is enabled and the correct server information is configured in db_connection.py.
- SQL Server Browser is running.
- Permissions: Confirm that the user has the required permissions on the TRN database.
- Module Import Issues: If you encounter ModuleNotFoundError for db_connection, ensure your PYTHONPATH is set correctly or run tests from the project root.

Test Failures:
- Review the PyTest console output and the HTML report (if generated) for detailed error messages.
- Check your SQL queries and database connection settings for any discrepancies.
