import psycopg2
from dotenv import load_dotenv
from config import (DATABASE, USER,
                    PORT, HOST, PASSWORD)

def connection_to_db():
    conn = psycopg2.connect(database = DATABASE,
                            user = USER, password = PASSWORD, 
                            host = HOST, port = PORT)
    if conn:
        cur=conn.cursor()
        return conn, cur
    
    else:
        return 'no connection established'
        