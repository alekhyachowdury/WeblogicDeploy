import requests
import json

url = "https://150.136.152.236:7002/management/wls/latest/deployments/application"
#url = "http://localhost:1880/test"


payload={"name": "testwebapp2","targets": ["ibmjcs_d_adminserver"]}

files = {'model':(None, json.dumps(payload), 'application/json'),
         'deployment': ('SampleWebApp7.war', open('SampleWebApp7.war', 'rb'), 'application/octet-stream')
                         }
print(files)

headers = {  
  'X-Requested-By': 'TestClient',
  'Authorization': 'Basic d2VibG9naWM6d2VsY29tZTE=',
  }

response = requests.request("POST", url, headers=headers, files=files, verify=False)

print(response.text)
