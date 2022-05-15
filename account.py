from random import randrange
from time import sleep
class Account:
    
    def __init__(self, firstname, lastname, dob, gender):
        self.acc_number = str(dob) + str(randrange(100,999))
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.dob = dob
        self.balance = 0

        if gender == 1:
            sex = "Mr"
        else: 
            sex = "Mrs"
        print(f'Welcome {sex} {self.firstname}. You account has been sucessfully created')
        print(f"You account number is {self.acc_number}")
        print("----------------------")


    def deposit(self):
        amount = int(input("Insert the deposit amount(in $): "))
        self.balance += amount
        print(f" Your current balance is {self.balance}$")
        return self.balance

    def withdraw(self):
        amount = int(input("Insert the withdraw amount(in $): "))

        if (self.balance < amount):
            missing = amount - self.balance
            print(f"You don't have enough cash in you bank account. You need {missing} more $")
        else:
            self.balance -= amount
            print(f" Your current balance is {self.balance}$")
        return self.balance
    
    def view_account(self):
        print(f'Name: {self.firstname} {self.lastname}.\n Date of Birth: {self.dob}\n Gender:{self.gender}\nAccount Number: {self.acc_number}\n Balance: {self.balance}$')
        print("----------------------")


count = 0
while(True):
    if (count>0):
        sleep(5)
    print("________________")
    print("MENU INTERACTIF")
    print("-----------------")


    print(" 1. Create account\n 2.Get account info\n 3. Update account info\n 4. Exit\n")
    print("____________________________")
    
    choice = int(input("What do you want to do: "))


    a =[]
    if (choice == 1):
        firstname = (input("What us your first name: "))
        lastname = (input("What us your last name: "))
        dob = int(input("DOB (YYYYMMDD): "))
        gender = int(input("0 for male and 1 for female: "))
        
        a.append(Account(firstname, lastname, dob, gender))
        print(a[0].view_account())

    elif (choice ==2):
        acc = (input("Input your account number"))
        
        for b in a:
            if(b.acc_number == acc):
                print(b)

            else:
                print("Check again")
        
            
        
        
    elif(choice == 4):
        break
    
    count +=1