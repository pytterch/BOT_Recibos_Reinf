import json
import easygui

with open("modificado.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

grupos = list(dados.keys())

escolha = easygui.choicebox("Qual grupo deseja rodar?", "Selecionar Grupo", grupos)

if escolha not in grupos:
    print("Nenhum grupo selecionado, encerrando.")
    exit()

empresas_para_rodar = dados[escolha]
print(f"Rodando grupo: {escolha} ({len(empresas_para_rodar)} empresas)")
