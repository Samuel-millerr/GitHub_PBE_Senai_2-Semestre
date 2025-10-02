import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Book, Publisher, Author

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados de um arquivo CSV usando Pandas.'

    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default="population/livros.csv")
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")
        parser.add_argument("--delete", action="store_true")

    @transaction.atomic
    def handle(self, *args, **o):
        df = pd.read_csv(o["arquivo"], encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]

        self.stdout.write(f"Colunas encontradas no CSV: {list(df.columns)}")
        
        if o["truncate"]:
            Book.objects.all().delete()

        df["titulo"] = df["titulo"].astype(str).str.strip()
        df["subtitulo"] = df["subtitulo"].astype(str).str.strip()
        df["autor"] = df["autor"].astype(int)
        df["editora"] = df["editora"].astype(int)
        df["descricao"] = df["descricao"].astype(str).str.strip()
        df["idioma"] = df["idioma"].astype(str).str.strip()
        df["ano_publicacao"] = df["ano_publicacao"].astype(int)
        df["paginas"] = df["paginas"].astype(int)
        df["preco"] = df["preco"].astype(float)
        df["estoque"] = df["estoque"].astype(int)
        df["desconto"] = df["desconto"].astype(float)
        df["disponivel"] = df["disponivel"].astype(bool)
        df["dimensoes"] = df["dimensoes"].astype(str).str.strip()
        df["peso"] = df["peso"].astype(float)

        df = df.query("titulo != '' ")

        if["update"]:
            criados = 0
            atualizados = 0

            for r in df.itertuples(index=False):
                """ Essas váriaveis são criadas para garantir que esteja sendo passado um objeto em si, pois o django espera como base na hora de inserir os dados
                na tabela, um id específico e não necessáriamente um int como no caso dos outros valores """
                autor_obj = Author.objects.get(id=r.autor)
                editora_obj = Publisher.objects.get(id=r.editora)
                _, created = Book.objects.update_or_create(
                    titulo = r.titulo,
                    subtitulo = r.subtitulo,
                    autor = autor_obj,
                    editora = editora_obj,
                    isbn = r.isbn,
                    descricao = r.descricao,
                    idioma = r.idioma,
                    ano_publicacao = r.ano_publicacao,
                    paginas = r.paginas,
                    preco = r.preco,
                    estoque = r.estoque,
                    desconto = r.desconto,
                    disponivel = r.disponivel,
                    dimensoes = r.dimensoes,
                    peso = r.peso
                )

                criados += int(created)
                atualizados += (not created)

            self.stdout.write(self.style.SUCCESS(f"Criados: {criados} | Atualizados: {atualizados}"))

        elif o["delete"]:
            Book.objects.all().delete()

        else:
            objects = []

            for r in df.itertuples(index=False):
                autor_obj = Author.objects.get(id=r.autor)
                editora_obj = Publisher.objects.get(id=r.editora)
                objects.append(Book(
                    titulo=r.titulo,
                    subtitulo=r.subtitulo,
                    autor=autor_obj,
                    editora=editora_obj,
                    isbn=r.isbn,
                    descricao=r.descricao,
                    idioma=r.idioma,
                    ano=r.ano_publicacao,
                    paginas=r.paginas,
                    preco=r.preco,
                    estoque=r.estoque,
                    desconto=r.desconto,
                    disponivel=r.disponivel,
                    dimensoes=r.dimensoes,
                    peso=r.peso
                ))

            Book.objects.bulk_create(objects, ignore_conflicts=True)

            self.stdout.write(self.style.SUCCESS(f"Criados: {len(objects)}"))