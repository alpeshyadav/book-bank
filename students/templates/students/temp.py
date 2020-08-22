import requests


url = "https://deckofcardsapi.com/api/deck/tnwmc9dqygl8/draw/"

querystring = {"count":"3"}

headers = {
    'User-Agent': "PostmanRuntime/7.18.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "923503e1-9a10-4636-b914-54b677e17fe9,5825a854-b41f-4cbc-baff-263c60fc2889",
    'Host': "deckofcardsapi.com",
    'Accept-Encoding': "gzip, deflate",
    'Cookie': "__cfduid=d0f1ecc6e0c56078cfef9b7644665cd441580046839",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

deck = response.json()
deck_id = deck['deck_id']
print(deck_id)