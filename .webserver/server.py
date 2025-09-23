import os
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

""" Aqui são definidas as variáveis globais, que servem como um 'banco de dados' simples. """

global usuarios_cadastrados
global filmes_cadastrados
usuarios_cadastrados = {1: {'user': 'Samuel', 'password': '1234'}}
filmes_cadastrados = {1 :{"title": "O Poderoso Chefão", "actors": "Marlon Brando, Al Pacino", "director": "Francis Coppola", "year": "1972", "genre": "Crime, Drama", "producer": "Albert S. Ruddy", "summary": "A saga da família mafiosa Corleone e seu patriarca, Vito Corleone."}}

"""A definição do handler personalizado é criado através de uma classe que herda o 'SimpleHTTPRequestHandler'.
O objetivo receber e processar as respostas de um evento específico que ocorre dentro do servidor."""

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
        """ Aqui é utilizada uma das formas possívels para abrir uma página dentro de um servidor, 
        o que muda aqui é somente o caminho inserido como parâmetro na função. """
        f = open(os.path.join(caminho), encoding='utf-8')
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(f.read().encode('utf-8'))

    def retornar_post_formulario(self):
        """ Função usada para ler e retornar o corpo do POST já decodificado."""
        content_length = int(self.headers['Content-length'])
        body = self.rfile.read(content_length).decode('utf-8')
        form_data = parse_qs(body)
        return form_data
    
    def gerar_arquivo_js(self, filmes_data, caminho_js="filmes.js"):
        """ Gera um arquivo JavaScript com base nos filmes cadastrados.
        Os dados são convertidos para JSON (mesma estrutura) 
        e utilizados no HTML através do script criado. """
        
        films_json = json.dumps(filmes_data, ensure_ascii=False)
        conteudo_js = f"const films_data = {films_json}; \n" \
                    "const length_films_data = Object.keys(films_data).length - 1; \n" \
                    "const cardFilm = document.getElementsByClassName('siteCardFilm'); \n" \
                    "for(let i = 0; i <= length_films_data; i++){ \n" \
                    "   let info_film = cardFilm[i].children; \n" \
                    "   info_film[0].innerHTML = 'Título: ' + films_data[i+1]['title'];\n" \
                    "   info_film[1].innerHTML = 'Atores: ' + films_data[i+1]['actors']; \n" \
                    "   info_film[2].innerHTML = 'Diretor: ' + films_data[i+1]['director'];  \n" \
                    "   info_film[3].innerHTML = 'Ano: ' + films_data[i+1]['year']; \n" \
                    "   info_film[4].innerHTML = 'Gênero: ' + films_data[i+1]['genre']; \n" \
                    "   info_film[5].innerHTML = 'Produtor: ' + films_data[i+1]['producer']; \n" \
                    "}"
        
        with open(caminho_js, "w", encoding="utf-8") as f:
            f.write(conteudo_js)

    def do_GET(self):
        try:    
            """ Esse bloco de código tem como objetivo 'renderizar' todas as páginas dentro do servidor, cada caminho indicado dentro das condições 
            é um caminho possível de ser feito dentro do site. Todas as páginas estão utilizando de uma função em comum para abrir as páginas. """

            if self.path == "/login":
                self.carregar_pagina('./login.html')   
            elif self.path == "/cadastro":
                self.carregar_pagina('./cadastro.html')
            elif self.path == "/filmes_cadastro":
                self.carregar_pagina('./filmes_cadastro.html')
            elif self.path == "/filmes_listagem":
                self.carregar_pagina('./filmes_listagem.html')
                self.gerar_arquivo_js(filmes_cadastrados)
            else:
                return super().do_GET()
        except FileNotFoundError:
            self.send_error(404, "File Not Found")
    
    def do_POST(self):
        """ Os dois metódos POST abaixo funcionam da mesma forma, recebendo informações dos formulário
        e realizando questões como autenticação e liberação. """
        if self.path == '/send_login':
            form_data = self.retornar_post_formulario()

            user_type = form_data.get('user', [""])[0]
            password_type = form_data.get('password', [""])[0]

            for user in usuarios_cadastrados.values():
                if user['user'] == user_type and user['password'] == password_type:
                    self.carregar_pagina("./filmes_listagem.html") # Carrega a página caso o usuário e senhas estiverem corretos
                    message = "<script>alert('Seja bem vindo!! Acesso permitido.')</script>" # Gera uma mensagem de 'error' caso as credencias estejam erradas
                    self.wfile.write(message.encode("utf-8"))
                    self.gerar_arquivo_js(filmes_cadastrados) # Ativa a função de criação do arquivo js, caso tenha filmes cadastrados, eles apareceram na tela
                else:
                    self.carregar_pagina("./login.html")
                    message = "<script>alert('Acesso negado!! Usuário ou senha incorretos.')</script>" # Gera uma mensagem de 'error' caso as credencias estejam erradas
                    self.wfile.write(message.encode("utf-8"))

        elif self.path == '/send_cadastro':
            form_data = self.retornar_post_formulario()

            user_type = form_data.get('user', [""])[0]
            password_type = form_data.get('password', [""])[0]
            confirm_password_type = form_data.get('confirmPassword', [""])[0]

            if password_type == confirm_password_type:
                user = {"user": user_type, "password": password_type}
                i = len(usuarios_cadastrados)
                usuarios_cadastrados[i+1] = user

                self.carregar_pagina('./login.html')
                message = "<script>alert('Usuário cadastrado com sucesso!')</script>"
                self.wfile.write(message.encode("utf-8"))

        elif self.path == "/send_cadastro_filmes":
            """ O cadastro de filmes se consiste em uma lógica bem simples, os dados
            são recolhidos do formulário e depois passados para um dinionário em python """
            form_data = self.retornar_post_formulario()

            title = form_data.get('title', [""])[0]
            actors = form_data.get('actor', [""])[0]
            director = form_data.get('director', [""])[0]
            year = form_data.get('year', [""])[0]
            genre = form_data.get('genre', [""])[0]
            producer = form_data.get('producer', [""])[0]
            summary = form_data.get('summary', [""])[0]

            film = {
                "title": title,
                "actors": actors,
                "director": director,
                "year": year,
                "genre": genre,
                "producer": producer,
                "summary": summary
            }
            
            i = len(filmes_cadastrados)
            filmes_cadastrados[i+1] = film

            self.carregar_pagina('./filmes_listagem.html')
            self.gerar_arquivo_js(filmes_cadastrados)  # Ativa a função de criação do arquivo js, caso tenha filmes cadastrados, eles apareceram na tela
            message = "<script>alert('Filme cadastrado com sucesso!')</script>"
            self.wfile.write(message.encode("utf-8"))
        
        else:
            super(MyHandle, self).do_POST()
            
 
def main():
    """Função para iniciar o servidor, recebe a porta que deve ser utilizada, ou seja , o endereço do servidor, e o handle personalidado criado na classe
    acima.
    """
    server_address = ('',8000)
    httpd = HTTPServer(server_address, MyHandle)
    print(f"Servidor rodando na porta http://localhost:{server_address[1]}") # Os colchetes no server_address é utilizado para pegar a porta indicada no código
    httpd.serve_forever()

main()