import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import CustomUser
from generator.models import Variant


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
        elif '1' in user_data_json:
            user_variant = user_data_json["variant"]
            user_name_variant = self.scope["user"].first_name + ' ' + self.scope[
                "user"].last_name + ' / Вариант - ' + str(user_variant) + ' ' + 'FINISHED /'
            self.user_Data.pop(
                self.scope["user"].first_name + ' ' + self.scope["user"].last_name + ' / Вариант - ' + str(
                    user_variant) + '/')
            variant = Variant.objects.get(pk=user_variant)
            answers_true = variant.get_answers()
            answers_custom = {}
            result = 0
            user = CustomUser.objects.get(username=self.scope["user"].username)
            user.favorites.add(Variant.objects.get(pk=user_variant))
            for key in user_data_json:
                if len(key) < 3:
                    if user_data_json[key] == '':
                        user_data_json[key] = 'None'
            for key in answers_true:
                if user_data_json[key].strip() == answers_true[key].strip():
                    result += 1
                answers_custom[key] = answers_true[key] + ' --/-- ' + user_data_json[key]
            answers_custom["result"] = result
            self.user_Data[user_name_variant] = answers_custom
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
            user_name_variant = user_name + ' / Вариант - ' + str(user_variant) + '/'
            self.user_Data[user_name_variant] = {}
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
