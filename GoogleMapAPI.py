import json
import requests

#Google MAP API call
# params = {
# 'key': 'AIzaSyAE-tQ0-K_j78fDO-IFXHXbKso35013mcc',
# 'origins': '4810 Viro Rd, La Canada, CA, USA',
# 'destinations': '1941 Lombardy, La Canada, CA, USA'
# }
# url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
# response = requests.get(url,params)
# print(response.status_code == 200)
#
#
# print(response.text)
# result = json.loads(response.text)

#Google Place API call
params = {
'key': 'AIzaSyAE-tQ0-K_j78fDO-IFXHXbKso35013mcc',
'q':'Los Angeles, CA, USA'
}
# url ='https://www.google.com/maps/embed/v1/place/json?'
url ='https://www.google.com/maps/embed/v1/place?key=AIzaSyAE-tQ0-K_j78fDO-IFXHXbKso35013mcc&q=Eiffel+Tower,Paris+France'
response = requests.get(url)
print(response.status_code == 200)


print(response.text)
#result = json.loads(response.text)