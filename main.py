from order_management import create_order, save_orders_to_file, load_orders_from_file


def display_menu():
  print("\nPizza Ordering System")
  print("1. Create a new order")
  print("2. Save orders to file")
  print("3. View existing orders")
  print("4. Exit")


pizza_order_list = []


while True:
  display_menu()
  choice = input("Select an option (1/2/3/4): ")

  if choice == '1':
    new_order = create_order()
    pizza_order_list.append(new_order)
    print("Order created!")

  elif choice == '2':
    save_orders_to_file(pizza_order_list)
    print("rders save to file!")

  elif choice == '3':
    orders = load_orders_from_file()
    print("Existing Orders:")
    for index, order in enumerate(orders, start=1):
      print(
        f"{index}. Costumer: {order.customer_name}, ordered {order.pizza_type}, with toppings {','.join(order.toppings)}"
      )

  elif choice == "4":
    print("Exiting the Pizza Ordering Sysytem.")
    break
  else:
    print("Invalid choice, please select a valid option.")
