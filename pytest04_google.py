import pytest
import requests
req = requests.get("https://www.google.com/")
print(req.text)
assert 201 == req.status_code