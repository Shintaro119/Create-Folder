import requests

client_id = 'ifxgm52f01bb8j8te4h2tv6lmo4xlw4r'
client_secret = 'A5laygJ3jqXCIUH5NXnMjus3euMKM1Bc'

# 認証エンドポイントにリクエストを送信してトークンを取得します
auth_url = 'https://api.box.com/oauth2/token'
data = {'grant_type': 'client_credentials', 'client_id': client_id, 'client_secret': client_secret}
response = requests.post(auth_url, data=data)

# トークンを取得します
access_token = response.json()['access_token']
