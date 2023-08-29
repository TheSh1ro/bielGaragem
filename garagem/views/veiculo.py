from rest_framework.viewsets import ModelViewSet

from garagem.models import Acessorio, Categoria, Cor, Marca, Modelo, Veiculo
from garagem.serializers import (
    AcessorioSerializer,
    CategoriaSerializer,
    CorSerializer,
    MarcaSerializer,
    ModeloSerializer,
    VeiculoDetailSerializer,
    VeiculoListSerializer,
    VeiculoSerializer,
)


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer
