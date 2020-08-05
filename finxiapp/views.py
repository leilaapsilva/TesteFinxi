from rest_framework import generics
from .models import DemandaDePecas
from .serializers import DemandaSerializer

# Create your views here.
class ListaDemandas(generics.ListCreateAPIView):

    queryset = DemandaDePecas.objects.all()
    serializer_class = DemandaSerializer