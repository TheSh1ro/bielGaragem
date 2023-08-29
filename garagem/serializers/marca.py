from rest_framework.serializers import ModelSerializer

from garagem.models import Acessorio, Categoria, Cor, Marca, Modelo, Veiculo


class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"
