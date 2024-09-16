import pandas as pd
from order import *
from wearhouse import *
from banking import *
from logistic import *


wearhouse_object = Update("main wearhouse.csv")
bank_output = Output()

if __name__ == '__main__':
    class Start(Update):

        def start(self):
            print("Account mode: \n 1.customer \n 2.seller")
            acount_mode = int(input("Enter your choice: "))

            if acount_mode == 1:
                while True:
                    print("Customer Mode Menu:")
                    print("1.show available products")
                    print("2.show your cart")
                    print("3.payment")
                    print("0.exit store")
                    customer_menu = int(input("Enter your choice: "))
                    if customer_menu == 1:
                        cart_object = Cart()
                        print(pd.read_csv("main wearhouse.csv"))
                        status = "Continue"
                        while status != "finish":
                            product_name = input("Enter product name: ").lower()
                            size = input("Enter product's size: ").lower()
                            quantity = int(input("Enter product's quantity: "))
                            cart_object.add_to_cart(
                                database, product_name, size, quantity)
                            status = input("Continue / Finish? ").lower()
                    elif customer_menu == 2:
                        try:
                            print(cart_object.cart)
                        except:
                            print("Your cart is empty!")
                    elif customer_menu == 3:
                        try:
                            len(cart_object.cart)
                        except:
                            print("Your cart is empty!")
                        else:
                            name = input("Enter your name: ")
                            phone_number = input("Enter your phone number: ")
                            while len(phone_number) != 10:
                                print("The number should be 10 digits, please try again.")
                                phone_number = input("Enter your phone number: ")
                            address = input("Enter your address: ")
                            delivery_time = input("Enter your delivery_time: ")
                            order_object = Payment_data(
                                name, phone_number, address)
                            card_number = input("Enter your card number: ")
                            city = input("Enter your city: ").lower()
                            state = input("Enter your state: ").lower()
                            postal_code = input("Enter your postal code: ")
                            while len(postal_code) != 10:
                                print("The number should be 10 digits, please try again.")
                                postal_code = input("Enter your postal code: ")
                            address_detail = input(
                                "Enter your address detail: ")
                            logistics_object = Logistics(
                                city, state, postal_code, address_detail)
                            address = Address(
                                city, state, postal_code, address_detail)
                            order_object.make_payment(card_number)

                            wearhouse_object.auto_update(cart_object, order_object, card_number)
                            bank_obj = Banking(name, phone_number, address)
                            bank_obj.cheking_card(
                                card_number, cart_object, address, order_object)
                            delivery_method = logistics_object.assign_delivery(
                                cart_object, order_object, card_number)
                            factor_object = Factor(order_object, cart_object, delivery_time)
                            Time(delivery_time, order_object, card_number).Delivery_time()
                            factor_object.create_factor(delivery_method)
                    elif customer_menu == 0:
                        break
                    else:
                        print("Invalid choice! Try again...")

            elif acount_mode == 2:
                while True:
                    print("Seller Mode Menu:")
                    print("1.Wearhouse")
                    print("2.Banking")
                    print("0.Exit seller mode")
                    seller_menu = int(input("Enter your choice: "))
                    if seller_menu == 1:
                        print('we have 2 options to update wear house: ')
                        print('1:giving file')
                        print('2:giving informations')
                        seller_choice = int(input('Enter your choice:'))

                        if seller_choice == 1:
                            update_wearhouse = input('give your file path:')
                            wearhouse_object.update_with_file(update_wearhouse)
                            # return Manual_Update.update_stock_from_csv()
                            wearhouse_object.save_stock()
                        elif seller_choice == 2:
                            wearhouse_object.update_with_terminal()
                            # return Manual_Update.update_stock_from_terminal()
                            wearhouse_object.save_stock()
                        else:
                            print("Invalid choice! Try again...")
                    elif seller_menu == 2:
                        bank_output.output()
                    elif seller_menu == 0:
                        break
                    else:
                        print("Invalid choice! Try again...")
            else:
                print("Invalid choice!")


start = Start("main wearhouse.csv")
start.start()
