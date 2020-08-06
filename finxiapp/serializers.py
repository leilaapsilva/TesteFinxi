from rest_framework import serializers 
from .models import DemandaDePecas 
from django.contrib.auth.models import User 

#class UserSerializer(serializers.ModelSerializer):


class DemandaSerializer(serializers.ModelSerializer):
    
    user_anunciante = serializers.StringRelatedField()
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = DemandaDePecas
        fields = '__all__' 

    def create(self, validated_data):
        return DemandaDePecas.objects.create(**validated_data)     