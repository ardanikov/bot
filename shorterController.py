import requests

headers = {
    'User-Agent': 'Chrome/62.0 (BSD x86_64; rv:71.0) Gecko/20100101 Firefox/71.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://s.id',
    'Connection': 'keep-alive',
    'Referer': 'https://s.id/',
}


# def shortLink():
#     data = {
#     'url': 'https://cdn.discordapp.com/attachments/1181792357205688370/1197441729046003753/image.png?ex=65bb4783&is=65a8d283&hm=14b9d0ec6002587173000e28f600a60496bb0154247978f5fcd11298e8b33c39&'
#     }
#     response = requests.post('https://s.id/api/public/link/shorten', headers=headers, data=data)
#     return response



data = {
'url': 'https://cdn.discordapp.com/attachments/1181792357205688370/1197441729046003753/image.png?ex=65bb4783&is=65a8d283&hm=14b9d0ec6002587173000e28f600a60496bb0154247978f5fcd11298e8b33c39&'
}
response = requests.post('https://s.id/api/public/link/shorten', headers=headers, data=data)
print(response)
