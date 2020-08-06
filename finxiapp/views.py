from rest_framework import generics
from .models import DemandaDePecas
from .serializers import DemandaSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404



# import pdb
# pdb.set_trace()

# Create your views here.
class ListaDemandas(generics.ListCreateAPIView):

    queryset = DemandaDePecas.objects.all()
    serializer_class = DemandaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                            IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        #Anunciante é o usuário logado na criação da Demanda
        serializer.save(user_anunciante=self.request.user)

class UpdateDemanda(generics.UpdateAPIView):
    queryset = DemandaDePecas.objects.all()
    serializer_class = DemandaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                            IsOwnerOrReadOnly]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = request.data.get("status")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


##################
class DemandaDetail(APIView):

    """
    Obter, atualizar ou deletar uma instância de Demanda de Produto
    """

    def get_object(self, pk):
        try:
            return DemandaDePecas.objects.get(pk=pk)
        except DemandaDePecas.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        demanda = self.get_object(pk)
        serializer = DemandaSerializer(demanda)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DemandaSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, pk, format=None):
    #     event = self.get_object(pk)
    #     serializer = EventSerializer(event, data=request.DATA)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        demanda = self.get_object(pk)
        demanda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        