import requests


def loc():
    url  ='https://maps.googleapis.com/maps/api/distancematrix/json?origins=28.63604402976094,77.28579609207998&destinations=28.6306293465413,77.22327540106556&units=imperial&key=AIzaSyA2EXfIe-2Zcggbr1UjpAFr5Bjlsu3yLsQ',
    res = requests.get(url)
    return res

# loc()


import requests

url = 'https://maps.googleapis.com/maps/api/directions/json?origins=28.63604402976094,77.28579609207998&destinations=28.6306293465413,77.22327540106556&units=imperial&key=AIzaSyA2EXfIe-2Zcggbr1UjpAFr5Bjlsu3yLsQ',

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


