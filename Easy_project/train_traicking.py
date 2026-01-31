import requests
api_key = "3cbaacb2camsh4b482609edc72e8p10db80jsn7baaf0169172"
url = "https://indian-railway-irctc.p.rapidapi.com/api/trains/v1/train/status"

train_number = input("Enter train number: ")

headers = {
    "x-rapidapi-key": "3cbaacb2camsh4b482609edc72e8p10db80jsn7baaf0169172",
    "x-rapidapi-host": "indian-railway-irctc.p.rapidapi.com"
}

query = {"trainNo": train_number}

response = requests.get(url, headers=headers, params=query)
data = response.json()
print(data)