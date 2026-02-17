import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZXhwIjoxNzcxNTkyNzE4fQ.zn3V9NxEdEs8fzi1LfsNDLC5H64LaiXS5TFsp-J58YE"
}
requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)
print(requisicao)
print(requisicao.json())