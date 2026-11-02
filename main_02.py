wallets = {
    "Ali": 500000,
    "Sara": 1200000,
    "Reza": 300000,
    "Mina": 800000
}
while True:
    print("1 -> Show all users and wallet balances")
    print("2 -> Search user balance")
    print("3 -> Add new user")
    print("4 -> Deposit money")
    print("5 -> Withdraw money")
    print("6 -> Transfer money")
    print("7 -> Delete user")
    print("8 -> Count all users")
    print("9 -> Calculate total wallet balance")
    print("10 -> Find user with highest balance")
    print("11 -> Show final wallet information")
    print("12 -> Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        for name, balance in wallets.items():
            print(f"{name} -> {balance}")
    elif choice == 2:
        name = input("Enter user name: ")
        if name in wallets:
            print("Wallet Balance: ", wallets[name])
        else:
            print("Wallet does not exist")
    elif choice == 3:
        new_name = input("Enter new name: ")
        if new_name in wallets:
            print("User already exists")
        else:
            new_balance = int(input("Enter new balance: "))
            wallets[new_name] = new_balance
            print("Success!")
            print(wallets)
    elif choice == 4:
        name = input("Enter user name: ")
        if name in wallets:
            new_balance = int(input("Enter new balance: "))
            wallets[name] += new_balance
            print("Success!")
            print(wallets)
        else:
            print("User not found")
    elif choice == 5:
        name = input("Enter user name: ")
        if name in wallets:
            withdraw_money = int(input("Enter withdraw money: "))
            if withdraw_money <= 0:
                print("Invalid money")
            elif withdraw_money <= wallets[name]:
                wallets[name] -= withdraw_money
                wallets[name] -= withdraw_money
                print("Success!")
                print(wallets)
            else:
                print("Insufficient balance")
        else:
            print("User not found")
    elif choice == 6:
        sender_name = input("Enter sender name: ")
        receiver_name = input("Enter receiver name: ")
        if sender_name in wallets and receiver_name in wallets:
            if sender_name == receiver_name:
                print("cannot transfer money")
            else:
                amount = int(input("Enter amount: "))
                if amount <= 0:
                    print("Invalid amount")
                elif amount > wallets[sender_name]:
                    print("Insufficient money")
                else:
                    wallets[sender_name] -= amount
                    wallets[receiver_name] += amount
                    print("Success!")
                    print(wallets)
        else:
            print("User not found")

    elif choice == 7:
        name = input("Enter user name: ")
        if name in wallets:
            wallets.pop(name)
            print("Success!")
            print(wallets)
        else:
            print("User not found")
    elif choice == 8:
        count = len(wallets)
        print(f"Total users:{count}")
    elif choice == 9:
        total_balance = 0
        for balance in wallets.values():
            total_balance += balance
        print(f"Total wallet balance:{total_balance}")

    elif choice == 10:
        max_balance = max(wallets, key=wallets.get)
        print(f"max balance:{max_balance}")

    elif choice == 11:
        for name, balance in wallets.items():
            print(f"{name} -> {balance}")
    elif choice == 12:
        print("Exit")
        break
    else:
        print("Invalid choice")


