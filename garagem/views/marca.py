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


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
