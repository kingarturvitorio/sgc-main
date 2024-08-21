from django.db import models

# Create your models here.
class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    documento = models.CharField(max_length=100)
    carteirinha = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone_responsavel = models.CharField(max_length=100)
    telefone_contato = models.CharField(max_length=100)
    telefone_emergencia = models.CharField(max_length=100)
    tipo_convenio = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=False, blank=False)
    nome_responsavel = models.CharField(max_length=100)
    documento_responsavel = models.CharField(max_length=100)
    foto_carteirinha = models.ImageField(upload_to='documentos_pacientes/', blank=True, null=True)

    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return self.nome