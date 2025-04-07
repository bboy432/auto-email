import requests
from requests.structures import CaseInsensitiveDict

url = "https://raw.githubusercontent.com/bboy432/auto-email/main/README.md"

# If repo is private - we need to add a token in header:
headers = CaseInsensitiveDict()


resp = requests.get(url, headers=headers)
print(resp.status_code)
f = open("wow.md", "w")
f.write(str(resp.text))
f.close()
