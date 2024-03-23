
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='CS2020!',database='CSMS')
mycursor=mydb.cursor()


ch='Y'
while ch=='Y':
   op=int(input('''\nPRESS
1.TO VIEW THE DETAILS OF ALL WORKERS
2.TO VIEW MAXIMUM WORKING HOURS PER DAY OF EACH WORKER
3.TO VIEW THOSE WORKERS WORKING BEYOND THE GOVT SPECIFIED TIME LIMIT(>10 HRS PER DAY)
4.TO VIEW ANY CHILD LABOURS IF ANY(WORKING BELOW THE AGE OF 14,CHECKING JOINING DATE<01-12-2000)
5.TO VIEW THOSE WORKERS NOT BEING PAID MINIMUM SALARY AS PER GOVT RULES(MINIMUM SALARY:FOR MALES>=60 AND FOR FEMALES>=50 PER HOUR)
6.TO EXIT

ENTER YOUR CHOICE:'''))
 
   print("\n")
    
   if op==1:
         print('\nTHE DETAILS ARE IN THE FOLLOWING ORDER:')
         print('(ID,NAME,JOB,WAGE PER HOUR,DOB,PROOF GIVEN FOR DOB,JOINING DATE,LEAVING DATE,CONTACT,ADDRESS,GENDER)\n')
         mycursor.execute("select * from mgr ")
         for x in mycursor:
            print(x)
         print('PROOF FOR DOB:BC-BIRTH CERTIFICATE,CTC-CLASS TENTH/TWELFTH CERTIFICATE,AC-AADHAR CARD')



   elif op==2:
       print('\n(ID,NAME,JOB,MAX_WHRS)')
       mycursor.execute("select m.id as ID,m.name as NAME,m.job as JOB,max(hour(s.outtime-s.intime)) as MAX_WHRS from mgr m,supvr s group by id")
       for x in mycursor:
            print(x)
        
   elif op==3:
       print('\n(ID,NAME,JOB,WHRS)')
       mycursor.execute('''select m.id as ID,m.name as NAME,m.job as JOB,hour(s.outtime-s.intime) as WHRS from mgr m,supvr s
       where hour(s.outtime-s.intime)>10 group by m.id''')
       for x in mycursor:
            print(x)
        

   elif op==4:
       print('\n(ID,NAME,JOB,DOB,JDATE)')
       mycursor.execute(" select id as ID,name as NAME,job as JOB,DOB,JDATE  from mgr  where jdate<'2000-12-01'")
       for x in mycursor:
            print(x)
       print("NOTE:THIS IS CONSIDERING THE MINIMUM AGE FROM WHICH THE WORKER STARTED WORKING")      
       
      
         
   elif op==5:
       print('\n(NAME,ID,GENDER,JOB,WAGEPH)')
       m="M"
       f="F"
       mycursor.execute("select ID,NAME,GENDER,JOB,WAGEPH from mgr where gender='"+m+"' and wageph<61")
       for x in mycursor:
            print(x)
       mycursor.execute("select ID,NAME,GENDER,JOB,WAGEPH from mgr where gender='"+f+"' and wageph<51")
       for x in mycursor:
            print(x)    
      

   elif op==6:
        break
   else:
        print("\nINVALID CHOICE! TRY AGAIN")





