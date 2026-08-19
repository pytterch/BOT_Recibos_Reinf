import json

with open("modificado.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

for item in dados["Empresas"]:
    item[1] = item[1].lstrip("0")