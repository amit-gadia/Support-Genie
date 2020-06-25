import mysql.connector
conn=mysql.connector.Connect(host="localhost",user="root",passwd="Toor",port="3309",database="emp_prj")
cur=conn.cursor(buffered=True) 
work_type=input("work_type : ")
sql="select eid,roles from emp_info;"
cur.execute(sql)
kk3=0
for i in cur.fetchall():
    vtr=0
    for j in i[1].split(","):
        if(j==work_type):
            vtr=1
    if(vtr>0):
        av_eid=i[0]    
        sql="select eid from details_emp;"
        cur.execute(sql)
        for k in cur.fetchall():
            if(k[0]==av_eid):
                sql="select abandoned_resolved,answer_time,resolved_time,abandoned_time from details_emp;"
                cur.execute(sql)
                for i in cur.fetchall():
                    if(i[0]=="resolved" and len(i[1]) != 0 and len(i[2]) != 0):
                        kk3=1
                    elif(i[0]=="abandoned" and len(i[3])!= 0):
                        kk3=1
if(kk3==1):
    print("IS AVAILABLE")
else:
    print("IS NOT AVAILABLE")
                