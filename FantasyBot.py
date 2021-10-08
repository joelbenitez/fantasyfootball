import requests
from requests.structures import CaseInsensitiveDict

url = "https://hooks.slack.com/services/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"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = '{"text":"YourText"}'


resp = requests.post(url, headers=headers, data=data)