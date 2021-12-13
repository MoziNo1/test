import pymysql

db_connect = pymysql.connect(host="172.21.12.33", db="dbtest", user="root", password="root1234")
cur = db_connect.cursor()
search_sql = """select * from crlmt_crg_inf where Cst_Numb = "CSTP2020006112" """
mm = cur.execute(search_sql)
print(mm)