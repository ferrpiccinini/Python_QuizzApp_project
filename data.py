import requests
data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
data_json = data.json()
