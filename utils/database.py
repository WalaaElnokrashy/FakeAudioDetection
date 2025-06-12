import pyodbc
from config import Config

def get_db_connection():
    try:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={Config.SQL_SERVER};"
            f"DATABASE={Config.DATABASE};"
            f"Trusted_Connection=yes;"
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None