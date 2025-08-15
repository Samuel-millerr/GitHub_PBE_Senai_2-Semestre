class Veiculo():
    def __init__(self, marca: str, modelo: str, ano_fabricacao: int, cor: str, qtd_portas: str):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.cor = cor
        self.qtd_portas = qtd_portas

    def andar_com_veiculo(self):
        return f"Você está andando com um(a) {self.__class__.__name__} do modelo {self.modelo}"
    
    def parar_com_veiculo(self, km):
        return f"Você parou de andar com o(a) {self.__class__.__name__}, você andou por {km}km"
    
    def imprimir(self, veiculo):
        for keys, values in veiculo.__dict__.items():
            print(f"{keys}: {values}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, cor, qtd_bancos, qtd_portas: int = 4):
        super().__init__(marca, modelo, ano_fabricacao, cor, qtd_portas)
        self.qtd_bancos = qtd_bancos

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, cor, empina: bool = False, qtd_portas: int= 0):
        super().__init__(marca, modelo, ano_fabricacao, cor, qtd_portas)
        self.empina = empina

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, cor, qtd_carga_maxima: float, qtd_portas: int = 2):
        super().__init__(marca, modelo, ano_fabricacao, cor, qtd_portas)
        self.qtd_carga_maxima = qtd_carga_maxima

def main(decisao):
    if decisao == "1":
        carro = Carro("Honda", "Civic", 1992, "Preto", 5)
        carro.imprimir(carro)
        print(carro.andar_com_veiculo())
        print(carro.parar_com_veiculo(30))
    elif decisao == "2":
        moto = Moto("Honda", "Biz", 1998, "Vermelha", False)
        moto.imprimir(moto)
        print(moto.andar_com_veiculo())
        print(moto.parar_com_veiculo(200))
    elif decisao == "3":
        caminhao = Caminhao("Scania", "R450", 2019, "Cinza", 234)
        caminhao.imprimir(caminhao)
        print(caminhao.andar_com_veiculo())
        print(caminhao.parar_com_veiculo(560))

while True:
    print("\nDigite qual veículo você gostaria de ver as informações: ")
    print("[ 1 ] Carro\n[ 2 ] Moto\n[ 3 ] Caminhão\n[ 0 ] Sair")
    decisao = input()
    if  decisao == "0":
        break
    main(decisao)

