import requests
import json
response = requests.get('https://api.smartsheet.com/2.0/sheets/7679274808305540',headers = {'Authorization':'Bearer zwusuvdtqnmgib0vyvwexozj89','Content-Type':'application/json'})
json_file = response.json()
f = open("copy.txt","w+")
f.write(json_file)
f.close()