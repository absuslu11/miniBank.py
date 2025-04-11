import time

total = 0

def show_balance():
    global total
    print("*************")
    print(f" your balance is ${total: .2f}")
    print("*************")

def deposit():
    global total
    print("*************")
    amount = float(input("Enter an amount to be deposited:"))
    print("*************")
    total += amount
    time.sleep(3)
    print (f"your deposit of {amount: .2f} was deposited into your account")



def withdraw():
    global total
    print("*************")
    negative = int(input("Enter how much you would like to withdraw: "))
    print("*************")
    if negative > total:
        print("insufficient funds")
    else:
        total -= negative
        time.sleep(2)
        print (f"your withdrawl of {negative: .2f} was withdrawed from your account")


cont = True


while cont:
    print("*************")
    print("Banking program")
    print("*************")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("*************")
    
    choice = int(input("Enter Your Choice (1-4): "))

    def play(choice):
        match choice:
            case 1:
                print(show_balance())
            case 2:
                print(deposit())
            case 3:
                withdraw()
            case 4:
                cont = False
            case _:
                print("not a valid Choice")

    print(play(choice))
    