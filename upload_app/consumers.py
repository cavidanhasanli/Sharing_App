import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .serializers import ReadOnlyCommentSerializers, CommentSerializers
from .models import Comment
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
        create = await self.create_comment(text_data)


    async def create_comment(self, event):

        events = json.loads(event)
        comment = await self._create_comment(events)

        comment_data = ReadOnlyCommentSerializers(comment).data
        await self.channel_layer.group_send(
            self.file_group_name,
            {
                'type': 'file.comment',
                'sender_file_id':events['sender_file'],
                'comment': events['comment']
            }
        )

    async def file_comment(self, event):

        message = event['comment']
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def _create_comment(self, content):

        sender_file = content.get('sender_file')

        Comment.objects.create(sender_file_id=sender_file,comment=comment)

