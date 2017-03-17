from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated

from communications.permissions import IsChatParticipant
from .models import Chat, Message
from core.api import UserSerializer
from core.models import User
from application.api import router


class MessageSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    def create(self, validated_data):
        message = Message.objects.create(author_id=self.context['request'].user.id, **validated_data)
        return message

    class Meta:
        fields = ('content', 'author', 'chat')
        model = Message


class ChatSerializer(serializers.ModelSerializer):

    users = UserSerializer(many=True, context={'request': None})

    class Meta:
        fields = ('pk', 'users')
        model = Chat


class ChatCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        chat = Chat.objects.create(author_id=self.context['request'].user.id)
        chat.save()

        for user_id in validated_data['users']:
            chat.users.add(user_id)
        chat.users.add(self.context['request'].user.id)
        return chat

    def update(self, instance, validated_data):

        for user in instance.users.all():
            if user.id not in validated_data['users']:
                instance.users.remove(user.id)

        for user_id in validated_data['users']:
            if user_id not in instance.users.all():
                instance.users.add(user_id)
        return instance

    class Meta:
        fields = ('users',)
        model = Chat


class ChatViewSet(viewsets.ModelViewSet):

    serializer_class = ChatSerializer

    def get_serializer_class(self):
        serializer_class = super(ChatViewSet, self).get_serializer_class()
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return ChatCreateSerializer
        else:
            return serializer_class

    def get_queryset(self):
        return Chat.objects.all().filter(users=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):

    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [IsChatParticipant,
                          IsAuthenticated,
                          ]

    def get_queryset(self):
        qs = super(MessageViewSet, self).get_queryset()
        qs = qs.filter(chat__users=self.request.user)
        return qs


router.register('chat', ChatViewSet, 'chat')
router.register('message', MessageViewSet, 'message')