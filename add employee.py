import mysql.connector

conn=mysql.connector.Connect(host="localhost",user="root",passwd="Toor",port="3309",database="emp_prj")
cur=conn.cursor(buffered=True) 

cur.execute("select id from emp_info;")
lenofid=len(cur.fetchall())
cur.execute("select id from emp_info;")
if(lenofid != 0):
    l_id=cur.fetchall()[-1][0]
elif(lenofid==0):
    l_id=0
phone_no=""
Name=""
Name=input("Enter Name Without Prefix: ")
phone_no=input("Enter Phone Number: ")
roles=""
for i in range(int(input("No. of roles: "))):
    roles=roles+input("Enter Role "+str(i+1)+": ")+","
print(roles)
tok=""
for i in Name.split(" "):
    tok=tok+i[0]
tok=tok+phone_no[len(phone_no)-2:]
tok=tok+str(int(l_id)+1)
print(tok,Name,phone_no,roles)

atok=str(tok)
aName=str(Name)
aphone_no=str(phone_no)
aroles=str(roles)

cur.execute("insert into emp_info(eid,Name,phone_no,roles) values(%s,%s,%s,%s);",(atok,aName,aphone_no,aroles))
conn.commit()