# consumers.py

import json
from channels.generic.websocket import WebsocketConsumer
from .external_api import get_live_data

class MapConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def send_live_data(self, event):
        data = event['data']
        self.send(text_data=json.dumps(data))

