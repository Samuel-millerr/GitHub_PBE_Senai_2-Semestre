import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

"""A definição do handler personalizado é criado através de uma classe que herda o 'SimpleHTTPRequestHandler' e tem como objetivo final 
receber e processar as respostas de um evento específico que ocorre dentro do servidor.
"""
class MyHandle(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            f = open(os.path.join(path, 'index.html'), encoding='utf-8')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f.read().encode('utf-8'))
            f.close()
            return None
        except FileNotFoundError:
            pass 
        return super().list_directory(path)

    def carregar_pagina(self, caminho):
        """ Aqui é utilizada uma das formas possívels para abrir uma página dentro de um servidor, o que muda aqui é somente o caminho inserido como 
        parâmetro na função.
        """
        f = open(os.path.join(caminho), encoding='utf-8')
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(f.read().encode('utf-8'))

    def do_GET(self):
        try:    
            """ Esse bloco de código tem como objetivo 'renderizar' todas as páginas dentro do servidor, cada caminho indicado dentro das condições 
            é um caminho possível de ser feito dentro do site. Todas as páginas estão utilizando de uma função em comum para abrir as páginas.
            """
            if self.path == "/login":
                self.carregar_pagina('./login.html')   
            elif self.path == "/cadastro":
                self.carregar_pagina('./cadastro.html')
            elif self.path == "/filmes_cadastro":
                self.carregar_pagina('./filmes_cadastro.html')
            elif self.path == "/filmes_listagem":
                self.carregar_pagina('./filmes_listagem.html')
            else:
                return super().do_GET()
        except FileNotFoundError:
            self.send_error(404, "File Not Found")

def main():
    """Função para iniciar o servidor, recebe a porta que deve ser utilizada, ou seja , o endereço do servidor, e o handle personalidado criado na classe
    acima.
    """
    server_address = ('',8001)
    httpd = HTTPServer(server_address, MyHandle)
    print(f"Servidor rodando na porta http://localhost:{server_address[1]}") # Os colchetes no server_address é utilizado para pegar a porta indicada no código
    httpd.serve_forever()

main()

# Primeiro exemplo de criação de servidor
# Definido a porta 
# port = 8000

# Definindo o gerenciador/manipular de requisições
# handler = SimpleHTTPRequestHandler

# Criando a instancia do servidor
# server = HTTPServer(('localhost', port), MyHandle.list_directory)

# print(f"Server Runing in http://localhost:{port}")

# server.serve_forever()
