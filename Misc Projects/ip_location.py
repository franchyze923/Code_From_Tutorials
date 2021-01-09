import requests

## single ip request
# response = requests.get("http://ip-api.com/json/24.48.0.1").json()
#
# print(response['lat'])
# print(response['lon'])

# batch ip request

response = requests.post("http://ip-api.com/batch", json=[
  {"query": "208.80.152.201"},
  {"query": "167.71.3.52"},
  {"query": "206.189.198.234"},
  {"query": "157.230.75.212"}
]).json()

for ip_info in response:
    for k,v in ip_info.items():
        print(k,v)
    print("\n")


