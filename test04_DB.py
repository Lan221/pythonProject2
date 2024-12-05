import pymysql
conn = pymysql.connect(host="192.168.213.128",port=8000,
                       user="root",password="root",database="ihrm",charset="utf8")

my_cursor = conn.cursor()
my_cursor.execute("select * from t_book")
result = my_cursor.fetchone()
print(result)
my_cursor.close()
conn.close()
