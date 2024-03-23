import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='CS2020!',database='CSMS')
mycursor=mydb.cursor()

wid=int(input('Enter worker id:'))

 
ch='Y'
while ch=='Y':
   op=int(input('''\nPRESS
1.TO VIEW YOUR DETAILS
2.TO VIEW YOUR MONTHWISE SALARY
3.TO VIEW YOUR MONTHWISE ATTENDANCE
4.TO VIEW YOUR LEAVE DETAILS MONTHWISE(TOTAL NO.OF APPROVED LEAVES/UNAPPROVED LEAVES)
(NOTE:MONTHWISE DETAILS SHOULD BE VIEWED AT THE END OF THE MONTH OR ELSE YOU WILL GET TO KNOW DETAILS OF ONLY THOSE DAYS YOU CAME TO WORK IN THAT MONTH)
5.TO EXIT

ENTER YOUR CHOICE:'''))
 
   print("\n")
    
   if op==1:
         print('\nTHE DETAILS ARE IN THE FOLLOWING ORDER:')
         print('(ID,NAME,JOB,WAGE PER HOUR,DOB,PROOF GIVEN FOR DOB,JOINING DATE,LEAVING DATE,CONTACT,ADDRESS,GENDER)\n')
         mycursor.execute("select * from mgr where id='"+str(wid)+"'")
         row = mycursor.fetchone()
         if row == None:
            print("This worker id does not exist in records!")
         else:
            print(row)
         print('PROOF FOR DOB:BC-BIRTH CERTIFICATE,CTC-CLASS TENTH/TWELFTH CERTIFICATE,AC-AADHAR CARD')

   elif op==2:
       print('\n(MONTH,SALARY)')
       mycursor.execute(" select monthname(s.date) as MONTH,hour(s.outtime-s.intime)*m.wageph as SALARY from supvr s,mgr m where m.id='"+str(wid)+"' group by monthname(s.date)")
       for x in mycursor:
          print(x)
   elif op==3:
       print('\n(MONTH,ATTENDANCE)')
       mycursor.execute("select monthname(date) as MONTH,count(*) as ATTENDANCE from supvr where id='"+str(wid)+"' group by monthname(date)")
       row = mycursor.fetchone()
       if row == None:
            print("This worker id does not exist in records!")
       else:
            print(row)

   elif op==4:
       print('\n(MONTH,APPROVED-LEAVES,UNAPPROVED-LEAVES)')
       mycursor.execute("select monthname(date) as MONTH,approvedl as APPROVED_LEAVES,unapprovedl as UNAPPROVED_LEAVES from supvr where id='"+str(wid)+"' group by monthname(date)")
       row = mycursor.fetchone()
       if row == None:
            print("This worker id does not exist in records!")
       else:
            print(row)
       
   elif op==5:
        break
   else:
        print("\nINVALID CHOICE! TRY AGAIN")

       
