import requests
import json

url1 = 'http://54.198.188.96:80/'

payload = {
		"num":0
		}

r = requests.post(url1, json=payload)
print(r.text)

r2 = requests.get(url1)
print(r2.text)


url2 = 'http://3.83.51.151:80/'

payload = {
		"num":0
		}

r = requests.post(url2, json=payload)
print(r.text)

r2 = requests.get(url2)
print(r2.text)



url3 = 'http://lb1-852577388.us-east-1.elb.amazonaws.com'

payload = {
		"num":0
		}

r = requests.post(url3, json=payload)
print(r.text)

r2 = requests.get(url1)
print(r2.text)

r2 = requests.get(url2)
print(r2.text)

r2 = requests.get(url3)
print(r2.text)
