import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Publisher

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default="population/editoras.csv")
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")
        parser.add_argument("--delete", action="store_true")

    @transaction.atomic
    def handle(self, *args, **o):
        df = pd.read_csv(o["--arquivo"], encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip('\ufeff') for c in df.columns]

        if o["truncate"]:
            Publisher.objects.all().delete()

        df["nome"] = df["nome"].astype(str).str.strip()
        df["cnpj"] = df["cnpj"].astype(str).str.strip()
        df["telefone"] = df["telefone"].astype(str).str.strip()
        df["email"] = df["email"].astype(str).str.strip()
        df["site"] = df["site"].astype(str).str.strip()

        df.query("nome != ''")
        
        if o["update"]:
            criados = 0
            atualizados = 0

            for r in df.itertuples(index=False):
                _, created = Publisher.objects.update_or_create(
                    nome = r.nome
                    cnpj = r.cnpj
                    telefone = r.telefone
                    email = r.email
                    site = r.site
                )

            criados += int(created)
            atualizados += (not created)

            self.stdout.write(self.style(f"CRIADOS: {criados} | Atualizados: {atualizados}"))

        elif o["delete"]:
            Publisher.objects.all().delete()

        else:
            objects = [Publisher(
                nome = r.nome,
                cnpj = r.cnpj,
                telefone = r.telefone,
                email = r.email,
                site = r.site,
            ) for r in df.itertuples(index=False)]

            Publisher.objects.bulk_create(objects, ignore_conflicts=True)

            self.stdout.write(self.style.SUCCESS(f"Criados: {len(objects)}"))