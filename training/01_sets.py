#Ejercicio 1: Print and fill a set
print("--Ejercicio 1: Print and fill a set--")
list_orders = []
set_full_names_customers = set()
list_orders_mensual = []

for i in range(4):
  print(f"-- Agendamiento de ordenes semana {i + 1}")
  set_full_names_customers = set()
  list_orders = []

  for j in range(7):
    print(f"Orden dia {j + 1}")
    name = input("¿Cuál es su nombre?: ")
    set_full_names_customers.add(name)
    order = input("¿Qué desea ordenar?: ")

    prices = {
        'dish1': 5,
        'dish2': 8,
        'dish3': 12,
        'dish4': 23,
        'dish5': 11,
        'dish6': 16,
        'dish7': 19,
        'dish8': 2,
        'dish9': 4,
        'dish10': 8
    }

    if order in {
      'dish1', 
      'dish2', 
      'dish3', 
      'dish4', 
      'dish5', 
      'dish6', 
      'dish7', 
      'dish8', 
      'dish9', 
      'dish10'
    }:
      print(f"{order} tiene un precio de ${prices[order]}")
      list_orders.append(order)
    else:
      print(f"Lo siento, no tenemos {order} en el menú")

  list_orders_mensual.append(list_orders)
  print(f"Clientes: {set_full_names_customers}")
  print(f"Ordenes semana {i + 1}: {list_orders}")

print(f"Ordenes mensuales: {list_orders_mensual}")

#Ejercicio 2: Methods and operation sets
print("--Ejercicio 2: Methods and operation sets--")

set_full_names_emplooyes = {
  'Lana Ortiz', 
  'Juan Martinez', 
  'Pedro Gomez', 
  'Maria Caballero', 
  'Lina Perez', 
  'Nicolas Diaz'
}

set_ages_emplooyes = {28, 30, 32, 18, 19, 24}

print(f"Lista inicial de empleados:{set_full_names_emplooyes}")
print(f"Edades de empleados: {set_ages_emplooyes}")

set_full_names_emplooyes.add('Carlos')
set_ages_emplooyes.add(22)
set_full_names_emplooyes.add('Susana')
set_ages_emplooyes.add(45)

print(f"Lista con contratandos: {set_full_names_emplooyes}")
print(f"Edades de empleados: {set_ages_emplooyes}")

set_full_names_emplooyes.remove('Lina Perez')
set_ages_emplooyes.remove(19)
set_full_names_emplooyes.remove('Lana Ortiz')
set_ages_emplooyes.remove(28)
set_full_names_emplooyes.remove('Pedro Gomez')
set_ages_emplooyes.remove(32)
set_full_names_emplooyes.remove('Nicolas Diaz')
set_ages_emplooyes.remove(24)

print(f"Lista sin despedidos: {set_full_names_emplooyes}")
print(f"Edades de empleados: {set_ages_emplooyes}")

a = set_full_names_emplooyes.copy()
print(f"Con copy: {a}")

set_full_names_emplooyes.discard('Maria')
print(f"Con discard: {set_full_names_emplooyes}")

b = set_full_names_emplooyes.pop()
print(f"Con pop: {b}")

set_full_names_emplooyes.update(['Hannah', 'Gen'])
print(f"Con update: {set_full_names_emplooyes}")

set_full_names_emplooyes.clear()
print(f"Con clear: {set_full_names_emplooyes}")

names_str_emplooyes = list(set_full_names_emplooyes)  
ages_str_emplooyes = list(set_ages_emplooyes)

#Ejercicio 3: Sets Operation
print("--Ejercicio 3: Sets Operation--")
set_orders_semana_one = set(list_orders_mensual[0])
set_orders_semana_two = set(list_orders_mensual[1])
set_orders_semana_three = set(list_orders_mensual[2])
set_orders_semana_four = set(list_orders_mensual[3])

print("Intersection between S1 y S4:", set_orders_semana_one.intersection(set_orders_semana_four))
print("Exclusive intersection between S2 y S3:", set_orders_semana_two.symmetric_difference(set_orders_semana_three))
print("Union between S1 y S2:", set_orders_semana_one.intersection(set_orders_semana_two))
print("Difference between S2 y S4:", set_orders_semana_two.difference(set_orders_semana_four))
print("Subset between S1 y S2:", set_orders_semana_one.issubset(set_orders_semana_two))
print("Superset between S1 y S2:", set_orders_semana_one.issuperset(set_orders_semana_two))

#Ejercicio 3: List, dict and set
print('Ejercicio 3: List, dict and set')
list_number = [1,2,3,4,5]
list_name_number = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
dict_number = {1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro', 5: 'cinco'}
set_number = {1,2,3,4,5}
set_name_number = {'uno', 'dos', 'tres', 'cuatro', 'cinco'}

print("List", list_number)
print("To dictionary", dict(zip(list_number, list_name_number)), "or", dict(zip(list_number, list_number)))
print("To set", set(list_number))

print("Dict", dict_number)
print("To list", list(dict_number.values()), "or", list(dict_number.keys()), "or", list(dict_number.items()))
print("To set", set(dict_number.values()), "or", set(dict_number.keys()), "or", set(dict_number.items()))

print("Set", set_number)
print("To list", list(set_number))
print("To dict", dict(zip(set_number, set_name_number)), "or", dict(zip(set_number, set_number)))
