import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='CS2020!',database='CSMS')
mycursor=mydb.cursor()

def curdate():
   global d
   d=input("Enter today's date(IN THE FORMAT YYYY-MM-DD):")

curdate()
       


ch='Y'
while ch=='Y':
    op=int(input('''PRESS
1.TO INPUT INCOMING TIME
2.TO INPUT OUTGOING TIME
3.TO ENTER COMPLAIN REGARDING ANY WORKER
4.TO INPUT TOTAL NO.OF APPROVED LEAVES OF ANY WORKER FOR THIS MONTH
5.TO INPUT TOTAL NO.OF UNAPPROVED LEAVES OF ANY WORKER FOR THIS MONTH
NOTE:PLEASE ENTER 4. AND 5. AT THE MONTH END
6.TO EXIT

ENTER YOUR CHOICE:'''))
    print("\n")

    if op==1:
         wid=int(input('Enter worker id:'))
         x=mycursor.execute("select job from mgr where id='"+str(wid)+"'")
         y=mycursor.execute("select wageph from mgr where id='"+str(wid)+"'")
         it=input('Enter incoming time(IN THE FORMAT hh:mm):')
         mycursor.execute("insert into supvr(id,job,date,intime,wageph) values('"+str(wid)+"','"+x+"','"+d+"','"+it+"','"+y+"')")
         mydb.commit()

    elif op==2:
         wid=int(input('Enter worker id:'))
         ot=input('Enter outgoing time(IN THE FORMAT hh:mm):')
         mycursor.execute("update supvr set outtime='"+ot+"' where id='"+str(wid)+"'")
         mydb.commit()

    

    elif op==3:
       wid=int(input('Enter worker id:'))
       c=input('Enter complain(regarding workmanship/attendance/discipline etc):')
       mycursor.execute("update supvr set complains='"+c+"' where id='"+str(wid)+"'")
       mydb.commit()

    elif op==4:
       wid=int(input('Enter worker id:'))
       n=int(input('Enter total no.of approved leaves:'))
       mycursor.execute("update supvr set approvedl='"+str(n)+"' where id='"+str(wid)+"'")
       mydb.commit()

    elif op==5:
        wid=int(input('Enter worker id:'))
        n=int(input('Enter total no.of unapproved leaves:'))
        mycursor.execute("update supvr set unapprovedl='"+str(n)+"' where id='"+str(wid)+"'")
        mydb.commit()
       
    elif op==6:
        break
    else:
        print("\nINVALID CHOICE! TRY AGAIN")
    
      
    
