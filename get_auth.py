import requests
import json


auth_code = "use your own"
client_id = "use your use your own"
client_secret = "use your own"
code_challenge = "use your own"
code_verifier = code_challenge

access_token = "use your own"
refresh_token = "use your own"
# expires in 2678400 from 6:41pm 1/23/2021 (31 days)

def get_auth() :
    auth_url = ("https://myanimelist.net/v1/oauth2/authorize"
    "?response_type=code"
    "&client_id=" + client_id +
    "&code_challenge=" + code_challenge +
    "&state=1")

    print(auth_url)

def complete_auth():
    url = "https://myanimelist.net/v1/oauth2/token"
    data = {
        "client_id"    : client_id,
        "client_secret" : client_secret,
        "code"          : auth_code,
        "code_verifier" : code_verifier,
        "grant_type"    : "authorization_code"
    }
    response = requests.post(url, data)
    print(response.status_code)
    print(response.text)

def test_auth():
    url = "https://api.myanimelist.net/v2/users/@me"
    response = requests.get(url, headers={"Authorization" : "Bearer " + access_token})
    print(response.status_code)
    print(response.text)
    
# get_auth()
# complete_auth()
test_auth()
