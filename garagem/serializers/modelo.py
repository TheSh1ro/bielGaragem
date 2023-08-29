from rest_framework.serializers import ModelSerializer

from garagem.models import Acessorio, Categoria, Cor, Marca, Modelo, Veiculo


class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"
