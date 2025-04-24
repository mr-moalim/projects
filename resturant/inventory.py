import json
class Shop:
    def __init__(self,name):
        self.name=name
        self.product=[]
        self.customer=[]
        self.sales=[]
        self.load()


    def add_product(self):
        pn=str(input("Enter the name of the product: "))
        pp=float(input("Enter the price of the product: "))
        sp=int(input("Enter the number of the items: "))
        ip=str(input("Enter the id of the product: "))
        new_product = Product(pn,pp,sp,ip)
        self.product.append(new_product)
        self.save()




    def add_customer(self):
        nc = str(input("Enter the name of the customer: "))
        ic = str(input("Enter the id of the customer: "))
        new_customer = Customer(nc,ic)
        self.customer.append(new_customer)
        self.save()

    def make_sale(self):
        customer_id = str(input("Enter the ID of the customer: "))
        product_id = str(input("Enter the ID of the product: "))
        quantity = int(input("Enter the quantity of the product: "))

        # Find the customer
        customer = None
        for c in self.customer:
            if str(c.id) == customer_id:
                customer = c
                break

        if customer is None:
            print("❌ Customer not found.")
            return

        # Find the product
        product = None
        for p in self.product:
            if p.id == product_id:
                product = p
                break

        if product is None:
            print("❌ Product not found.")
            return

        if product.stock < quantity:
            print("❌ Not enough stock.")
            return

        # Reduce product stock
        product.stock -= quantity

        # Calculate total price
        total_price = product.price * quantity

        # Record the sale
        sale_record = {
            "customer": customer.name,
            "product": product.name,
            "quantity": quantity,
            "total": total_price
        }
        self.sales.append(sale_record)

        customer.add_purchase(product.name, quantity, total_price)

        print("✅ Sale completed successfully.")
        self.save()


    def view_inventory(self):
        for product in self.product:
            print(f"product: {product.name}")
            print(f"price: {product.price}")
            print(f"stock: {product.stock}")
            print(f"id: {product.id}")
            print()


    def view_customers(self):
        for customer in self.customer:
            print(f"customer: {customer.name}")
            print(f"id: {customer.id}")
            print()


    def view_sales(self):
        for sales in self.sales:
            print(f"customer: {sales.customer}")
            print(f"product: {sales.product}")
            print(f"quantity: {sales.quantity}")
            print(f"total: {sales.total}")
            print()


    def save(self):
        customers_data= [{"name":c.name,"id":c.id}for c in self.customer]
        products_data= [{"name":p.name,"price":p.price,"stock":p.stock,"id":p.id}for p in self.product]
        all_info = \
            {"customer": customers_data,
             "product": products_data,
             "sales": self.sales}

        with open("info.json", "w") as file:
            json.dump(all_info,file,indent=4)

    def load(self):
        try:
            with open("info.json", "r") as f:
                data = json.load(f)

                self.customer = []
                for p in data.get("customer", []):
                    customer = Customer(p["name"], p["id"])
                    self.customer.append(customer)

                self.product = []
                for d in data.get("product", []):
                    product = Product(d["name"], d["price"], d["stock"], d["id"])
                    self.product.append(product)

                self.sales = data.get("sales", [])

                print("✅ Data loaded successfully!")

        except FileNotFoundError:
            print("⚠️ File not found. Starting with empty data.")
        except json.JSONDecodeError:
            print("❌ Failed to load JSON data. File might be corrupted.")

class Customer:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.purchase_history = []

    def add_purchase(self, product_name: str, quantity: int, total: float):
        purchase = {
            "product": product_name,
            "quantity": quantity,
            "total": total
        }
        self.purchase_history.append(purchase)

    def view_history(self):
        if not self.purchase_history:
            print(f"{self.name} has no purchase history.")
        else:
            print(f"Purchase history for {self.name}:")
            for purchase in self.purchase_history:
                print(f"- {purchase['quantity']}x {purchase['product']} = ${purchase['total']}")



class Product :
    def __init__(self,name: str, price: float, stock: int, id: str):
        self.name = name
        self.price = price
        self.stock = stock
        self.id = id

    def update_price(self,new_price: float):
        self.price = new_price

    def update_stock(self,amount: int):
        self.stock = amount

    def show_info(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.stock}")
        print(f"Id: {self.id}")




shop = Shop("My Shop")
shop.load()

while True:
    print("\n--- Shop Menu ---")
    print("1. Add Product")
    print("2. Add Customer")
    print("3. Make Sale")
    print("4. View Inventory")
    print("5. View Customers")
    print("6. View Sales")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        shop.add_product()
    elif choice == "2":
        shop.add_customer()
    elif choice == "3":
        shop.make_sale()
    elif choice == "4":
        shop.view_inventory()
    elif choice == "5":
        shop.view_customers()
    elif choice == "6":
        for sale in shop.sales:
            print(f"{sale['customer']} bought {sale['quantity']}x {sale['product']} - Total: ${sale['total']}")
    elif choice == "7":
        shop.save()  # Auto-save before exiting
        print("✅ Data saved. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
