import requests

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(r.headers)
print(r.status_code)
print(r.json())
print(r.json()['bpi'])
print(r.json()['bpi']['USD'])
print(r.json()['bpi']['USD']['rate'])