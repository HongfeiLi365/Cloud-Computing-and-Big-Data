import requests
import json
url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp3-test"
payload = {
        	"accountId": #<your aws account id used for accessing lex>,
		    "submitterEmail": # <insert your coursera account email>,
		    "secret": # <insert your secret token from coursera>,
		    "ipaddress": #<Insert IP:Port of EKS Master>
    }
r = requests.post(url, data=json.dumps(payload))
print(r.status_code, r.reason)
print(r.text)