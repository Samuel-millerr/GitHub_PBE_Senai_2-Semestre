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
        self.saude = min(100, self.saude + 10)
        self.tedio = max(self.tedio-self.tedio, self.tedio - randint(5, 10)) # Utilizado para para o tedio não ficar negativo
        self.paz = min(100, self.paz + paz)

        if paz <= 0 : print(f"Durante a meditação {self.nome} teve pensamentos sombrios, sua paz interior foi abalada!")

    def curar_com_forca(self):
        cura = randint(0, 15)
        self.saude = min(100, self.saude + cura)

    def mudar_lado_forca(self):
        if self.paz > 50:
            paz = randint(2, 10)
            self.paz = max(0, self.paz - paz)
            print(f"{self.nome} não pode mudar para o lado sombrio, sua paz interior é muito grande!")
            print(f"Por tentar mudar de lado {self.nome} perdeu {paz} de paz!")
        elif self.paz > 10:
            paz = randint(5, 15)
            self.paz = max(0, self.paz - paz)
            print(f"{self.nome} sente o lado sombrio o chamando mas ainda resiste sobre esses pensamentos.")
            print(f"Por tentar mudar de lado {self.nome} perdeu {paz} de paz!")
        else:
            print(f"{self.nome} desistiu do lado da luz...")
            self.paz = 0

    def passar_tempo(self):
        super().passar_tempo()
        self.paz = max(0, self.paz - randint(0, 5))

# Declaração da segunda classe de tamagoshi
class TamagoshiSith(Tamagoshi):
    def __init__(self, nome, idade: float = 0, fome: int = 0, saude: int = 100, tedio: int = 15, raiva: int = 50, lado_forca: str = "Sombrio"):
        super().__init__(nome, idade, fome, saude, tedio)
        self.raiva = raiva
        self.lado_forca = lado_forca

    def canalizar_raiva(self):
        self.saude = min(100, self.saude - 5)
        self.tedio = max(self.tedio-self.tedio, self.tedio - randint(5, 10)) # Utilizado para para o tedio não ficar negativo
        self.raiva = min(100, self.raiva + randint(0, 5))
    
    def ritual_sombrio(self):
        self.saude = min(100, self.saude + 20)
        self.fome = min(100, self.fome + 25)
        self.raiva = min(100, self.raiva + 15)

    def mudar_lado_forca(self):
        if self.raiva > 50:
            raiva = randint(2, 5)
            self.raiva = max(0, self.raiva - raiva)
            print(f"{self.nome} não pode mudar para o lado da luz, sua raiva interior é muito grande!")
            print(f"Por tentar mudar de lado {self.nome} perdeu {raiva} de raiva!")
        elif self.raiva > 10:
            raiva = randint(2, 10)
            self.raiva = max(0, self.raiva - raiva)
            print(f"{self.nome} sente o lado da luz o chamando mas ignora esses pensamentos.")
            print(f"Por tentar mudar de lado {self.nome} perdeu {raiva} de raiva!")
        else:
            print(f"{self.nome} desistiu do lado sombrio...")
            self.raiva = 0
        
    def passar_tempo(self):
        super().passar_tempo()
        self.raiva = max(0, self.raiva - randint(0, 5))

        
# Declaração da terceira classe de tamagoshi
class TamagoshiDroid(Tamagoshi):
    def __init__(self, nome: str, idade: float = 0, bateria: int = 100, saude: int = 100):    
        self.nome = nome
        self.idade = idade
        self.bateria = bateria
        self.saude = saude
        self.lado_forca = "null"

    def recarregar_bateria(self):
        energia = randint(10, 20)
        self.bateria = min(100, energia+self.bateria)
    
    def autoconserto(self):
        self.saude = min(100, self.saude + 10)
        self.idade += 0.5
    
    def autodestruicao(self):
        self.saude = 0

    def passar_tempo(self):
        self.idade += 0.2
        self.saude -= randint(0, 5)
        self.bateria = max(0, self.bateria - randint(0, 5))

    def vida(self):
        if self.bateria < 50:
            self.saude -= 10
        elif self.bateria < 25:
            self.saude -= 15
        elif self.bateria < 10:
            self.saude -= 30
        elif self.bateria < 1:
            self.saude -= self.saude