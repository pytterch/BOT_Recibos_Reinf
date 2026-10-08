from functions import *
from Json_Open import *

# Criando pasta da competência
append_pasta()

# Abertura do sistema domínio
system()

#Loop Principal executando todas as empresas do json
for nome, cod in dados[escolha]:
    print(f"Entrando na empresa {nome} 🏢")
    print(".\n.\n")
    navegar_dominio(cod)

    resultadoprimeiro = localizar_r2099()
    if resultadoprimeiro:
        print("💾 Salvando o Evento R-2099 💾")
        print(".\n.\n")
        clicar_evento_r2099()
        imprimir(cod, nome, "R-2000", escolha)
    else:
        print("Não foi encontrado Evento Atenção ‼️‼️‼️")
        print(".\n.\n")

    resultadoultimo = localizar_r4099()
    if resultadoultimo:
        print("💾 Salvando o Evento R-4099 💾")
        print(".\n.\n")
        clicar_evento_r4099()
        imprimir(cod, nome, "R-4000", escolha)
        voltar()
    else:
        print("🏢 Empresa sem Movimento de R-4000 🏢")
        print(".\n.\n")
        voltar()