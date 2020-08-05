from rest_framework import serializers 
from .models import DemandaDePecas 

class DemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandaDePecas
        fields = '__all__' 