import logging

from socketio import namespace, mixins
from socketio.sdjango import namespace as django_namespace


@django_namespace('/deck')
class DeckNamespace(namespace.BaseNamespace, mixins.RoomsMixin, mixins.BroadcastMixin):
    def __init__(self, *args, **kwargs):
        super(DeckNamespace, self).__init__(*args, **kwargs)
        if 'decks' not in self.session:
            self.session['decks'] = set()  # a set of simple strings

    def initialize(self):
        self.logger = logging.getLogger("socketio.deck")
        self.log("Socket.io deck session started")

    def log(self, message):
        print '[{0}] {1}'.format(self.socket.sessid, message)

    def join(self, deck_id):
        self.log('Joining deck: {}'.format(deck_id))
        self.session['decks'].add(self._get_room_name(deck_id))

    def on_join(self, deck_id):
        self.deck_id = deck_id
        self.join(deck_id)
        return True

    def on_deck_update(self, deck_id):
        self.log('Deck update: {0}'.format(deck_id))
        self.broadcast_event('deck_update', deck_id)
        return True

    def emit_to_deck(self, deck_id, event, *args):
        pkt = dict(type="event",
                   name=event,
                   args=args,
                   endpoint=self.ns_name)
        deck_name = self._get_room_name(deck_id)
        for sessid, socket in self.socket.server.sockets.iteritems():
            if 'decks' not in socket.session:
                continue
            if deck_name in socket.session['decks'] and self.socket != socket:
                socket.send_packet(pkt)

    def _get_room_name(self, deck_id):
        return '{}_{}'.format(self.ns_name, deck_id)
