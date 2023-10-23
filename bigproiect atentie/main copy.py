from api import *
import requests

api_url = 'https://api.api-ninjas.com/v1/country?name=United States'
response = requests.get(api_url, headers={'X-Api-Key': '5IAHbuEJqhVMzlgGpK0SzQ==OpnN3GgrUVEoIrLl'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)


#Zn1hYdrN6uYVJXHJefAvtRIwQInIoJ0dRpcaphMZ