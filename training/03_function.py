#Ejercicio 1: Function, lambda
print("Bienvenido a Cake Shop")

orders_cake_biscuit = []
orders_cake_cream = []
orders_cake_toppings = []

list_biscuit_type = [
  'Vainilla', 
  'Yogurt de fresa',
  'Zanahoria',
  'Chocolate',
  'Red Velvet',
  'Naranja',
  'Limon', 
  'Almendras'
]

list_cream_type = [
  'Fresa',
  'Chocolate negro',
  'Vainilla',
  'Mermelada de cereza',
  'Chocolate blanco'
]

list_toppings_type = [
  'Fresas',
  'Chips',
  'Brownie',
  'Cerezas',
  'Galletas'
]

def cake_biscuit_chose():
  biscuit_type = input("¿Qué tipo de bizcocho desea?: ")
  if biscuit_type in list_biscuit_type:
    orders_cake_biscuit.append(biscuit_type)
  return biscuit_type
  
def cake_cream_chose():
  cream_type = input("¿Qué tipo de crema desea?: ")
  if cream_type in list_cream_type:
    orders_cake_cream.append(cream_type)
  return cream_type

def cake_toppings_chose():
  toppings_type = input("¿Qué tipo de crema desea?: ")
  if toppings_type in list_toppings_type:
    orders_cake_cream.append(toppings_type)
  return toppings_type

def cake_price(biscuit_order, cream_order, toppings_order):
  orders_cake_biscuit_price = [10000,20000,35000,22000,15000,11000,14000,17000]
  orders_cake_cream_price = [1000,2000,3500,2200,1500]
  orders_cake_toppings_price = [700,800,1000,200,500]
  orders_cake_biscuit_discount = list(map(lambda price: price - price * 0.25, orders_cake_biscuit_price))
  orders_cake_toppings_discounted = list(filter(lambda price: price - price * 0.10 if price > 500 else price, orders_cake_toppings_price))
  
  dictionary_biscuit = dict(zip(list_biscuit_type, orders_cake_biscuit_discount))
  dictionary_cream = dict(zip(list_cream_type, orders_cake_cream_price))
  dictionary_toppings = dict(zip(list_toppings_type, orders_cake_toppings_discounted))

  biscuit_price = 0
  cream_price = 0
  toppings_price = 0

  if biscuit_order in dictionary_biscuit:
    biscuit_price = dictionary_biscuit[biscuit_order]
  else:
    print("No tenemos ese bizcocho")

  if cream_order in dictionary_cream:
    cream_price = dictionary_cream[cream_order]
  else:
    print("No tenemos ese tipo de crema")

  if toppings_order in dictionary_toppings:
    toppings_price = dictionary_toppings[toppings_order]
  else:
    print("No tenemos esos toppings")

  total_price = biscuit_price + cream_price + toppings_price
  return total_price
  
def cake_order(biscuit_func, cream_func, toppings_func, price_func):
  biscuit = biscuit_func()
  cream = cream_func()
  toppings = toppings_func()
  print("Usted ordenó un pastel de", biscuit, "con", cream, "y", toppings, "el precio es: ", price_func(biscuit, cream, toppings))

cake_order(cake_biscuit_chose, cake_cream_chose, cake_toppings_chose, cake_price)
