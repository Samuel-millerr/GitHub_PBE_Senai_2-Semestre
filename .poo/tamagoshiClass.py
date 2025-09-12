class Tamagoshi():
    def __init__(self, nome, idade: float, fome: int, saude: int, tedio: int):
        self.nome = nome
        self.idade = 0
        self.fome = 0
        self.saude = 100
        self.tedio = 0

    def info_tamagoshi(self, tamagoshi):
        for key, value in tamagoshi.__dict__.items():
            if type(value) == float:
                print(f"{key}: {value:.1f}")
            else:
                print(f"{key}: {value}")

    def alimentar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome = max(0, self.fome - quantidade)
        else: print("O máximo de comida que pode ser dado para o tamagoshi é de 100.")
        
    def brincar(self, tempo):
        if (tempo >= 0) and (tempo <= 100):
            self.tedio = max(0, self.tedio - tempo)
        else:
            print("O máximo de tempo que você pode brincar com o tamagoshi é de 0 a 100.")
            
    def getHumor(self):
        humor = max(0, 100 - ((self.saude + self.tedio)/2.75))
        return f"{humor:.2f}"
    
    def vida(self):
        if (self.fome > 50 and self.fome <= 60) or (self.tedio > 50 and self.tedio <=60):
            self.saude = max(self.saude -self.saude, self.saude - 10)
        elif (self.fome > 60 and self.fome <= 80) or (self.tedio > 60 and self.tedio <=80):
            self.saude = max(self.saude - self.saude, self.saude - 15)
        elif (self.fome > 80 and self.fome <=90) or (self.tedio > 80 and self.tedio <=90):
            self.saude = (self.saude - self.saude, self.saude - 30)
        elif (self.fome > 90) or (self.tedio > 90):
            pass
        elif (self.fome > 99) or (self.tedio > 99):
            self.saude = 0 
            return  0
             
    def passar_tempo(self):
        self.idade += 0.2
        self.tedio = min(100, self.fome + 2.5)
        self.fome = min(100, self.fome + 3.5)
    
    @classmethod
    def criar_tamagoshi(cls, nome):
        return cls(nome)
    
