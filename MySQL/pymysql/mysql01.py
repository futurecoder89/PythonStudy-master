'''
폴더명 : pymysql
파일명 : mysql01.py
'''
# Step1  pymysql 모듈 불러오기
import pymysql

# Step2 Mysql Connection 연결
con = pymysql.connect(
    host='172.16.12.101',
    user='scott',
    password='tiger',
    db='hr',
    charset='UTF8')

# Step3 Connection 으로부터 Cursor 생성
cur = con.cursor();

# Step4 Sql문 실행
sql = 'SELECT empno, ename, job FROM emp'
cur.execute(sql)

# 데이타 Fetch
rows = cur.fetchall();
print(rows) 

# Step5 DB 연결 종료
con.close()



