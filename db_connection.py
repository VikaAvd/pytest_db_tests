import pyodbc

def get_db_connection():
    """
    Adjust for your environment with your values.
    Connection string uses ODBC Driver 17 for SQL Server, with extra parameters for Driver 18 if needed.
    """
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=EPUALVIW059D\\SQLEXPRESS01;"
        "DATABASE=TRN;"
        "UID=robot;"
        "PWD=Vika_password123;"
        "Encrypt=no;"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(conn_str)

import pyodbc

