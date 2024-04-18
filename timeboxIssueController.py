import requests

def create_timebox_issue(body):
    req = requests.post('https://space.venturo.pro/api/v2/timebox', json = body)
    return req