import requests
import json

ROOT_URL = 'https://bugzilla.mozilla.org/'
API_KEY = '<your-bugzilla-api-key>'

def get_call(URL, *queries):
    headers = {'X-BUGZILLA-API-KEY' : API_KEY}
    payload = {}
    for query in queries:
        payload[query[0]] = query[1]
    response = requests.get(URL, headers=headers, params=payload)
    if response.status_code == 200:
        body = response.json()
    else:
        try:
            body = response.json()
        except Exception:
            body = None
    return response.status_code, body


def search_bugs(*queries):
    URL = ROOT_URL + 'rest/bug'
    status_code, response = get_call(URL, *queries)
    return status_code, response
