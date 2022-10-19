'''
파일명 : mysql02.py
'''
from sqlalchemy import create_engine
import pandas as pd

db_connection_str = 'mysql+pymysql://scott:tiger@172.16.12.101/hr?charset=utf8mb4'
db_connection = create_engine(db_connection_str)
conn = db_connection.connect()

sql = "select * from emp"

result = pd.read_sql_query(sql, conn)
print(pd.DataFrame(result))

conn.close()
