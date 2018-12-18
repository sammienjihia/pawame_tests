from channels_api.bindings import ResourceBinding
from graphapp.serializers import GraphDataSerializer

class GraphDataBinding(ResourceBinding):
    serializer_class = GraphDataSerializer