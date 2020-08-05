from django.db import models
from django.contrib.auth.models import User 

class Administrador(models.Model):
    user = models.OneToOneField(User, related_name="administrador", on_delete=models.CASCADE)

class Anunciante(models.Model):    
    user = models.OneToOneField(User, related_name="anunciante", on_delete=models.CASCADE)

class DemandaDePecas(models.Model):

    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    endereco_entrega = models.CharField(max_length=200, verbose_name="Endereço de entrega")
    contato_email = models.CharField(max_length=200, verbose_name="Email de contato") #email/telefone
    contato_telefone = models.CharField(max_length=50, verbose_name="Telefone")
    anunciante = models.ForeignKey(Anunciante, on_delete=models.CASCADE, null=True)
    status = models.BooleanField() #aberta 0/finalizada 1   

    def __str__(self):
        return self.descricao 

