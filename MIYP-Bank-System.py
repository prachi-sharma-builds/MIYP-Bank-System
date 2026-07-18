from random import randint
from datetime import datetime
import time



print("---------------------MIYP Bank-----------------------")
print("---------------Money In Your Pocket---------------")
print("---------------Small Bank, Big Trust--------------")
print(" ")

class Bank:
    def __init__(self, owner, password, balance):
        self._owner = owner
        self._password = password
        self.balance = balance
        
    # Owner name getter
    @property
    def owner(self):
        return self._owner
    
    # Owner passwaord
    @owner.setter
    def owner(self, new_owner):
        if isinstance(new_owner, str) and new_owner.strip(" "):
            self._owner = new_owner
        else:
            print("The username is incorrect!")
    
    # owner password getter
    @property
    def password(self):
        return self._password
    
    # owner password setter
    @password.setter
    def password(self, new_password):
        if isinstance(new_password, str) and new_password.isalpha():
            self._password = new_password
        else:
            print("The password is incorrect!")
            
    # owner balance getter
    @property
    def balance(self):
        return self._balance
    
    # owner balance setter
    @balance.setter
    def balance(self, new_balance):               
        if new_balance > 0:
            self._balance = new_balance
        else:
            print("Enter the correct balance!")
            
    # Deposit
    def deposit(self, amount):
        if self._balance >= amount:
            self._balance += amount
            print(f"Rs.{amount} Deposited.")
        elif amount > 0:
            self._balance += amount
            print(f"Rs.{amount} Deposited.")
        else:
            print("Enter the correct amount.")
            
    # Withdrawal 
    def withdraw(self, amount):
        if amount <= self._balance and amount > 0:
             self._balance -= amount
             print(f"Rs.{amount} Withdrawn.")
        else:
            print("Insufficient balance")
             
    # Display
    def displayAmount(self):
        print("--------Financial Record--------")
        print(" ")
        print(f"Owner Name: {self._owner}")
        print(f"Total Balance: {self._balance}")
        
            
        
print("Create Account")
print(" ")
userName = input("Enter owner's username: ")
userPass = input("Create your password. It must contain letters: ")
userPass = userPass.lower()
iniBalance = int(input("Enter tnitial balance: ")) # Initial Balance
print(" ")
print(" ")
    
    
acc = Bank(userName, userPass, iniBalance)


print(" ")
print("Login Into Your Account")
print(" ")

while True:
        print("Password verificaiton")
        verifyPass = input("Verify your password: ")
        if verifyPass == acc.password:
            print("Your password is successfully verified.")
            print(" ")
            break
        else:
            print("Wrong password. Try again!")
            print(" ")
            print(" ")
            
print("OTP Verificaiton")
print(" ")
otp = randint(1000,9999)
time.sleep(2)
print("Please wait for the OTP...")
time.sleep(4)
print(f"Your OTP is: {otp} . Dont't share it with anybody. ")
verifyOTP = int(input("Enter 4 digit OTP:  "))
print(" ")

if verifyOTP == otp:
    print("You are successfully verified!")
    print(" ")
    now = datetime.now()
    current_hour = now.hour
    
    if 5 <= current_hour < 12:
        greeting = "Good Morning"                   
    
    elif 12 <= current_hour < 17:
        greeting = "Good Afternoon"
        
    elif 17 <= current_hour < 21:
        greeting = "Good Evening"
        
    else:
        greeting = "Good Night"
        
    print(f"{greeting} {acc.owner}!")
    print(f"Login Time: {now.strftime('%I:%M %p')}")
    print(f"Login Date: {now.strftime('%d %B %Y')}")
    
    while True:
        print(" ")
        print(" ")
        print("------DASHBOARD------")
        
        
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change Password")
        print("5. View account Details")
        print("6. Logout")
        
        choice = int(input("Choose an option between 1-6: "))
        
        if choice == 1:
            print(f"Your current balance: Rs.{acc.balance}")
            
        elif choice == 2:
            rupees = int(input("Enter the amount to deposit: "))
            acc.deposit(rupees)
            
        elif choice == 3:
            rupees = int(input("Enter the amount to withdraw: "))
            acc.withdraw(rupees)
            
        elif choice == 4:
            attempts = 3
            while attempts > 0:
                old_password = input("Enter current password: ")

                if old_password == acc.password:
                    new_password = input("Enter new password: ")
                    acc.password = new_password
                    print(f"Password updated successfully.")
                    break
                    
                else:
                    print("Wrong password. Try again. 3 attempts allowed.")
                    attempts = attempts - 1
                    print(f"You have {attempts} attempt(s) left.")
                    
                    
            if attempts == 0:
                print("You have exceeded the maximum attempts. Please try again later.") 
                
        elif choice == 5:
            print("---------Account Details----------")
            print(f"Owner Name: {acc.owner}")
            print(f"Bank Name: MIYP Bank")
            print(f"Current Balance: {acc.balance}")
            print(f"Login Time: {now.strftime('%I:%M %p')}")
            print(f"Login Date: {now.strftime('%d %B %Y')}")
            
            
        elif choice == 6:
            print("You have been logout from your account.")
            break
        
        else:
            print("You have entered the wrong choice. Please enter correctly.")
            print(" ")
            print(" ")
            
        