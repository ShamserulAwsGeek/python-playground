

#ATATT3xFfGF0QxZC-q1VbMel8wQEkvs0N8IKS70-cV0E2gJ1JOBay2Q_ePQH3isH-jebq4ppXIqAN9OIKN-BMz_LSM9a3oyLdCM-lGaJ_6rfm00geuUOL8egysiFE2uTNykaHE-rSoi4qSsLqwmQmMo1UXILiwwQgCJyS2emP3Zh4_zKWAVoOs8=7DE75A18


# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://shamserul1357.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("shamserul1357@gmail.com", "ATATT3xFfGF0QxZC-q1VbMel8wQEkvs0N8IKS70-cV0E2gJ1JOBay2Q_ePQH3isH-jebq4ppXIqAN9OIKN-BMz_LSM9a3oyLdCM-lGaJ_6rfm00geuUOL8egysiFE2uTNykaHE-rSoi4qSsLqwmQmMo1UXILiwwQgCJyS2emP3Zh4_zKWAVoOs8=7DE75A18")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))