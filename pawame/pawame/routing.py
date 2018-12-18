from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class

from graphapp.bindings import GraphDataBinding

class APIDemultiplexer(WebsocketDemultiplexer):

    consumers = {
      'graph_data': GraphDataBinding.consumer
    }

channel_routing = [
    route_class(APIDemultiplexer)
]