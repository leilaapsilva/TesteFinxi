from rest_framework import generics
from .models import DemandaDePecas
from .serializers import DemandaSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class ListaDemandas(generics.ListCreateAPIView):

    queryset = DemandaDePecas.objects.all()
    serializer_class = DemandaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                            IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)