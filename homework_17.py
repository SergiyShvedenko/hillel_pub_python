
import json

data = {111111: ('Adam', 23), 222222: ('Bob', 34), 333333: ('Carter', 45),
        444444: ('Daniel', 56), 555555: ('Ethan', 67), 666666: ('Finn', 78)}

with open('hw_17.json', 'w') as file:
  json.dump(data, file)
