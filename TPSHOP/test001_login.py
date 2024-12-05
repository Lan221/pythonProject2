import requests
#create session
session = requests.session()
#send request to get the key
response1 = session.get("https://www.google.com/")

