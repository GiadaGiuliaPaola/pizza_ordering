from datetime import datetime as dt


class PizzaOrder:

  def __init__(self,
               customer_name: str,
               pizza_type: str,
               toppings: list,
               order_time=None,
               is_delivered=False):
    self.customer_name = customer_name
    self.pizza_type = pizza_type
    self.toppings = toppings
    self.order_time = order_time if order_time else dt.now()
    self.is_delivered= is_delivered


def create_order():
  customer_name = input("What's your name? ")
  pizza_type = input("Which pizza would you like? ")
  toppings = input(
    "Which extra toppings would you like to add? Please separate them with a comma. "
  ).split(',')
  return PizzaOrder(customer_name, pizza_type, toppings)


def save_orders_to_file(order_list):
  with open("./orders.txt", "w") as file:
    for order in order_list:
      file.write(f"{order.customer_name}, {order.pizza_type}, {','.join(order.toppings)}, {order.order_time}, {order.is_delivered} \n")
      


def load_orders_from_file():
  orders = []
  with open('./orders.txt', 'r') as file:
    for line in file:
      order_data = line.strip().split(', ')
      if len(order_data) == 5:
        customer_name, pizza_type, toppings, order_time, is_delivered = order_data
        toppings = toppings.split(',')
        order_time = dt.strptime(order_time, '%Y-%m-%d %H:%M:%S.%f')
        is_delivered = is_delivered == 'True'
        order = PizzaOrder(customer_name, pizza_type, toppings, order_time,
                           is_delivered)
        orders.append(order)
      else:
        print(f"Invalid data format in the line: {line.strip()}")
  return orders
