import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Author

class Command(BaseCommand): # Definição de um novo comando personalizado do django
    def add_arguments(self, parser): # Adiciona argumentos que podem ser utilizados em seu comando personalizado
        """ Aqui é onde é definido os argumentos necessários para o uso do comando, cada argumento pode conter certas propriedades
        específicas, como `default`, que define um valor padrão ao argumento caso o usuário passe nenhum valor. 
        No caso de argumentos com o parâmetro `action`, eles se comportam como flags booleanas: se o usuário passar a flag no terminal, 
        o valor será True, se não passar, será False, o que indica dentro da lógica do comando qual o tipo que deve ser utilizado.
        O parâmetro `action="store_true"` garante exatamente isso, permitindo que a lógica construída no código utilize 
        esse valor para decidir qual ação executar.
        """

        # Na linha abaixo é definido o caminho padrão lido pelo csv caso o usuário não passe nenhum caminho
        parser.add_argument("--arquivo", default="population/autores.csv") 
        
        # Na linha abaixo comando truncate significa que a tabela será totalmente apagada antes de adicionar o arquivo
        parser.add_argument("--truncate", action="store_true") 
        
        # Na linha abaixo é desiginado o comando de atualização da tabela, sem nenhuma eliminação dos antigos dados específica
        parser.add_argument("--update", action="store_true")

        # Na linha de baixo é designado o camando de eliminação dos dados do banco
        parser.add_argument("--delete", action="store_true")

        """ A parte de adicionar argumentos permite em suma na criação de parametros relacionados aos comandos 
        personalizados, pode ser tanto que será utilizado dentro de seu comando ou até mesmo uma remificação do mesmo
        """

    @transaction.atomic # Aqui mantém o comando como uma forma atomica, ou seja, ou todo comando funciona, ou nada funciona
    def handle(self, *args, **o): # Adição da lógica de seu comando personalidado
        df = pd.read_csv(o["arquivo"], encoding="utf-8-sig") 
        """
        Na parte o comando acima o o["arquivo"] indica o caminho do csv caso o usuário não passe esse parametro no 
        terminal.
        Já o enconding garante que o csv seja lido no esquema de texto brasileiro.
        """
        df.columns = [c.strip().lower().lstrip('\ufeff') for c in df.columns]
        """
        O comando acima tem como objetivo formatar todos os titulos do csv.
        strip() - remove os espaços extra
        strip() - deixa tudo em minusculo
        lstrip() - remove todos os caracteres indesejados
        """

        if o["truncate"]: # Caso o comando digitado no terminal for truncate ele apagara todos os dados do
                          # banco antes de adicionar os novos.
            Author.objects.all().delete()
        
        # As seleções abaixo garantem a  formatação de todos os dados da tabela, os formatando por colunas
        df["nome"] = df["nome"].astype(str).str.strip()
        df["sobrenome"] = df["sobrenome"].astype(str).str.strip()
        df["data_nascimento"] = pd.to_datetime(df["data_nascimento"], errors="coerce", format="%Y-%m-%d").dt.date
        df["nacionalidade"] = df["nacionalidade"].astype(str).str.strip()

        df = df.query("nome !='' and sobrenome !='' ") # Um filtro interno do banco que garante que nãoo sejam passados campos que estejam vazios
        df = df.dropna(subset=["data_nascimento"]) # O comando dropna apaga as linhas que contem nulo armazenado no campo "data_nascimento"

        if o["update"]:
            criados = 0
            atualizados = 0

            for r in df.itertuples(index=False):
                _, created = Author.objects.update_or_create(
                    nome = r.nome,
                    sobrenome = r.sobrenome,
                    data_nascimento = r.data_nascimento,
                    defaults={"nacionalidade": r.nacionalidade}
                )

                criados += int(created)
                atualizados += (not created)
            self.stdout.write(self.style.SUCCESS(f"Criados: {criados} | Atualizados: {atualizados}"))
        elif o["delete"]:
            Author.objects.all().delete()
        else:
            objects = [Author(
                nome = r.nome,
                sobrenome = r.sobrenome,
                data_nascimento = r.data_nascimento,
                nacionalidade = r.nacionalidade
            ) for r in df.itertuples(index=False)]
            
            Author.objects.bulk_create(objects, ignore_conflicts=True)

            self.stdout.write(self.style.SUCCESS(f"Criados: {len(objects)}"))