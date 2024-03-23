
def mainmenu():

  print("\t\t-----------------------------------------------------------------------------")
  print("\t\t*************WELCOME TO CONSTRUCTION SITE MANAGEMENT SYSTEM(CSMS)************")
  print("\t\t-----------------------------------------------------------------------------")

mainmenu()
while True:
    print("\n\t\t*********************************| MAIN MENU |*******************************")
    ch=int(input('''PRESS:
1.FOR MANAGER
2.FOR SUPERVISOR
3.FOR GOVT ADMINISTRATOR
4.FOR WORKER
5.TO EXIT
ENTER YOUR ROLE:'''))
    if ch==1:
        import manager
    elif ch==2:
        import supervisor
    elif ch==3:
        import administrator
    elif ch==4:
        import worker
    elif ch==5:
        break
    else:
        print("INVALID CHOICE! TRY AGAIN")
    

