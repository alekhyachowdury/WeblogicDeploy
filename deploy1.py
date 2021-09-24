import requests
import json

url = "https://150.136.152.236:7002/management/wls/latest/deployments/application"

payload={"name": "testwebapp","targets": ["ibmjcs_d_adminserver"]}


files = {'model':(None, json.dumps(payload), 'application/json'),
         'deployment': ('SampleWebApp5.war', open('SampleWebApp5.war', 'rb'), 'application/octet-stream')
                         }


headers = {  
  'X-Requested-By': 'TestClient',
  'Authorization': 'Basic d2VibG9naWM6d2VsY29tZTE=',
  }

response = requests.request("POST", url, headers=headers,  files=files, verify=False)

print(response.text)
