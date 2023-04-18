import requests

# URL da API que será requisitada:
API_LINK = "https://cat-fact.herokuapp.com/facts"

# Requisita a API:
response = requests.get(API_LINK)

# Converte a resposta para um objeto Json:
json_cat = response.json()

print("Aqui estão 5 fatos diários sobre gatos: \n")

x = 1

# Printa os 5 fatos diarios sobre gatos:
for i in json_cat:
    print(f"{x} - { i['text'] }")
    x = x + 1

print("\n")