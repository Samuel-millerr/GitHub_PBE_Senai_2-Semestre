from tamagoshiBreeds import TamagoshiJedi, TamagoshiSith, TamagoshiDroid

import random
from time import sleep
from os import system

def clear():
    system('cls')

def main():
    tamagoshi_criado =  False # Declarações de variáveis utilizadas no código

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

            if decisao == "1": tamagoshi = TamagoshiJedi(nome)
            elif decisao == "2": tamagoshi = TamagoshiSith(nome)
            elif decisao == "3": tamagoshi = TamagoshiDroid(nome)

            clear()
            print(f"O tamagoshi foi criado seu nome é \033[3;33m{tamagoshi.nome}\33[m e ele é um {tamagoshi.__class__.__name__}")
            tamagoshi_criado = True

        elif decisao == "2":
            if not tamagoshi_criado: 
                clear()
                print("Você ainda não criou seu tamagoshi, por gentileza crie ele antes de continuar.")
            else: 
                print("teste")
                quadrantes = 0
                while True:
                    tamagoshi.vida() # Verifica as condições de vida do tamagoshi
                    
                    if tamagoshi.saude <= 0:
                        clear()

                        print("Seu bixinho morreu T_T...")
                        input("... aperte ENTER para continuar")
                        
                        tamagoshi_criado = False
                        break   
                    else:
                        clear()         
                        quadrantes += 1 # Passagem de tempo 

                        if quadrantes > 1: # Mostra a passagem de tempo somente após o primeiro quadrante
                            tamagoshi.passar_tempo()  
                            if tamagoshi.lado_forca == "Luz" or tamagoshi.lado_forca == "Sombrio": print(f"\nO atual humor de {tamagoshi.nome} é {tamagoshi.getHumor()}")         
                            print(f"O tempo passou, {tamagoshi.nome} agora tem {tamagoshi.idade:.1f} anos.")

                        print(f"\nQUADRANTE {quadrantes}º")
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
                                            "\n[ 3 ] Canalizar raiva \033[3;37m#Diminui a saúde e aumenta a raiva de seu tamagoshi\33[m" 
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
                            clear()
                            if tamagoshi.lado_forca == "Luz" or tamagoshi.lado_forca == "Sombrio": 
                                print("\33[34mAÇÃO:\033[m BRINCAR")
                                tempo = int(input("Digite a quantidade de tempo que você deseja dar brincar com seu tamagoshi: "))
                                print(f"{tamagoshi.nome} está brincando...")
                                sleep(2)

                                tedio_anterior = tamagoshi.tedio
                                tamagoshi.brincar(tempo)
                                
                                print("\nSTATUS ANTIGO X STATUS NOVO")
                                print(f"Tédio:   {tedio_anterior:.2f}    >      {tamagoshi.tedio:.2f}")

                            else: 
                                print("\33[34mAÇÃO:\033[m RECARREGAR BATERIAS")
                                print(f"{tamagoshi.nome} está sendo recarregado...")
                                sleep(2)

                                bateria_anterior = tamagoshi.bateria
                                tamagoshi.recarregar_bateria()

                                print("\nSTATUS ANTIGO X STATUS NOVO")
                                print(f"Bateria:   {bateria_anterior:.2f}    >     {tamagoshi.bateria:.2f}")

                        elif decisao == "2":
                            clear()
                            if tamagoshi.lado_forca == "Luz" or tamagoshi.lado_forca == "Sombrio":
                                print("\33[34mAÇÃO:\033[m ALIMENTAR")
                                comida = int(input("Digite a quantidade de comida que você deseja dar para seu tamagoshi: "))
                                print(f"{tamagoshi.nome} está comendo...")
                                sleep(2)
                                
                                fome_anterior = tamagoshi.fome
                                tamagoshi.alimentar(comida)
                                
                                print("\nSTATUS ANTIGO X STATUS NOVO")
                                print(f"Fome:    {fome_anterior:.2f}  >     {tamagoshi.fome:.2f}")

                            else: 
                                print("\33[34mAÇÃO:\033[m AUTOCONSERTO")
                                print(f"{tamagoshi.nome} está se autoconsertando...")
                                sleep(2)

                                saude_anterior = tamagoshi.saude
                                tamagoshi.autoconserto()

                                print("\nSTATUS ANTIGO X STATUS NOVO")
                                print(f"Condição:   {saude_anterior:.2f}  >     {tamagoshi.saude:.2f}")

                        elif decisao == "3":
                            clear()
                            if tamagoshi.lado_forca == "Luz": 
                                print("\33[34mAÇÃO:\033[m MEDITAR")
                                print(f"{tamagoshi.nome} está meditando...")
                                sleep(2)

                                saude_anterior = tamagoshi.saude
                                tedio_anterior = tamagoshi.tedio
                                paz_anterior = tamagoshi.paz
                                tamagoshi.meditar()
                                
                                print("\nSTATUS ANTIGO X STATUS NOVO")
                                print(f"Saúde:   {saude_anterior:.2f}  >     {tamagoshi.saude:.2f}")
                                print(f"Tedio:   {tedio_anterior:.2f}  >     {tamagoshi.tedio:.2f}")
                                print(f"Paz:     {paz_anterior:.2f}    >     {tamagoshi.paz:.2f}")

                            elif tamagoshi.lado_forca == "Sombrio": 
                                print("\33[34mAÇÃO:\033[m CANALIZAR RAIVA")
                                print(f"{tamagoshi.nome} está canalizando sua raiva...")
                                sleep(2)

                                saude_anterior = tamagoshi.saude
                                tedio_anterior = tamagoshi.tedio
                                raiva_anterior = tamagoshi.raiva
                                tamagoshi.canalizar_raiva()

                                print("\nSTATUS ANTIGO X STATUS NOVO")
                                print(f"Saúde:   {saude_anterior:.2f}  >     {tamagoshi.saude:.2f}")
                                print(f"Tedio:   {tedio_anterior:.2f}  >     {tamagoshi.tedio:.2f}")
                                print(f"Raiva:     {raiva_anterior:.2f}    >     {tamagoshi.raiva:.2f}")

                            else: 
                                print("\33[34mAÇÃO:\033[m AUTODESTRUIÇÃO")
                                print(f"{tamagoshi.nome} irá se autodestruir em...")
                                print(3)
                                sleep(2)
                                print(2)
                                sleep(2)
                                print(1)
                                sleep(2)

                                tamagoshi.autodestruicao()
                                
                        elif decisao == "4" and tamagoshi.lado_forca in ("Luz","Sombrio"):
                            clear()
                            if tamagoshi.lado_forca == "Luz": 
                                clear()
                                print("\33[34mAÇÃO:\033[m CURAR")
                                print(f"{tamagoshi.nome} está se curando...")
                                sleep(2)

                                saude_anterior = tamagoshi.saude
                                tamagoshi.curar_com_forca()

                                print("\nSTATUS ANTIGO X STATUS NOVO")
                                print(f"Saúde:   {saude_anterior:.2f}  >     {tamagoshi.saude:.2f}")

                            elif tamagoshi.lado_forca == "Sombrio": 
                                clear()
                                print("\33[34mAÇÃO:\033[m RITUAL SOMBRIO")
                                print(f"{tamagoshi.nome} está mexendo com o lado negro..")
                                sleep(2)

                                saude_anterior = tamagoshi.saude
                                fome_anterior = tamagoshi.fome
                                raiva_anterior = tamagoshi.raiva
                                tamagoshi.ritual_sombrio()

                                print("\nSTATUS ANTIGO X STATUS NOVO")
                                print(f"Saúde:   {saude_anterior:.2f}  >     {tamagoshi.saude:.2f}")
                                print(f"Fome:   {fome_anterior:.2f}  >     {tamagoshi.fome:.2f}")
                                print(f"Raiva:     {raiva_anterior:.2f}    >     {tamagoshi.raiva:.2f}")
                        
                        elif decisao == "5":
                            clear()
                            tamagoshi.mudar_lado_forca()
                            if tamagoshi.lado_forca == "Luz":    
                                if tamagoshi.paz <= 0:
                                    nome = tamagoshi.nome

                                    tamagoshi = TamagoshiSith.criar_tamagoshi(nome)
                            else:
                                if tamagoshi.raiva <= 0:
                                    nome = tamagoshi.nome

                                    tamagoshi = TamagoshiJedi.criar_tamagoshi(nome)                        
                        else: 
                            clear()
                            print("Você moscou hein, não selecionou nenhuma das opções! Você não interagiu com seu tamagoshi T_T.")

                        input("\nAperte \33[1;32mENTER\33[m para passar o tempo\n")
        else:
            clear()
            print("Você não escolheu nenhuma das opções, por gentileza tente novamente.")
main()