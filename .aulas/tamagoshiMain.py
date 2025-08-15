from tamagoshiBreeds import TamagoshiSindical, TamagoshiNulo, TamagoshiReacionario

from random import choice
from os import system

tamagoshi_criado = False

def clear():
    system('cls')

def main():
    while True:
        print("=== CUIDE DE SEU TAMAGOSHI ==")
        print("Tome sua decisão de acordo com uma das opções abaixo (digite os números):")
        decisao = input("[ 1 ] Criar Tamagoshi \n[ 2 ] Cuidar de seu Tamagoshi \n[ 0 ] Sair\n >").strip()
        if decisao == "0":
            break
        elif decisao == "1":
            clear()
            print("Digite o nome do seu tamagoshi")
            nome = input("\n > ")
            
            clear()
            print("Escolha o vies politico de seu Tamagoshi: ")
            decisao = input("[ 1 ] Esquerda\n[ 2 ] Centro\n[ 3 ] Direita")
            if decisao == "1": 
                tamagoshi = TamagoshiSindical(nome, "Esquerda")
            elif decisao == "2":
                tamagoshi = TamagoshiNulo(nome, "Centro")
            elif decisao == "3":
                tamagoshi = TamagoshiReacionario(nome, "Esquerda")
            else:
                vies = choice("Esquerdista", "Centrista", "Direita")
                print(f"Você não selecionou nenhuma das opções, por isso foi selecionado um vies aleatorio, {vies}")
            
            clear()


        elif decisao == "2":
            pass

main()