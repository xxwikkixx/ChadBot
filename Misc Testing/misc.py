import requests
r = requests.get('https://finnhub.io/api/v1/scan/support-resistance?symbol=IBM&resolution=D&token=')
print(r.json())