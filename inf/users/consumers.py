import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import CustomUser


class AdminConsumer(WebsocketConsumer):
    user_Data = {}

    def connect(self):
        self.room_group_name = "index"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        self.user_Data.pop(self.scope["user"].first_name + ' ' + self.scope["user"].last_name, "Ничего страшного")
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        user_data_json = json.loads(text_data)
        if "return_dict" in user_data_json:
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {"type": "chat_message", "data": self.user_Data}
            )
        else:
            user = CustomUser.objects.get(username=self.scope["user"].username)
            user_first_name = user.first_name
            user_last_name = user.last_name
            user_name = user_first_name + ' ' + user_last_name
            user_variant = user_data_json["variant"]
            self.user_Data[user_name] = user_variant
            user_data = {"username": user_name, "variant": user_variant}
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {"type": "chat_message", "data": self.user_Data}
            )

    def chat_message(self, event):
        # user_variant = event["data"]["variant"]
        # user_name = event["data"]["username"]
        # user_data = {"username": user_name, "variant": user_variant}
        self.send(text_data=json.dumps({
            'event': "Send", "data": self.user_Data
        }))
