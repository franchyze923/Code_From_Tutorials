import requests

# Implicit Grant Flow
# Get this token from requesting in browser

access_token = "paste your token that you got from browser url here"

header = {'Authorization': 'Bearer {}'.format(access_token)}
response = requests.get("https://api.fitbit.com/1/user/-/profile.json", headers=header).json()

print(response['user'])

for k, v in response['user'].items():
    print(k)
    print(v)
    print("\n")


