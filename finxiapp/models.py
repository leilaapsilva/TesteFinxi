from django.db import models
from django.contrib.auth.models import User 

#from django.core.exceptions import ValidationError
#from django.utils.translation import gettext_lazy as _

MAX_LENGTH = 200 # Constante que define o tamanho máximo padrão dos campos de texto

class Administrador(models.Model):
    user = models.OneToOneField(User, related_name="administrador", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Anunciante(models.Model):    
    user = models.OneToOneField(User, related_name="anunciante", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username 

#def valida_telefone(tel): #exemplo
    # if value % 2 != 0:
    #         raise ValidationError(
    #             _('%(value)s is not an even number'),
    #             params={'value': value},
    #         )

# https://docs.djangoproject.com/en/3.0/ref/validators/

class DemandaDePecas(models.Model):
    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    contato_email = models.EmailField(max_length=200, verbose_name="Email de contato") #email/telefone
    contato_telefone = models.CharField(max_length=50, verbose_name="Telefone")
    anunciante = models.ForeignKey(Anunciante, on_delete=models.CASCADE, null=True)
    anunciante2 = models.ForeignKey('auth.User', related_name='demanda', on_delete=models.CASCADE, null=True)
    status = models.BooleanField() #aberta 0/finalizada 1   
    endereco_rua = models.CharField(max_length=MAX_LENGTH, verbose_name="Rua", null=True)
    endereco_numero = models.CharField(max_length=10, verbose_name="Número", null=True)
    endereco_complemento = models.CharField(max_length=MAX_LENGTH, verbose_name="Complemento", null=True)
    endereco_bairro = models.CharField(max_length=MAX_LENGTH, verbose_name="Bairro", null=True)
    endereco_cidade = models.CharField(max_length=MAX_LENGTH, verbose_name="Cidade", null=True)
    endereco_estado = models.CharField(max_length=2, verbose_name="Estado", null=True) # (Sigla)

    def __str__(self):
        return self.descricao 