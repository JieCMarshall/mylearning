import json
from urllib.request import urlopen

with urlopen("https://jsonplaceholder.typicode.com/users?format=json") as response:
     source = response.read()

# print(source)
data = json.loads(source)
# print (json.dumps(data, indent=2))
# print (len(data))

user = dict()
for item in data:
    myname = item['name']
    myaddr = item['address']
    user[myname] = myaddr

print (user['Leanne Graham'])

