import json
from cryptography.fernet import Fernet

main_file = "Ahmed\\password\\password.json"

try:
    with open("Ahmed\\password\\key.key", "rb") as key_file:
        key = key_file.read()
except FileNotFoundError:
    key = Fernet.generate_key()
    with open("Ahmed\\password\\key.key", "wb") as key_file:
        key_file.write(key)

cipher = Fernet(key)

def ENCRYPT(passkey):
    encrypted = cipher.encrypt(passkey.encode()).decode('utf-8')
    return encrypted  

def DECRYPT(passkey):
    if isinstance(passkey, str):
        passkey = passkey.encode('utf-8')
    decrypted = cipher.decrypt(passkey).decode('utf-8')
    return decrypted

try:
    with open(main_file, "r") as file:
        passwords = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
        passwords = []

class Passwords():
    def __init__(self,account,password,platform,pin):
        self.account=account
        self.password=password
        self.platform=platform
        self.pin=pin

    def add(self):
        self.account = input("Enter username: ")
        self.password = input("Enter password: ")
        self.platform = input("Enter platform: ")
        enc_password = ENCRYPT(self.password)

        passwords.append({"username": self.account, "password": enc_password, "platform": self.platform})

        with open(main_file, "w") as file:
            json.dump(passwords, file, indent=4)

        print("✅ Password saved successfully!")

    def update(self):
        view()
        try:
            pass_num = int(input("\nEnter the account number to update: ")) - 1
            if 0 <= pass_num < len(passwords):
                self.account = input("Enter username: ")
                self.password = input("Enter password: ")
                self.platform = input("Enter platform: ")
                enc_password = ENCRYPT(self.password)

                passwords[pass_num] = {"username": self.account, "password": enc_password, "platform": self.platform}

                with open(main_file, "w") as file:
                    json.dump(passwords, file, indent=4)

                print("✅ Password updated successfully!")
            else:
                print("Invalid account number.")
        except ValueError:
            print("Please enter a valid number.")

    def delete(self):
        view()
        try:
            pass_num = int(input("\nEnter the account number to delete: ")) - 1
            if 0 <= pass_num < len(passwords):
                passwords.pop(pass_num)

                with open(main_file, "w") as file:
                    json.dump(passwords, file, indent=4)

                print("✅ Password removed successfully!")
            else:
                print("Invalid account number.")
        except ValueError:
            print("Please enter a valid number.")

def view():
    for i, entry in enumerate(passwords, start=1):
        print("\n**************")
        print(f"Account number: {i}")
        print(f"Username: {entry['username']}")
        try:
            print(f"Password: {DECRYPT(entry['password'])}")
        except:
            print("Password: [DECRYPTION ERROR]")
        print(f"Platform: {entry['platform']}")
        print("**************")

accounts = []
for user in passwords:
    obj = Passwords(user["username"], user["password"], user["platform"])
    accounts.append(obj)

# Create an object from your class to use methods
pm = Passwords("","","")

for i in range(len(accounts)):
    print(f"{i+1}. {accounts[i].username}")
chosen_index = int(input("Choose your account number: ")) - 1


for i in range(3):
    print("-----------------------------------------")
    pas = input("Enter the master password: ")
    if pas == "2006":
        print("Welcome to the password manager")
        break
    else:
        if i == 2:
            print("You reached the maximum tries, goodbye")
            exit()
        else:
            print("Wrong password, try again")
    print("-----------------------------------------\n")

while True:
    print("\n-----------------------------------------")
    try:
        choice = int(input("What do you want to do? \n1. Add \n2. View \n3. Update \n4. Remove \n5. Quit\n"))
        if choice == 1:
            pm.add()
        elif choice == 2:
            view()
        elif choice == 3:
            pm.update()
        elif choice == 4:
            pm.delete()
        elif choice == 5:
            print("\nGoodbye!")
            exit()
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
    except ValueError:
        print("Please enter a valid number.")
    print("-----------------------------------------\n")
