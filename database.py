import mysql.connector
conn=mysql.connector.Connect(host="localhost",user="root",passwd="Toor",port='3309')
cur=conn.cursor()
cur.execute("create database emp_prj;")
conn.close()
conn=mysql.connector.Connect(host="localhost",user="root",passwd="Toor",port='3309',database="emp_prj")
cur=conn.cursor()
cur.execute("create table Emp_Info(id int(50) AUTO_INCREMENT PRIMARY KEY,eid varchar(50),Name varchar(50),phone_no varchar(50),roles varchar(50));")
cur.execute("create table Details_emp(id int(50) AUTO_INCREMENT PRIMARY KEY,eid varchar(50),start_time varchar(50),abandoned_resolved varchar(50),answer_time varchar(50),resolved_time varchar(50),abandoned_time varchar(50));")


