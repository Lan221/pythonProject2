import requests
resp = requests.get("http://www.google.fr")
print(resp.text)