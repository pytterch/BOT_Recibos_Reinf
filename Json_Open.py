import json

with open("Sem movimento_Pedro.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

for item in dados["empresas"]:
    item[1] = item[1].lstrip("0")