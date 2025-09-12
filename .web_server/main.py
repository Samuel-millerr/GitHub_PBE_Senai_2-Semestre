import requests

def get_address(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['logradouro']
    else:
        return {"error": "endereço não encontrado"}
    
cep = input("Digite algum cep: ")
print(get_address(cep))