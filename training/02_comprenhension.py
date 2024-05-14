#Ejercicio 1: List_comprenhension
name_bank_taxes = ['IVA', 'IBI', 'ISR', 'IAE', 'Agua', 'Local']
value_bank_taxes = [19, 1.1, 10, 2, 7, 8]

dictionary_bank_taxes = dict(zip(name_bank_taxes, value_bank_taxes))

print("Lista de impuestos", dictionary_bank_taxes)

cash_bank_chosen = input("  ¿Cuánto dinero va a aplicar? ")

values_final_to_pay = [float(cash_bank_chosen) + tax/100 * float(cash_bank_chosen) for tax in value_bank_taxes]

for i in range(0,len(name_bank_taxes)):
 print("Para ", name_bank_taxes[i], "el valor es", values_final_to_pay[i])

#Ejercicio 2: List comprenhension
loans_customers_bank = [
  ("Sofia Arjona", 500000000, 24), 
  ("Carolina Marquez", 200000000, 35), 
  ("Juan Cardona", 80000000, 25), 
  ("Luis Rodriguez", 720000000, 32), 
  ("Maria Perez", 150000000, 38), 
  ("Jose Gonzalez", 90000000, 56),
  ("Ana Hernandez", 3000000000, 45),
  ("Rafaela Diaz", 50000000, 70),
  ("Javier Severiche", 600000000, 33),
  ("Sara Arango", 55000000, 54),
]

loans_greater_than_200 = [custom for custom, loan, age in loans_customers_bank if loan > 200000000 and age > 30]

print("Los que tienen préstamos mayores a $200.000.000 y son mayores de 30:")
for i in range(len(loans_greater_than_200)):
  print(loans_greater_than_200[i])

#Ejercicio 3: Dictionary comprenhension
diccionario_loans_customers = {name: loan for name, loan, age in loans_customers_bank}

diccionario_age_customers = {name: age for name, loan, age in loans_customers_bank}

print(diccionario_loans_customers)
print(diccionario_age_customers)





