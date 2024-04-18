import requests


headers = {
    'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9zcGFjZS52ZW50dXJvLnByb1wvYXBpXC92MVwvYXV0aFwvbG9naW4iLCJpYXQiOjE3MDQ5NjAxODUsIm5iZiI6MTcwNDk2MDE4NSwianRpIjoiN200T1Vwd05xSHJlWVJCMyIsInN1YiI6NzYsInBydiI6ImYzMzY4YTM5ZjJjNTEyNmQ5NjMxNWJhZDc0YzRlODkzODdhNThmNGEiLCJ1c2VyIjp7ImlkIjo3NiwiZW1haWwiOiJ0dWdhcy5mcml6enlhcmRoYW5pQGdtYWlsLmNvbSIsInVwZGF0ZWRfc2VjdXJpdHkiOm51bGx9fQ.MqiBUqj0KPMFU6aBWxiNdg-BqCThBIgZ2pfOJ_Dk8so'
}
body = {
'created_at' : "",
'created_by' : "289",
'duedate' : "",
'feature_issue' :  "",
'is_accept_review' : "",
'is_review': "1",
'm_project_id' : "2",
'm_project_status' : "1",
'name' : "no data 2",
'point' : 0,
'type' : "0",
'user_acceptance_id' : 5,
'user_auth_id' : 76
}

req = requests.post('https://space.venturo.pro/api/v1/review', json = body, headers=headers)
print(req)