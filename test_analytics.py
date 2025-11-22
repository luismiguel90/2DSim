import requests

# Para testar POST request em analytics

url = "http://127.0.0.1:5000/api/analytics"
data = {"activityID": "instancia_1"}

response = requests.post(url, json=data)
print(response.json())