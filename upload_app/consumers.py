import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .serializers import ReadOnlyCommentSerializers,CommentSerializers
import asyncio

class FileConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.file_name = self.scope['url_route']['kwargs']['file_name']
        self.file_group_name = 'self.file_name'

        await self.channel_layer.group_add(
            self.file_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        
        await self.channel_layer.group_discard(
            self.file_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.file_group_name,
            {
                'type': 'file.comment',
                'message': message
            }
        )


    async def create_comment(self, event):
        comment = await self._create_comment(event.get('data'))
        comment_id = f'{comment.id}'
        comment_data = ReadOnlyCommentSerializers(comment).data

        await self.channel_layer.group_send(
            self.file_group_name,
            {
                'type': 'file.comment',
                'comment_data': comment_data
            }
        )

    async def file_comment(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
        'message': message
        }))

    @database_sync_to_async
    def _create_comment(self, content):
        serializer = CommentSerializers(data=content)
        serializer.is_valid(raise_exception=True)
        comment = serializer.create(serializer.validated_data)
        return comment