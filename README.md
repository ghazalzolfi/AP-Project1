E-commerce System with Command-Line Interface (CLI)

This project involves building a simplified e-commerce system with multiple modules, implemented through a command-line interface. The system consists of several key components:

1. Customer Module:
   - Allows customers to browse available products, view details, add them to a shopping cart, and proceed with the checkout process.
   - After placing an order, customers can provide shipping details and complete the payment via a mock payment gateway.
   - Orders are assigned unique order IDs, and successful transactions generate a receipt saved as a text file.

2. Inventory Manager Module:
   - Handles the updating and management of product stock in the store.
   - Allows adding new products and updating existing stock via manual entry or by importing CSV files.
   - The system ensures product availability is updated after each purchase, and out-of-stock products are labeled as unavailable.

3. Accounting Module:
   - Tracks all placed orders and generates financial reports for the store.
   - Maintains records of orders, quantities, and total amounts, which can be exported as CSV files for analysis.

4. Logistics Module:
   - Manages the shipping of orders, ensuring correct customer addresses and timely delivery.
   - Orders are assigned to one of three delivery windows (morning, noon, afternoon), and unavailable windows are hidden from the customer's options.

The project focuses on simulating an end-to-end e-commerce experience with features such as order management, stock updates, payment validation, and delivery scheduling, all implemented in Python with a focus on modularity and command-line interaction.
