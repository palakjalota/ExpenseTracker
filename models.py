import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="palak",
   database = "mydatabase"
 )
cur = mydb.cursor()
#cur.execute("DROP TABLE IF EXISTS expenseman")
#cur.execute("create table expenseman (id INT AUTO_INCREMENT PRIMARY KEY,date date NOT NULL ,category text NOT NULL,sub_category text NOT NULL,expense integer NOT NULL)")

def create_exp(date,category,sub_category,expense):
    #lastconnection = datetime.strptime(date, "%d/%m/%Y").strftime('%Y-%m-%d')
    print(date)
    cur.execute('INSERT INTO expenseman (date,category,sub_category,expense) VALUES(%s,%s,%s,%s)',(date,category,sub_category,expense))
    mydb.commit()
    #con.close()


def get_exp():
    cur.execute('select * from expenseman')
    allexpense = cur.fetchall()
    return allexpense