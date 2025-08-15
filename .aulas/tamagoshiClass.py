class Tamagoshi():
    def __init__(self, nome, idade: float, fome: int, saude: int, tedio: int, vies_politico: str):
        self.nome = nome
        self.idade = 0
        self.fome = 0
        self.saude = 100
        self.tedio = 0
        self.vies_politico = vies_politico

    def info_tamagoshi(self, tamagoshi):
        for key, value in tamagoshi.__dict__.items():
            print(f"{key}: {value}")
            
    def alimentar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade /100)
        
    def brincar(self, tempo):
        if (tempo >= 0) and (tempo <= 100):
            self.tedio -= self.tedio * (tempo /100)

    def getHumor(self):
        return 100 - ((self.nome + self.tedio)/2)
    
    def vida(self):
        if (self.fome > 50 and self.fome <= 60) or (self.tedio > 50 and self.tedio <=60):
            self.saude -= 10
        elif (self.fome > 60 and self.fome <= 80) or (self.tedio > 60 and self.tedio <=80):
            self.saude -= 15
        elif (self.fome > 80 and self.fome <=90) or (self.tedio > 80 and self.tedio <=90):
            self.saude -= 30
        elif (self.fome > 90) or (self.tedio > 90):
            print("TO MORENDOOOOOOOOOOOOOOOOOO...... AHHHHHHH")
        elif (self.fome > 99) or (self.tedio > 99):
            self.saude = 0
            print("Seu bichinho foi de vasco T_T")
             
    def passar_tempo(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5