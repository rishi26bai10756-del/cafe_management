# Campus Cafe - Python Cafe Management System

## Project Information

**Student:** RISHI GIRI GOSWAMI  
**Registration Number:** 26BAI10756  
**Course:** Python Essentials  
**Project:** Campus Cafe - Cafe Management System

## 1. Project Overview

Campus Cafe is a simple command-line cafe management system developed using Python.

The project simulates a real cafe ordering experience. A customer can enter their name, choose between dine-in and takeaway, view the menu, place multiple items in an order, select quantities, and receive a calculated bill.

The program also includes a 10% discount on orders of Rs. 500 or more, 5% GST after the discount, payment method selection, input validation, and a friendly final message.

The main aim is to apply Python programming concepts to a practical, everyday problem.

## 2. Features

- Customer name input
- Dine-in or takeaway selection
- Table number for dine-in orders
- Display of cafe menu and prices
- Multiple item ordering
- Quantity handling
- Validation for invalid menu items
- Validation for invalid quantities
- Automatic subtotal calculation
- 10% discount for subtotal of Rs. 500 or more
- 5% GST calculation after discount
- Final payable amount
- Cash, UPI, or Card payment selection
- Human-friendly messages
- Command-line execution without a GUI
- No external Python libraries required

## 3. Technologies Used

- Python 3
- Dictionaries
- Functions
- Loops
- Conditional statements
- Exception handling
- User input and formatted output
- Basic arithmetic

## 4. Project Structure

```text
campus-cafe/
│
├── cafe_management.py
├── README.md
├── requirements.txt
└── Project_Report.pdf
```

## 5. Requirements

Install Python 3.8 or later.

No third-party packages are needed.

## 6. How to Run

### Step 1 - Install Python

Install Python 3 from the official Python website if it is not already installed.

### Step 2 - Open the project folder

Open Command Prompt, PowerShell, Terminal, or VS Code terminal and move into the project folder.

### Step 3 - Run the program

```bash
python cafe_management.py
```

On some systems, use:

```bash
python3 cafe_management.py
```

### Step 4 - Follow the instructions

The program will ask for:

1. Customer name
2. Dine-in or takeaway
3. Table number if required
4. Food items
5. Quantity
6. Payment method

The final bill will then be displayed in the terminal.

## 7. Example Interaction

```text
==================================================
             WELCOME TO CAMPUS CAFE
==================================================
Hi! May I know your name? Rishi

Nice to meet you, Rishi!
Take your time. I will help you with the order.

Will it be Dine-in or Takeaway? Dine-in
Please enter your table number: 12

                 TODAY'S MENU
---------------------------------------------
Coffee                  Rs. 60
Tea                     Rs. 30
Cold Coffee             Rs. 90
Burger                  Rs. 120
Pizza                   Rs. 160
Sandwich                Rs. 80
French Fries            Rs. 70
Pasta                   Rs. 130
---------------------------------------------

What would you like to order? Burger
How many Burger would you like? 2
Sure! 2 Burger(s) added to your order.

Would you like to add something else? (yes/no): no

==================================================
                 CAMPUS CAFE
                  YOUR BILL
==================================================
Customer : Rishi
Order    : Dine-in
---------------------------------------------
Burger                  x 2    Rs. 240.00
---------------------------------------------
Subtotal                         Rs. 240.00
Discount                         -Rs. 0.00
GST (5%)                         Rs. 12.00
Amount to Pay                    Rs. 252.00
==================================================
```

## 8. Important Notes

- The program is designed for terminal/command-line execution.
- The menu is stored directly in the Python program.
- The project does not require a database or internet connection.
- Prices can be changed by editing the `MENU` dictionary.
- This is an academic project created to demonstrate Python programming concepts.

## 9. Future Improvements

The project can later be expanded by adding:

- Login for cafe staff
- Database storage
- Inventory management
- Daily sales reports
- Order numbers
- Digital receipts
- GUI interface
- Customer order history
- Admin menu management

## 10. Author

**RISHI GIRI GOSWAMI**  
**26BAI10756**  
**Python Essentials**
