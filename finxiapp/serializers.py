from rest_framework import serializers 
from .models import DemandaDePecas 
from django.contrib.auth.models import User 

#class UserSerializer(serializers.ModelSerializer):


class DemandaSerializer(serializers.ModelSerializer):
    
    anunciante2 = serializers.StringRelatedField(many=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = DemandaDePecas
        fields = '__all__' 