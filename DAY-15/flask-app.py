# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

#creating a flask app instance
app = Flask(__name__)

# Define a route that handles GET requests
@app.route("/createJIRA", methods=["POST"])
def createJIRA():
    url = "https://shamserul1357.atlassian.net/rest/api/3/issue"

    auth = HTTPBasicAuth("Example@gmail.com", "api-token")

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "my first jira ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        
        "issuetype": {
        "id": "10003"
        },
        
        "project": {
        "key": "SCRUM"
        },
        "summary": "first jira ticket",   
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))


app.run('0.0.0.0', port=5000)