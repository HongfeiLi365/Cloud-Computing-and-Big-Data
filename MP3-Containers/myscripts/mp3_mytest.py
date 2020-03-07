import requests
import json


url1 = 'http://34.201.66.196:5000/img-classification/free'

payload = {"dataset":"mnist"}
		
r1 = requests.post(url1, json=payload)
print(r1.text)



url2 = 'http://34.201.66.196:5000/img-classification/premium'

payload = {"dataset":"mnist"}
		
r2 = requests.post(url2, json=payload)
print(r2.text)



url3 = 'http://34.201.66.196:5000/config'

r3 = requests.get(url3)
print(r3.text)
