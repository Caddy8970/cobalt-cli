import requests
import json
import webbrowser

target = input("Paste the link you want to download: ")

url = "https://api.cobalt.tools/api/json"
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}

data = {
    'url': target
}

response = requests.post(url, headers=headers, data=json.dumps(data))
response = response.json()
download = response['url']

webbrowser.open(download)
