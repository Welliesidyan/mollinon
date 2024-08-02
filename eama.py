import requests

url = 'https://api.example.com/data'
headers = {
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")
