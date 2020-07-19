import json
from urllib.request import urlopen

# with urlopen("https://jsonplaceholder.typicode.com/users?format=json") as response:
#      source = response.read()
#
# # print(source)
# data = json.loads(source)
# # print (json.dumps(data, indent=2))
# # print (len(data))
#
# user = dict()
# for item in data:
#     myname = item['name']
#     myaddr = item['address']
#     user[myname] = myaddr
#
# print (user['Leanne Graham'])

#https://towardsdatascience.com/the-alternative-to-web-scraping-8d530ae705ca
# import requests
#
# r = requests.get("https://query2.finance.yahoo.com/v10/finance/quoteSummary/FB?modules=price")
# data = r.json()
# print(json.dumps(data, indent =2))
# print(f"the current price: {data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']}")

