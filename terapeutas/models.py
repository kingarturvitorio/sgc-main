from django.db import models

# Create your models here.

class Terapeuta(models.Model):
    nome_terapeuta = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    titulo_profissional = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    acordo = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    registro_classe = models.CharField(max_length=100)
    conselho_classe = models.CharField(max_length=100)
    dados_bancarios = models.CharField(max_length=100)
    documentos = models.ImageField(upload_to='documentos_terapeuta/', blank=True, null=True)
    outros = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['nome_terapeuta']
    
    def __str__(self):
        return self.nome_terapeuta