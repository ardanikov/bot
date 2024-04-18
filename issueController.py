import requests


headers = {
    'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9zcGFjZS52ZW50dXJvLnByb1wvYXBpXC92MVwvYXV0aFwvbG9naW4iLCJpYXQiOjE3MDQ5NjAxODUsIm5iZiI6MTcwNDk2MDE4NSwianRpIjoiN200T1Vwd05xSHJlWVJCMyIsInN1YiI6NzYsInBydiI6ImYzMzY4YTM5ZjJjNTEyNmQ5NjMxNWJhZDc0YzRlODkzODdhNThmNGEiLCJ1c2VyIjp7ImlkIjo3NiwiZW1haWwiOiJ0dWdhcy5mcml6enlhcmRoYW5pQGdtYWlsLmNvbSIsInVwZGF0ZWRfc2VjdXJpdHkiOm51bGx9fQ.MqiBUqj0KPMFU6aBWxiNdg-BqCThBIgZ2pfOJ_Dk8so'
}
def create_issue(body):
    req = requests.post('https://space.venturo.pro/api/v1/review', json = body, headers=headers)
    id_issue = req.json()
    return id_issue['data']['id']

def update_issue(body):
    req = requests.put('https://space.venturo.pro/api/v1/review', json = body, headers=headers)
    