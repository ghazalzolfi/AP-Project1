from order import *
from logistic import *
import csv

class Banking(Payment_data):

    def __init__(self, name, phone_number, address):
        super().__init__(name, phone_number, address)

    def cheking_card(self, card_number, cart_object, address, order_object):
        super().make_payment(card_number)
        total_quantity = 0
        if order_object.make_payment(card_number) == 1:
          for i in cart_object.cart.values():
                    for j in i.values():
                         total_quantity += j
          with open("orders.csv", "a") as file:
                    self.writer = csv.writer(file)
                    self.writer.writerow([total_quantity, self.order_ID, cart_object.pure_price,
                                   address.price(), cart_object.pure_price * 0.09])

    



class Output:
    def output(self):
        print(pd.read_csv("orders.csv"))