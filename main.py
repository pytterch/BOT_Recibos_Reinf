import pymsgbox
from functions import *
from Json_Open import *
from functions_reserve import *

while True:
    if VPN("openvpn.exe"):
        print("O Vpn está Aberto, vamos rodar o programa no Acesso Remoto 🖥️")
        print(".\n.\n.")
        acesso_remoto()
        system()
        
        for nome, cod in dados["empresas"]:
            print(f"Entrando na empresa {nome} 🏢")
            print(".\n.\n")
            navegar_dominio(cod)

            resultadoprimeiro = localizar_R2099()
            if resultadoprimeiro:
                print("💾 Salvando o Evento R-2099 💾")
                print(".\n.\n")
                clicar_evento_R2099()
                imprimir(cod, nome, "R-2000")
            else:
                print("Não foi encontrado Evento Atenção ‼️‼️‼️")
                print(".\n.\n")

            resultadoultimo = localizar_R4099()
            if resultadoultimo:
                print("💾 Salvando o Evento R-4099 💾")
                print(".\n.\n")
                clicar_evento_R4099()
                imprimir(cod, nome, "R-4000")
                voltar()
            else:
                print("🏢 Empresa sem Movimento de R-4000 🏢")
                print(".\n.\n")
                voltar()
        break

    else:
        resposta = pymsgbox.confirm(text="Se está home office você precisa abrir o VPN",
                                    title="Alerta",
                                    buttons=("Ok", "Estou presencial"))
        if resposta == "Ok":
            print("Abra o VPN")
            break

        elif resposta == "Estou presencial":
            print("Não vai ser necessário usar o Acesso remoto 🖥️")
            print(".\n.\n")
            system()

            for nome, cod in dados["empresas"]:
                cod.lstrip("0")
                print(f"Entrando na empresa {nome} 🏢")
                print(".\n.\n")
                navegar_dominio(cod)

                resultadoprimeiro = localizar_R2099()
                if resultadoprimeiro:
                    print("💾 Salvando o Evento R-2099 💾")
                    print(".\n.\n")
                    clicar_evento_R2099()
                    imprimir(cod, nome, "R-2000")
                else:
                    print("Não foi encontrado Evento Atenção ‼️‼️‼️")
                    print(".\n.\n")

                resultadoultimo = localizar_R4099()
                if resultadoultimo:
                    print("💾 Salvando o Evento R-4099 💾")
                    print(".\n.\n")
                    clicar_evento_R4099()
                    imprimir(cod, nome, "R-4000")
                    voltar()
                else:
                    print("🏢 Empresa sem Movimento de R-4000 🏢")
                    print(".\n.\n")
                    voltar()
            break
        else:
            continue