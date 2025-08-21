from tamagoshiBreeds import TamagoshiJedi, TamagoshiSith, TamagoshiDroid

import random
from time import sleep
from os import system

def clear():
    system('cls')

def main():
    # Declarações de variáveis utilizadas no código
    tamagoshi_criado = False
    quadrantes = 1

    while True:
        print("=== CUIDE DE SEU TAMAGOSHI ==")
        print("Tome sua decisão de acordo com uma das opções abaixo (digite os números):")
        decisao = input("[ 1 ] Criar Tamagoshi \n[ 2 ] Cuidar de seu Tamagoshi \n[ 0 ] Sair\n > ").strip()
        if decisao == "0":
            break
        elif decisao == "1":
            clear()
            print("Digite o nome do seu tamagoshi:")
            nome = input(" > ").strip()
            clear()
            print("Decida de qual raça seu tamagoshi será:")
            decisao = input("[ 1 ] Jedi\n[ 2 ] Sith\n[ 3 ] Droid\n > ").strip()
            if decisao not in ["1","2","3"]:
                decisao = random.choice(["1","2","3"])
                print(f"Você não escolheu nenhuma das opções possíveis, por isso for escolhido aleatoriamente, seu tamagoshi será a opção {decisao}")
                sleep(2)

            if decisao == "1": tamagoshi = TamagoshiJedi.criar_tamagoshi(nome)
            elif decisao == "2": tamagoshi = TamagoshiSith.criar_tamagoshi(nome)
            elif decisao == "3": tamagoshi = TamagoshiDroid.criar_tamagoshi(nome)

            clear()
            print(f"O tamagoshi foi criado seu nome é \033[3;33m{tamagoshi.nome}\33[m e ele é um {tamagoshi.__class__.__name__}")
            tamagoshi_criado = True if tamagoshi else False

        elif decisao == "2":
            if not tamagoshi_criado: 
                clear()
                print("Você ainda não criou seu tamagoshi, por gentileza crie ele antes de continuar.")
            else: 
                while True:
                    clear()
                    print(f"QUADRANTE {quadrantes}º")
                    print("Segue as informações sobre seu tamagoshi:")
                    tamagoshi.info_tamagoshi(tamagoshi)

                    print("\nQual ação você irá realizar com seu tamagoshi?")
                    if tamagoshi.lado_forca == "Luz":
                        decisao = input("[ 1 ] Brincar \033[3;37m# Diminui o tédio de seu tamagoshi\33[m" 
                                        "\n[ 2 ] Alimentar \033[3;37m# Diminui a fome de seu tamagoshi\33[m" 
                                        "\n[ 3 ] Meditar \033[3;37m# Aumenta a saúde e a paz de seu tamagoshi\33[m" 
                                        "\n[ 4 ] Curar com força \033[3;37m# Usa a força interior para recuperar vida\33[m" 
                                        "\n[ 5 ] Trocar lado da força \033[3;37m#...\33[m" 
                                        "\n[ 0 ] Sair\n > ").strip()
                    elif tamagoshi.lado_forca == "Sombrio":
                        decisao = input("[ 1 ] Brincar \033[3;37m# Diminui o tédio de seu tamagoshi\33[m" 
                                        "\n[ 2 ] Alimentar \033[3;37m# Diminui a fome de seu tamagoshi\33[m" 
                                        "\n[ 3 ] Canalizar raiva \033[3;37m#Aumenta a saúde e a raiva de seu tamagoshi\33[m" 
                                        "\n[ 4 ] Ritual sombrio \033[3;37m# Recupera muito a vida de seu tamagoshi, porém lhe causa fome\33[m" 
                                        "\n[ 5 ] Trocar lado da força \033[3;37m#...\33[m" 
                                        "\n[ 0 ] Sair\n > ").strip()
                    else:
                        decisao = input("[ 1 ] Recarregar bateria \033[3;37m# Recupera a bateria de seu tamagoshi\33[m"
                                        "\n[ 2 ] Autoconserto \033[3;37m# Recupera a condição de seu tamagoshi\33[m" 
                                        "\n[ 3 ] Autodestruição \033[3;37m#...\33[m"
                                        "\n[ 0 ] Sair\n > ").strip()
                    
                    if decisao == "0":
                        clear()
                        print(f"{tamagoshi.nome} foi dormir....")
                        break
                    elif decisao == "1": 
                        if decisao in ("1", "2"):  
                            tempo = int(input("Digite a quantidade de tempo que você deseja dar brincar com seu tamagoshi: "))
                            tedio_anterior = tamagoshi.tedio
                            tamagoshi.brincar(tempo)
                            print("\nSTATUS ANTIGO X STATUS NOVO")
                            print(f"Tédio: {tedio_anterior} > {tamagoshi.tedio}")
                        else: 
                            bateria_anterior = tamagoshi.bateria
                            tamagoshi.recarregar_bateria()
                            print("\nSTATUS ANTIGO X STATUS NOVO")
                            print(f"Bateria: {bateria_anterior} > {tamagoshi.bateria}")

                    elif decisao == "2":
                        if decisao in ("1", "2"):
                            comida = int(input("Digite a quantidade de comida que você deseja dar para seu tamagoshi: "))
                            fome_anterior = tamagoshi.fome
                            tamagoshi.alimentar(comida)
                            print("\nSTATUS ANTIGO X STATUS NOVO")
                            print(f"Fome: {fome_anterior} > {tamagoshi.fome}")
                        else: 
                            condicao_anterior = tamagoshi.condicao
                            tamagoshi.autoconserto()
                            print(f"Condição: {condicao_anterior} > {tamagoshi.condicao}")

                    elif decisao == "3":
                        if tamagoshi.lado_forca == "Luz": 
                            tamagoshi.meditar()
                        elif tamagoshi.lado_forca == "Sombrio": 
                            tamagoshi.canalizar_raiva()
                        else: 
                            tamagoshi.autodestruicao()
                            
                    elif decisao == "4":
                        if tamagoshi.lado_forca == "Luz": tamagoshi.curar_com_forca()
                        elif tamagoshi.lado_forca == "Sombrio": tamagoshi.ritual_sombrio()
                    
                    elif decisao == "5":
                        if tamagoshi.lado_forca == "Luz": tamagoshi.mudar_lado_forca(tamagoshi.nome)
                        elif tamagoshi.lado_forca == "Sombrio": tamagoshi.mudar_lado_forca(tamagoshi.nome)
                    
                    else: 
                        print("Você moscou hein, não selecionou nenhuma das opções, você não interagiu com seu tamagoshi T_T")

                    print(f"O atual humor de {tamagoshi.nome} é {tamagoshi.getHumor()}")
                    passar = input("Aperte \33[1;32mENTER\33[m para passar o tempo\n")

                    clear()         
                    quadrantes += 1
                    tamagoshi.passar_tempo()           
                    print(f"O tempo passou, {tamagoshi.nome} agora tem {tamagoshi.idade:.2f}")
        else:
            clear()
            print("Você não escolheu nenhuma das opções, por gentileza tente novamente.")
main()