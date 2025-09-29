import datetime


orders = []


def add_order():
    print("\n--- New Repair Order ---")
    customer = input("Customer Name: ").strip()
    device = input("Device Type: ").strip()
    issue = input("Issue: ").strip()
    due_date = input("Due Date (YYYY-MM-DD): ").strip()

    try:
        datetime.datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print(" Invalid date format. Please use YYYY-MM-DD.")
        return

    order = {
        "id": len(orders) + 1,
        "customer": customer,
        "device": device,
        "issue": issue,
        "due_date": due_date,
        "status": "Pending"
    }
    orders.append(order)
    print(f" Order {order['id']} added successfully!\n")


def list_orders():
    if not orders:
        print("\n No orders found.\n")
        return

    print("\n--- Repair Orders ---")
    for order in orders:
        print(f"ID: {order['id']} | Customer: {order['customer']} | "
              f"Device: {order['device']} | Issue: {order['issue']} | "
              f"Due: {order['due_date']} | Status: {order['status']}")
    print()


def generate_bill():
    if not orders:
        print("\n No orders to bill.\n")
        return

    try:
        order_id = int(input("Enter Order ID to bill: "))
        order = next((o for o in orders if o["id"] == order_id), None)
        if not order:
            print(" Order not found.")
            return
    except ValueError:
        print(" Invalid input. Enter a numeric Order ID.")
        return

    print("\n--- Billing ---")
    try:
        parts_cost = float(input("Enter total parts cost: "))
        repair_fee = float(input("Enter repair service fee: "))
        discount = float(input("Enter discount (if any, else 0): "))
    except ValueError:
        print(" Invalid amount entered.")
        return

    subtotal = parts_cost + repair_fee
    tax = subtotal * 0.18   # 18% tax
    total = subtotal + tax - discount

    # Update status
    order["status"] = "Completed"

    # Print formatted bill
    print("\n====== INVOICE ======")
    print(f"Customer: {order['customer']}")
    print(f"Device: {order['device']}")
    print(f"Issue: {order['issue']}")
    print(f"Due Date: {order['due_date']}")
    print("------------------------")
    print(f"Parts Cost:      ₹{parts_cost:.2f}")
    print(f"Repair Fee:      ₹{repair_fee:.2f}")
    print(f"Subtotal:        ₹{subtotal:.2f}")
    print(f"Tax (18%):       ₹{tax:.2f}")
    print(f"Discount:       -₹{discount:.2f}")
    print("------------------------")
    print(f"TOTAL:           ₹{total:.2f}")
    print("========================\n")


def menu():
    """Main menu"""
    while True:
        print("==== FixTrack ConsoleApp ====")
        print("1. Add Repair Order")
        print("2. View Orders")
        print("3. Generate Bill")
        print("4. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_order()
        elif choice == "2":
            list_orders()
        elif choice == "3":
            generate_bill()
        elif choice == "4":
            print(" Exiting FixTrack. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.\n")



if __name__ == "__main__":
    menu()
