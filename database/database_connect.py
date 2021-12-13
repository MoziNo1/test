import pymysql
import re

db_host = '172.21.12.33'
db_login_name = 'root'
db_login_password = 'root1234'
db_name = "zhangzihantest"

global db
try:
    db = pymysql.connect(user=db_login_name, host=db_host, password=db_login_password, database=db_name)
    print("连接成功")
except pymysql.err as e:
    print(e)
cur = db.cursor()
# cur.execute("select * from student")
# data = cur.fetchall()
# print(data)

create_table_sql = """create table classroom ( 
                    id varchar(20),
                    name varchar(20),
                    age int
                   )"""
insert_sql = """insert into classroom (id,name,age) values (1,'长子',18)"""
search_sql = "select * from classroom"
cur.execute(create_table_sql)
try:
    cur.execute(create_table_sql)
    db.commit()
except:
    db.rollback()

cur.execute(insert_sql)
cur.execute(search_sql)
# 当元组只有一个元素时，后面必须跟上一个逗号
data1 = cur.fetchall()
print(data1)

