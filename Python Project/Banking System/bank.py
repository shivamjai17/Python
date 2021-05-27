from getpass import getpass
import time
import os
import random
import json
with open('bank.json') as fp:
    bank=json.load(fp)
    fp.close()
def update():
    fp=open('bank.json','w')
    json.dump(bank,fp)
    fp.close()
def choice(i):
    print(f"Welcome Back !{bank['user'][i]}")
    print('\n\nMENU\n')
    print('1. Debit')
    print("2. Credit")
    print("3. Balance Enquiry")
    print("4. Profile Updation")
    print("5. Logout")
    c=int(input('Enter Your Choice'))
    if c==1:
        debit(i)
    elif c==2:
        credit(i)
    elif c==3:
        chk_bal(i)
    elif c==4:
        profile(i)
    elif c==5:
        main()
    else:
        print('Invalid Choice\nTry again')
def debit(i):
    global bank
    print('\nWelcome to Debit Service\n')
    amount=int(input('Enter Amount to Debit'))
    if amount >bank['bal'][i]:
        print("Insufficiant balance\n You have only{} rs ".format(bank['bal'][i]))
        print('\nTry Again')
        debit(i)
    else:
        bank['bal'][i]-=amount
        update()
        print('You Withdraw {} rs and current balance :{} in your account'.format(amount,bank['bal'][i]))
        choice(i)
def credit(i):
    global bank
    print('\n\nWelcome to Credit Services\n')
    amount=int(input('Enter amount to deposite : '))
    bank['bal'][i]+=amount
    update()
    print("Current amount : {} rs in your account\n{} credited sucesfully in your account".format(bank['bal'][i],amount))
    choice(i)
def chk_bal(i):
    print('\nWelcome to Balance enquiry\n')
    print('Name =',bank['user'][i])
    print('Account Number=',bank['acc'][i])
    print('Balance=',bank['bal'][i])
    choice(i)
def profile(i):
    print("\nWelcome {}\n".format(bank['user'][i]))
    print("1. Update Name")
    print("2. Update Password")
    print('3. Delete Account')
    print('4. Logout')
    c=int(input("Enter Your Choice"))
    if c==1:
        name=input('Enter New name : ')
        bank['user'][i]=name
        update()
        choice(i)
    elif c==2:
        cpa=getpass('\nEnter Current Password :')
        if cpa==bank['passwd'][i]:
            np=input("\nEnter New Password :")
            cp=("Confirm Password : ")
            if np==cp:
                bank['passwd'][i]=np
                update()
                print('Password Updated Succesfull')
            else:
                print("\nPassword Didn't Match")
                print('\nTry Again')
                profile(i)
        else :
            print('Password Incorrect')
            main()
    elif c==3:
         bank['name'].pop(i)
         bank['acc'].pop(i)
         bank['passwd'].pop(i)
         bank['bal'].pop(i)
         update()
         print("\nYour Account Sucessfully Deleted")
         print('\nBye Bye!')
         main()
    elif c==4:
        main()
    else:
        print('\nwrong Choice Try Again')
        profile(i)

def login():
    print('Welcome to Login Servicess')
    print("\n\n")
    acc_no=int(input('Enter Account Number : '))
    passw=getpass('Enetr password : ')
    if acc_no in bank['acc']:
        i=bank['acc'].index(acc_no)
        if passw in bank['passwd'][i]:
            print('You are Loged In')
            choice(i)
        else :
            print('Wronng Password Try Again :')
            login()
    else :
        print('No Registerd Account Found\n You Should Signup First')
    
def signup():
    name=input('Enter name : ')
    bal=int(input('Enter Balance'))
    pas=getpass('Enter Password')
    acc=bank['acc'][-1]+1
    bank['user'].append(name)
    bank['passwd'].append(pas)
    bank['bal'].append(bal)
    bank['acc'].append(acc)
    update()
    print(f"Your Account Nomber is:{acc}")
    print('Thanks for opening account')
def main():
    print("INDIAN BANK".center(157,'*'))
    print("   Menu  \n")
    print(" 1.Login\n 2.SignUp\n 3.Exit")
    ch = int(input("Enter your Choice : "))
    print()
    if ch == 1 : 
        login()
    elif ch == 2 :
        signup()
    elif ch == 3 :
        print('Thanks For Visiting')
        exit()   
    else :
        print("\n\nInvalid Input\nTry Again")
        main()    
if __name__ =="__main__" :
    main()

