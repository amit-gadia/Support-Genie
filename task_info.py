import mysql.connector
import datetime
a=datetime.datetime.now()
conn=mysql.connector.Connect(host="localhost",user="root",passwd="Toor",port="3309",database="emp_prj")
cur=conn.cursor()
cur.execute("show tables;")
print(cur.fetchall())
cur.execute("select * from details_emp;")
print(cur.fetchall())
eid=input("Enter EID: ")
start_time=a.date()
check=int(input("1. Abandoned \n2. Resolved\n"))
if(check==1):
    abandoned_resolved="abandoned"
    abandoned_time=input("Abandoned_time (YYYY-MM-DD): ")
    answer_time=""
    resolved_time=""
elif(check==2):
    abandoned_resolved="resolved"
    abandoned_time=""
    answer_time=input("Answer_time (YYYY-MM-DD): ")
    resolved_time=input("Resolved_time (YYYY-MM-DD): ")
cur.execute("insert into details_emp(eid,start_time,abandoned_resolved,answer_time,resolved_time,abandoned_time) values(%s,%s,%s,%s,%s,%s);",(eid,start_time,abandoned_resolved,answer_time,resolved_time,abandoned_time))
conn.commit()