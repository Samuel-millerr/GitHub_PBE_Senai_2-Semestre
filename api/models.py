from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255, null=False)
    sobrenome = models.CharField(max_length=255, null=False)
    data_nascimento = models.DateField(null=True, blank=True)
    nacionalidade = models.CharField(max_length=255)
    biografia = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
class Livro(models.Model):
    titulo = models.CharField(max_length=255)   
    qtdPaginas = models.CharField(max_length=255)
    disponivel = models.BooleanField(null=False, blank=True)

