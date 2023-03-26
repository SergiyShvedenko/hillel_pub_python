
import json
import csv
import random

with open('hw_17.json') as file:
  new_data = json.load(file)

keys = list(new_data.keys())
name_of_fields = ["ID", "Имя", "Возраст", "Телефон"]
counter = 0

with open('hw_18.csv', 'w', encoding='utf-8') as file:
  file_writer = csv.writer(file)
  file_writer.writerow(name_of_fields)
  for i in new_data.items():
    random_number = str(random.randint(1000000, 9000000))
    operators = ['095', '066', '098', '096', '050', '097']
    phone_number = random.choice(operators) + random_number
    field_x = keys[counter], new_data[keys[counter]][0], new_data[keys[counter]][1], phone_number
    counter = counter + 1
    file_writer.writerow(field_x)
