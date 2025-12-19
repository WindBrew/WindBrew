lockcount = 3
upin=4321
bal=10000
while True:
    if not lockcount == 0 :
        print("-------Welcome to somewhat Bank ATM-------")
        print("1.Check Balance\n2.Withdraw Amount\n3.Deposit Amount\n4.Change pin\n5.Exit\n")
        choice = int(input("Enter your choice: "))
        if not choice <1 or choice >5 :
            if choice == 1:
                 pin = int(input("Enter your pin: "))
                 if pin == upin :
                     print("Balance : ", bal)
                 else:
                     print("Incorrect pin")
                     print("")
                     print("You have",lockcount,"tries left")
                     lockcount-=1
            elif choice == 2:
                 pin = int(input("Enter your pin: "))
                 if pin == upin :
                     damt=int(input("Enter your deposit amount : "))
                     if damt > 0 :
                         bal += damt
                         print("Current Balance : ", bal)
                     else:
                         print("Deposit amount cannot be negative")
                 else:
                     print("Incorrect pin")
                     print("")
                     print("You have",lockcount,"tries left")
                     lockcount-=1
            elif choice == 3:
                 pin = int(input("Enter your pin: "))
                 if pin == upin :
                     wamt=int(input("Enter your withdrawl amount : "))
                     if not wamt > bal :
                         bal -= wamt
                         print("Current Balance : ", bal)
                     else:
                         print("Withdrawl amount cannot be greater than available balance")
                 else:
                     print("Incorrect pin")
                     print("You have",lockcount,"tries left")
                     print("")
                     lockcount-=1
            elif choice == 4:
                     pin = int(input("Enter your previous pin: "))
                     if pin == upin :
                         upin = int(input("Enter your new pin: "))
                     else:
                         print("Incorrect pin")
                         print("")
                         print("You have",lockcount,"tries left")
                         lockcount-=1
            elif choice == 5:
                     print("Thank you for visiting somewhat bank ATM, Have a good day!")
                     break
        else:
            print("Invalid choice")
    else:
        print("Your account has been locked for 24 hours")
        break
