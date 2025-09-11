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
        parser.add_argument("--arquivo", default="population/autores.csv") # Aqui é definido o caminho padrão lido pelo csv caso o usuário não passe nenhum caminho
        parser.add_argument("--truncate", action="store_true") # O camando truncate significa que a tabela será totalmente apagada antes de adicionar o arquivo
        parser.add_argument("--update", action="store_true")
        parser.add_argument("--delete", action="store_true")

    @transaction.atomic
    def handle(self, *args, **o): # Adição da lógica de seu comando personalidado
        df = pd.read_csv(o["arquivo"], encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip('\ufeff') for c in df.columns]

        if o['truncate']: Author.objects.all().delete()

        df["nome"] = df["nome"].astype(str).str.strip()
        df["sobrenome"] = df["sobrenome"].astype(str).str.strip()
        df["data_nascimento"] = pd.to_datetime(df["data_nascimento"], errors="coerce", format="%Y-%m-%d").dt.date
        df["nacionalidade"] = df["nacionalidade"].astype(str).str.strip()

        df = df.query("nome !='' and sobrenome !='' ")
        df = df.dropna(subset=["data_nascimento"])

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
        else:
            objects = [Author(
                nome = r.nome,
                sobrenome = r.sobrenome,
                data_nascimento = r.data_nascimento,
                nacionalidade = r.nacionalidade
            ) for r in df.itertuples(index=False)]
            
            Author.objects.bulk_create(objects, ignore_conflicts=True)

            self.stdout.write(self.style.SUCCESS(f"Criados: {len(objects)}"))