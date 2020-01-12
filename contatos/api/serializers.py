from rest_framework import serializers
from contatos.models import Contato


class ConatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['id', 'nome', 'telefone', 'email']