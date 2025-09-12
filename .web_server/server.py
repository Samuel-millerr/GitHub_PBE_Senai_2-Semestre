import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

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

    # Função utilizada para redução de código, tem como objetivo realizar o carregamento de todas as páginas localizadas dentro do projeto
    def carregar_pagina(self, caminho):
        f = open(os.path.join(caminho), encoding='utf-8')
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(f.read().encode('utf-8'))

    def do_GET(self):
        try:    
            if self.path == "/login":
                self.carregar_pagina('login.html')
                # if self.path == "/login?user=samuel&password=1234":
                #     self.carregar_pagina('index.html')     
            elif self.path == "/cadastro":
                self.carregar_pagina('cadastro.html')
            elif self.path == "/listar_filmes":
                self.carregar_pagina('listar_filmes.html')
            else:
                return super().do_GET()
        except FileNotFoundError:
            self.send_error(404, "File Not Found")

def main():
    server_address = ('',8000)
    httpd = HTTPServer(server_address, MyHandle)
    print(f"Servidor rodando na porta http://localhost:{server_address[1]}")
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
