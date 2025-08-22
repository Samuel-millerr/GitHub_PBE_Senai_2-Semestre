from tamagoshiClass import Tamagoshi
from random import randint

# Declaração da primeira classe de tamagoshi
class TamagoshiJedi(Tamagoshi):
    def __init__(self, nome, idade: float = 0, fome: int = 0, saude: int = 80, tedio: int = 0, paz: int = 50, lado_forca: str = "Luz"):
        super().__init__(nome, idade, fome, saude, tedio)
        self.paz = paz
        self.lado_forca = lado_forca
    
    def meditar(self):
        paz = randint(-8, 12)
        self.saude += 10
        self.tedio -= randint(5, 10)
        self.paz += paz

        if paz <= 0 : print(f"Durante a meditação {self.nome} teve pensamentos sombrios, sua paz interior foi abalada!")

    def curar_com_forca(self):
        cura = randint(0, 15)
        self.saude += cura

    def mudar_lado_forca(self, nome):
        if self.paz > 50:
            print(f"{self.nome} não pode mudar para o lado sombrio, sua paz interior é muito grande!")
        elif self.paz > 10:
            print(f"{self.nome} sente o lado sombrio o chamando mas ainda resiste sobre esses pensamentos.")
        else:
            print(f"{self.nome} desistiu do lado da luz...")
            tamagoshi = TamagoshiSith(nome)
            return tamagoshi
    
    def vida(self):
        super().vida
        if (self.fome > 50 and self.fome <= 60) or (self.tedio > 50 and self.tedio <=60): self.paz -= 10
        elif (self.fome > 60 and self.fome <= 80) or (self.tedio > 60 and self.tedio <=80): self.paz -= 20
        elif (self.fome > 80 and self.fome <=90) or (self.tedio > 80 and self.tedio <=90): self.paz -= 30

# Declaração da segunda classe de tamagoshi
class TamagoshiSith(Tamagoshi):
    def __init__(self, nome, idade: float = 0, fome: int = 0, saude: int = 100, tedio: int = 15, raiva: int = 50, lado_forca: str = "Sombrio"):
        super().__init__(nome, idade, fome, saude, tedio)
        self.raiva = raiva
        self.lado_forca = lado_forca

    def canalizar_raiva(self):
        self.saude += 5
        self.tedio -= randint(0, 10)
        self.raiva += randint(0, 5)
    
    def ritual_sombrio(self):
        self.saude += 20
        self.fome += 25
        self.raiva += 15

    def mudar_lado_forca(self, nome):
        if self.raiva > 50:
            print(f"{self.nome} não pode mudar para o lado da luz, sua raiva interior é muito grande!")
        elif self.raiva > 10:
            print(f"{self.nome} sente o lado da luz o chamando mas ignora sobre esses pensamentos.")
        else:
            print(f"{self.nome} desistiu do lado sombrio...")
            tamagoshi = TamagoshiJedi(nome)
            return tamagoshi
        
    def vida(self):
        super().vida
        if (self.fome > 50 and self.fome <= 60) or (self.tedio > 50 and self.tedio <=60): self.raiva -= 10
        elif (self.fome > 60 and self.fome <= 80) or (self.tedio > 60 and self.tedio <=80): self.raiva -= 20
        elif (self.fome > 80 and self.fome <=90) or (self.tedio > 80 and self.tedio <=90): self.raiva -= 30
        
# Declaração da terceira classe de tamagoshi
class TamagoshiDroid(Tamagoshi):
    def __init__(self, nome: str, idade: float = 0, bateria: int = 100, condicao: int = 100):    
        self.nome = nome
        self.idade = idade
        self.bateria = bateria
        self.condicao = condicao

    def recarregar_bateria(self):
        energia = randint(0, 15)
        self.bateria += energia
    
    def autoconserto(self):
        self.condicao += 10
        self.idade += 0.5
    
    def autodestruicao(self):
        self.condicao = 0
