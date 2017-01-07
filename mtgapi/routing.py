from channels.routing import route, include

from mtgapp.consumers import game_connect, game_disconnect

game_routing = [
    route("websocket.connect", game_connect, path=r'^/(?P<game_id>[a-zA-Z0-9_]+)/$'),
    route("websocket.disconnect", game_disconnect),
    route('websocket.receive', 'mtgapp.consumers.ws_consumer'),
]

routing = [
    include(game_routing, path=r'^/game'),
]
