from rest_framework.viewsets import ModelViewSet
from .serializers import ConatoSerializer
from contatos.models import Contato

class ContatoViewSet(ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ConatoSerializer