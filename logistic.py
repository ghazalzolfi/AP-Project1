# in this class we will determine post or peyk.
from order import *


class Logistics:
    def __init__(self, city, state, postal_code, address_detail):
        self.peyk_orders = []
        self.post_orders = []
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.address_detail = address_detail

    def assign_delivery(self, cart_object, order_object, card_number):
        if order_object.make_payment(card_number) == 1:
            self.city_ID = Address(
                self.city, self.state, self.postal_code, self.address_detail).id()[0]
            self.state_ID = Address(
                self.city, self.state, self.postal_code, self.address_detail).id()[1]
            delivery_method = ""
            if self.state_ID == 1:
                self.peyk_orders.append(cart_object.cart)
                delivery_method = "Peyk"
                print(f"Your order will be delivered by {delivery_method}.")
            else:
                self.post_orders.append(cart_object.cart)
                delivery_method = "Post"
                print(f"Your order will be delivered by {delivery_method}.")
            return delivery_method
        # else:
        #     print("The payment was unsuccessful. Try Again.")


class Address(Logistics):
    def __init__(self, city, state, postal_code, address_detail):
        super().__init__(city, state, postal_code, address_detail)
        self.state_ID = None
        self.city_ID = None

    def id(self):
        if self.state == "tehran" and self.city == 'parand':
            self.state_ID = 1
            self.city_ID = 1
        elif self.state == "tehran" and self.city == 'tehran':
            self.state_ID = 1
            self.city_ID = 2
        elif self.state == "esfahan" and self.city == 'kashan':
            self.state_ID = 2
            self.city_ID = 1
        elif self.state == "esfahan" and self.city == 'khomain':
            self.state_ID = 2
            self.city_ID = 2
        elif self.state == "tabriz" and self.city == 'kosroshahr':
            self.state_ID = 3
            self.city = 1
        elif self.state == "tabriz" and self.city == 'sardorod':
            self.state_ID = 3
            self.city = 2
        return [self.city_ID, self.state_ID]

    def price(self):
        if self.state_ID == 1:
            self.price = 30
        else:
            self.price = 50
        return self.price


time_chart = pd.read_csv("available times.csv")


class Time:
    def __init__(self, delivery_time, order_object, card_number):
        if order_object.make_payment(card_number) == 1:
            self.time = delivery_time
            if self.time != 'morning':
                if self.time == "noon":

                    if time_chart.iloc[0, 0] > 0:
                        time_chart.iloc[0, 0] = time_chart.iloc[0, 0] - 1
                    else:
                        print('this time is not available')
                        self.time = input('please enter another time:')
                        if self.time != 'morning':

                            if time_chart.iloc[0, 1] > 0:
                                time_chart.iloc[0,
                                                1] = time_chart.iloc[0, 1] - 1
                            else:
                                print('the only time that is available is morning')
                                self.time = 'morning'
                elif self.time == "afternoon":
                    if time_chart.iloc[0, 1] > 0:
                        time_chart.iloc[0, 1] = time_chart.iloc[1, 1] - 1
                    else:
                        print('this time is not available')
                        self.time = input('please enter another time:')
                        if self.time != 'morning':

                            if time_chart.iloc[0, 0] > 0:
                                time_chart.iloc[0,
                                                0] = time_chart.iloc[0, 0] - 1
                            else:
                                print('the only time that is available is morning')
                                self.time = 'morning'
        else:
            self.time = 0

    def Delivery_time(self):
        if self.time != 0:
            print(f"Your Order will be delivered at {self.time}.")
            time_chart.to_csv("available times.csv", index=False)

# print(time_chart)
