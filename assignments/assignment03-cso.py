import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    with open("cso.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Data successfully retrieved and saved to cso.json")  # Success message
else:
    print("Failed to retrieve data")