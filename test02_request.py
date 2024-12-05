import requests
resp = requests.get(url="https://www.google.com/images/searchbox/desktop_searchbox_sprites318_hr.webp")
print(resp.text)