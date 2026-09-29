import time

# --- CAFE SETUP ---
menu = {
    "Coffee": 60,
    "Tea": 30,
    "Cold Coffee": 90,
    "Burger": 120,
    "Pizza": 160,
    "Sandwich": 80,
    "French Fries": 70,
    "Pasta": 130
}

# --- WELCOME ---
print("=" * 45)
print("      ☕ WELCOME TO THE CAMPUS CAFE ☕")
print("=" * 45)

name = input("Hey there! What name can I put down for your order? ").strip().title()
if not name:
    name = "Friend"

print(f"\nAwesome to meet you, {name}! Make yourself at home.")

service = input("\nAre you hanging out here today or grabbing it to go? (Dine-in / Takeaway): ").strip().title()
if service not in ["Dine-In", "Dine In", "Takeaway", "To Go"]:
    service = "Dine-in"
    print("No worries, we'll get a table ready for you!")
else:
    if "Takeaway" in service or "Go" in service:
        service = "Takeaway"
    else:
        service = "Dine-in"

# --- MENU DISPLAY ---
print("\n" + "-" * 45)
print("             TODAY'S SPECIAL MENU")
print("-" * 45)

for item, price in menu.items():
    print(f"  • {item:<22} Rs. {price}")

print("-" * 45)
print("💡 Tip: If you're on the fence, our Cold Coffee and Burgers are absolute favorites!")

# --- ORDERING SYSTEM ---
order = {}
total = 0

while True:
    item_input = input("\nWhat sounds good to you? (Type 'Done' when finished): ").strip().title()

    if item_input == "Done":
        if not order:
            print("Oh, changed your mind? No rush at all—take your time looking!")
            continue
        print("\nGot it! Let me wrap up your ticket...")
        break

    if item_input not in menu:
        print("Hmm, we don't have that on the menu today. Want to try something else?")
        continue

    try:
        qty_input = input(f"How many {item_input}s can I get for you? ")
        quantity = int(qty_input)

        if quantity <= 0:
            print("Haha, you need at least 1! How many would you like?")
            continue

        item_cost = menu[item_input] * quantity
        order[item_input] = order.get(item_input, 0) + quantity
        total += item_cost

        print(f"Added {quantity} {item_input}(s) to your tray!")
        print(f"Running total: Rs. {total}")

        again = input("Anything else to go with that? (Yes / No): ").strip().lower()
        if again in ["no", "n", "nope", "that's all", "thats all"]:
            break

    except ValueError:
        print("Whoops! Just type a number (like 1, 2, or 3). Let's try that item again.")

# --- RECEIPT & PAYMENT ---
print("\n" + "=" * 45)
print("              YOUR CAFE RECEIPT")
print("=" * 45)
print(f" Guest:      {name}")
print(f" Order Type: {service}")
print("-" * 45)

if order:
    for item, quantity in order.items():
        cost = menu[item] * quantity
        print(f" {item:<20} x{quantity:<2}   Rs. {cost}")

    discount = total * 0.10 if total >= 500 else 0
    final_amount = total - discount

    print("-" * 45)
    print(f" Subtotal:             Rs. {total:.2f}")
    if discount > 0:
        print(f" Special Discount (10%): -Rs. {discount:.2f}")
        print(" ✨ You unlocked our 10% discount on orders over Rs. 500!")
    
    print(f" Total Due:            Rs. {final_amount:.2f}")
    print("-" * 45)

    payment = input("\nHow would you like to settle up? (Cash / UPI / Card): ").strip().title()
    if payment not in ["Cash", "Upi", "Card"]:
        payment = "Cash"
        print("We'll put that down as Cash then.")

    print(f"\nAll set! Payment received via {payment}.")
    print("Firing up the kitchen now...")

    time.sleep(1.5)

    print(f"\nThanks for hanging out with us today, {name}!")
    print("Enjoy your meal, and have an awesome rest of your day!")

else:
    print("No items ordered. Hope to see you next time!")

print("=" * 45)
print("      SEE YOU AGAIN AT CAMPUS CAFE!")
print("=" * 45)