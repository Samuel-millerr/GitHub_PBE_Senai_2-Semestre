import os
import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

"""A definição do handler personalizado é criado através de uma classe que herda o 'SimpleHTTPRequestHandler' e tem como objetivo final 
receber e processar as respostas de um evento específico que ocorre dentro do servidor.
"""

global usuarios_cadastrados
global filmes_cadastrados
usuarios_cadastrados = {1: {'user': 'Samuel', 'password': '1234'}}
filmes_cadastrados = {}

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
    
    def do_POST(self):

        if self.path == '/send_login':
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            user_type = form_data.get('user', [""])[0]
            password_type = form_data.get('password', [""])[0]

            if len(usuarios_cadastrados) <= 0:
                self.carregar_pagina("./login.html")
                message = "<script>alert('Nenhum usuário foi cadastrado ainda!')</script>" # Gera uma mensagem de 'error' caso as credencias estejam erradas
                self.wfile.write(message.encode("utf-8"))
            else:
                for user in usuarios_cadastrados.values():
                    if user['user'] == user_type and user['password'] == password_type:
                        self.carregar_pagina("./filmes_listagem.html") # Carrega a página caso o usuário e senhas estiverem corretos
                    else:
                        self.carregar_pagina("./login.html")
                        message = "<script>alert('Acesso negado!! Usuário ou senha incorretos.')</script>" # Gera uma mensagem de 'error' caso as credencias estejam erradas
                        self.wfile.write(message.encode("utf-8"))
            print(usuarios_cadastrados)

        elif self.path == '/send_cadastro':
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            user_type = form_data.get('user', [""])[0]
            password_type = form_data.get('password', [""])[0]
            confirm_password_type = form_data.get('confirmPassword', [""])[0]

            if password_type == confirm_password_type:
                user = {"user": user_type, "password": password_type}
                i = len(usuarios_cadastrados)
                usuarios_cadastrados[i+1] = user

                self.carregar_pagina('./cadastro.html')
                message = "<script>alert('Usuário cadastrado com sucesso!')</script>"
                self.wfile.write(message.encode("utf-8"))

        elif self.path == "/send_cadastro_filmes":
            print("teste")
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            title = form_data.get('title')
            actors = form_data.get('actor')
            director = form_data.get('director')
            year = form_data.get('year')
            genre = form_data.get('genre')
            producer = form_data.get('producer')
            summary = form_data.get('summary')

            film = {
                "title": title[0],
                "actors": actors,
                "director": director[0],
                "year": year[0],
                "genre": genre[0],
                "producer": producer[0],
                "summary": summary[0]
            }
            
            i = len(filmes_cadastrados)
            filmes_cadastrados[i+1] = film
            
            self.carregar_pagina('./filmes_listagem.html')
            message = "<script>alert('Filme cadastrado com sucesso!')</script>"
            self.wfile.write(message.encode("utf-8"))
        
        else:
            super(MyHandle, self).do_POST()
            
 
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
