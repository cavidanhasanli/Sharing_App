from rest_framework import serializers
from upload_app.models import Comment


class ReadOnlyCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'