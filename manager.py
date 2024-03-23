import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='CS2020!',database='CSMS')
mycursor=mydb.cursor()
def insert():
    
        wid=int(input('Enter worker_id:'))
        name=input('Enter worker name:')
        job=input('Enter job:')
        wage=int(input('Enter wage per hour:'))
        dob=input("Enter date of birth(in the format YYYY-MM-DD):")
        proof=input('Enter proof given for dob(Birth certificate(BC)/Class 10th or 12th certificate(CTC)/Aadhar card(AC)):')
        jdate=input("Enter date of joining(in the format YYYY-MM-DD):")
        ldate=input("Enter date of leaving(in the format YYYY-MM-DD) otherwise enter(1000-10-10) if the worker is presently working:")
        cno=input('Enter contact no. of worker:')
        address=input('Enter address of worker:')
        gender=input('Enter gender of worker(M/F):')
        
        mycursor.execute("insert into mgr values('"+str(wid)+"','"+name+"','"+job+"','"+str(wage)+"','"+str(dob)+"','"+proof+"','"+str(jdate)+"','"+str(ldate)+"','"+cno+"','"+address+"','"+gender+"')")
        mydb.commit()
        

def fetchall():    
  mycursor.execute("select * from mgr")
  myrecords=mycursor.fetchall()
  for x in myrecords:
     print (x)


def search():
    wid=input('Enter id of worker whose record is to be searched for:')
    mycursor.execute('select * from mgr where id="'+str(wid)+'"')
    row = mycursor.fetchone()
    if row == None:
       print("This worker id does not exist in records!")
    else:
        print(row)


def update():
    cid=int(input('Enter id of worker whose record is to be updated:'))
    x=int(input('''Enter field to be updated,PRESS
1.FOR (JOB/NAME/DOB/PROOF/JDATE/LDATE/CONTACT/ADDRESS/GENDER)
2.FOR (ID/WAGEPH)
ENTER YOUR CHOICE:'''))
    
    if x==1:
         y=int(input('''Press:
1-JOB,2-NAME,3-DOB,4-PROOF,5-JDATE,6-LDATE,7-CONTACT,8-ADDRESS,9-GENDER
ENTER YOUR CHOICE:'''))

         z=input('Enter new value:')
         if y==1:
              mycursor.execute("update mgr set job='"+z+"' where id='"+str(cid)+"'")
         elif y==2:
              mycursor.execute("update mgr set name='"+z+"' where id='"+str(cid)+"'")
         elif y==3:
             mycursor.execute("update mgr set dob='"+z+"' where id='"+str(cid)+"'")
         elif y==4:
             mycursor.execute("update mgr set proof='"+z+"' where id='"+str(cid)+"'")
         elif y==5:
             mycursor.execute("update mgr set jdate='"+z+"' where id='"+str(cid)+"'")
         elif y==6:
             mycursor.execute("update mgr set ldate='"+z+"' where id='"+str(cid)+"'")
         elif y==7:
             mycursor.execute("update mgr set contact='"+z+"' where id='"+str(cid)+"'")
         elif y==8:
             mycursor.execute("update mgr set address='"+z+"' where id='"+str(cid)+"'")
         elif y==9:
             mycursor.execute("update mgr set gender='"+z+"' where id='"+str(cid)+"'")
         mydb.commit()


    elif x==2:
        y=int(input('''Press:
1-ID,2-WAGEPH
ENTER YOUR CHOICE:'''))
        z=int(input('Enter new value:'))
        if x==1:
           mycursor.execute("update mgr set id='"+str(z)+"' where id='"+str(cid)+"'")
        elif x==2:
           mycursor.execute("update mgr set wageph='"+str(z)+"' where id='"+str(cid)+"'")
        mydb.commit()
    print('Record is successfully updated!')



def rowcount():
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("select * from mgr")
    noofrows=mycursor.rowcount
    print("No. of records in mgr table are:",noofrows)

def attendtod():
     d=input("Enter today's date(IN THE FORMAT YYYY-MM-DD):")
     print("\n(CATEGORY,ATTENDANCE_TODAY)")
     mycursor.execute("select job as CATEGORY,count(job) as ATTENDANCE_TODAY  from supvr where date='"+d+"' group by job")
     for x in mycursor:
        print(x)


def attendmon():
    print("(MONTH,CATEGORY,ATTENDANCE)")
    mycursor.execute("select monthname(date) as MONTH,job as CATEGORY,count(job) as ATTENDANCE from supvr group by job,monthname(date)")
    for x in mycursor:
        print(x)

        
def workop():
      d=input("Enter today's date(IN THE FORMAT YYYY-MM-DD):")
      print("\n(CATEGORY,NOOFWORKERS,MANHOURS)")
      mycursor.execute("select job as CATEGORY,count(job) as NOOFWORKERS,sum(hour(outtime-intime)) as MANHOURS from supvr where date='"+d+"' group by job")
      for x in mycursor:
        print(x)
        
def totalcost():
        
        print("\n(MONTH,JOB,NOOFWORKERS,WAGEPH,TOTAL_WHRS,TOTALCOST)")
        mycursor.execute(" select monthname(date) as MONTH,JOB,count(job) as NOOFWORKERS,WAGEPH,sum(hour(outtime-intime)) as TOTAL_WHRS,sum(hour(outtime-intime)*wageph) as TOTALCOST from supvr group by job,monthname(date)")
        for x in mycursor:
          print(x)


def complains():
    print("\n(ID,COMPLAINS)")
    mycursor.execute(' select ID,COMPLAINS from supvr where complains is not null')
    for x in mycursor:
        print(x)


        
ch='Y'
while ch=='Y':
    op=int(input('''\nPRESS
1.TO INSERT A NEW RECORD
2.TO DISPLAY ALL THE RECORDS(TO VIEW THE DETAILS OF ALL WORKERS)
3.TO SEARCH FOR A RECORD
4.TO UPDATE A RECORD
5.TO COUNT NO.OF RECORDS IN THE TABLE
6.TO VIEW TODAY'S ATTENDANCE PER CATEGORY OF WORKER
7.TO VIEW MONTHWISE ATTENDANCE PER CATEGORY OF WORKER
8.TO VIEW TODAY'S WORK OUTPUT IN MAN HOURS PER CATEGORY OF WORKER
9.TO VIEW TOTAL COST BEARED PER TYPE OF WORKER MONTHWISE
10.TO VIEW COMPLAINS REGARDING ANY WORKER IF ANY
11.TO EXIT

ENTER YOUR CHOICE:'''))
    print("\n")
    if op==1:
         insert()
    elif op==2:
        fetchall()
    elif op==3:
         search()
    elif op==4:
        update()
    elif op==5:
         rowcount()
    elif op==6:
        attendtod()
    elif op==7:
        attendmon()
    elif op==8:
        workop()
    elif op==9:
        totalcost()
    elif op==10:
        complains()
    elif op==11:
        break
    else:
        print("\nINVALID CHOICE! TRY AGAIN")
    
      
   

       
