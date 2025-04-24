import json

Account_link = "C:\\Users\\Yousef\\Desktop\\python\\Ahmed\\bank\\bank.json"

class BankSystem:

    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def Balance(self):
        print(f"The account holder is {self.name}, Your balance is {self.balance}$")

    def Withdraw(self):
        try:
            Q2 = int(input("How much do you want to withdraw? "))
            if Q2 > self.balance:
                print("You don't have enough balance!")
            elif Q2 < 0:
                print("You can't withdraw a negative amount.")
            else:
                self.balance -= Q2
                print(f"You withdrew {Q2}$. Your new balance is {self.balance}$")
                save_accounts()
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    def Deposit(self):
        try:
            Q2 = int(input("How much do you want to deposit? "))
            if Q2 > 0:
                self.balance += Q2
                print(f"You deposited {Q2}$. Your new balance is {self.balance}$")
                save_accounts()
            else:
                print("Deposit amount must be greater than zero.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    def to_dict(self):
        return {
            "name": self.name,
            "balance": self.balance,
            "password": self.password
        }

# ✅ Function outside class to save all accounts
def save_accounts():
    with open(Account_link, "w") as file:
        json.dump([acc.to_dict() for acc in accounts], file, indent=4)

# ✅ Load data
try:
    with open(Account_link, "r") as file:
        content = file.read().strip()
        if content:
            Account_file = json.loads(content)
        else:
            Account_file = []
except (FileNotFoundError, json.JSONDecodeError):
    Account_file = []

accounts = []
for user in Account_file:
    obj = BankSystem(user["name"], user["balance"], user["password"])
    accounts.append(obj)

# ✅ Choose account
for i in range(len(accounts)):
    print(f"{i+1}. {accounts[i].name}")
chosen_index = int(input("Choose your account number: ")) - 1

# ✅ Login system
for i in range(3):
    print("-----------------------------------------")
    try:
        pas = int(input("Enter the pin: "))
    except ValueError:
        print("Invalid input! Pin should be numbers only.")
        continue

    if pas == accounts[chosen_index].password:
        print("Welcome to your bank account")
        break
    else:
        if i == 2:
            print("You reached the maximum tries, goodbye")
            exit()
        else:
            print("Wrong password, try again")
    print("-----------------------------------------\n")

# ✅ Main menu
while True:
    print("\n****************")
    print("      Bank      ")
    print("****************")
    print("1. Show Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    print("****************")

    try:
        Q = int(input("Choose between 1-4: "))

        match Q:
            case 1:
                accounts[chosen_index].Balance()
            case 2:
                accounts[chosen_index].Withdraw()
            case 3:
                accounts[chosen_index].Deposit()
            case 4:
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Try again.")
    except ValueError:
        print("Invalid input! Please enter a number between 1-4.")
