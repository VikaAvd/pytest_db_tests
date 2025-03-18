import pyodbc

def get_db_connection():
    # Adjust for your environment with your values.
    # This connection string uses ODBC Driver 17 for SQL Server. 
    # Extra parameters "Encrypt=no;TrustServerCertificate=yes;" are added for ODBC Driver 18 for SQL Server.
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

