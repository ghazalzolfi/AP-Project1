import random as rand
import pandas as pd
from logistic import Time

database = pd.read_csv("main wearhouse.csv")


class Cart:
    def __init__(self):
        self.cart = {}
        self.pure_price = 0

    def add_to_cart(self, database, product_name, size, quantity):
        if product_name in list(database["stock_name"]):
            if size in list(database[database["stock_name"] == product_name]["size"]):
                if quantity <= (list(database[(database["stock_name"] == product_name) & (
                        database["size"] == size)]['current_stock'])[0]):
                    if product_name in self.cart.keys():
                        if size in self.cart[product_name]:
                            if quantity <= (list(database[(database["stock_name"] == product_name) & (
                                    database["size"] == size)]['current_stock'])[0]) - self.cart[product_name][size]:
                                self.cart[product_name][size] += quantity
                                self.pure_price += (list(database[(database["stock_name"] == product_name) & (
                                        database["size"] == size)]['price'])[0]) * quantity
                            else:
                                print(
                                    f"{quantity + self.cart[product_name][size]} number of {product_name} in size {size} is not available!")
                        else:
                            self.cart[product_name][size] = quantity
                            self.pure_price += (list(database[(database["stock_name"] == product_name) & (
                                    database["size"] == size)]['price'])[0]) * quantity
                    else:
                        self.cart[product_name] = {size: quantity}
                        self.pure_price += (list(database[(database["stock_name"] == product_name) & (
                                database["size"] == size)]['price'])[0]) * quantity
                else:
                    print(f"{quantity} number of {product_name} in size {size} is not available!")
            else:
                print(f"{product_name} in size {size} is not available!")
        else:
            print(f"{product_name} is not available!")
    


class Payment_data:
    def __init__(self, name, phone_number, address):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.order_ID = rand.randint((10**10), (10**11-1))
        self.payment_status = 1

    
    def make_payment(self, card_number):
        if len(str(card_number)) == 16:
            self.payment_status = 1
            result = "Payment was successful!"
            with open("payment_confirmation.txt", "w") as file:
                file.write(result)
        else:
            self.payment_status = 0
            result = "Payment was unsuccessful!"
            with open("payment_confirmation.txt", "w") as file:
                file.write(result)
        return self.payment_status

# print(Payment_data("name", "0123456789", "f").make_payment("0123456789123456"))
class Factor:
    def __init__(self, payment_data: Payment_data, cart: Cart, time):
        self.payment_data = payment_data
        self.cart = cart
        self.time = time
        

    # def Delivery_time(self, delivery_time, card_number):
    #     delivery_time = Time(delivery_time, self.payment_data, card_number).tell_time()
    #     self.time = delivery_time
    #     print(f"Your Order will be delivered at {self.time}.")
    
    def create_factor(self, delivery_method):
        product_price = {}
        for name in self.cart.cart.keys():
            for i in self.cart.cart[name].keys():
                size = i
                price = 0
                for j in self.cart.cart[name].values():
                    quantity = j
                    price += quantity * int(list(database[(database["stock_name"] == name) & (
                            database["size"] == size)]['price'])[0])
                    product_price[name] = price
        with open("fact.txt", "w") as file:
            file.write(f"{product_price}\n")
            file.write(f"Order ID: {self.payment_data.order_ID}\n")
            file.write(f"Address: {self.payment_data.address}\n")
            file.write(f"Name: {self.payment_data.name}\n")
            file.write(f"Delivery time: {self.time}\n")
            file.write(f"Delivery type: {delivery_method}\n")
        return file
