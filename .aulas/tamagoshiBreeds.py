from tamagoshiClass import Tamagoshi

class TamagoshiSindical(Tamagoshi):
    def __init__(self, nome, vies_politico: str = "Esquerda", idade: float = 0, fome: int = 0, saude: int = 90, tedio: int = 0):
        super().__init__(nome, idade, fome, saude, tedio, vies_politico)

class TamagoshiNulo(Tamagoshi):
    def __init__(self, nome, vies_politico: str = "Centro", idade: float = 0, fome: int = 0, saude: int = 100, tedio: int = 0):
        super().__init__(nome, idade, fome, saude, tedio, vies_politico)
    
class TamagoshiReacionario(Tamagoshi):
    def __init__(self, nome, vies_politico: str = "Direita", idade: float = 0, fome: int = 0, saude: int = 90, tedio: int = 0):
        super().__init__(nome, idade, fome, saude, tedio, vies_politico)