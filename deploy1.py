import requests
import json

url = "https://150.136.152.236:7002/management/wls/latest/deployments/application"
#url = "http://localhost:1880/test"

payload={"model": {"name":"testwebapp","targets": [ "ibmjcs_d_adminserver"]}}


files = {
         'deployment': ('SampleWebApp.war', open('C://deploypoc//SampleWebApp.war', 'rb'), 'application/octet-stream')
                         }


headers = {  
  'X-Requested-By': 'TestClient',
  'Authorization': 'Basic d2VibG9naWM6d2VsY29tZTE=',
  }

response = requests.request("POST", url, headers=headers, data=payload, files=files, verify=False)

print(response.text)
