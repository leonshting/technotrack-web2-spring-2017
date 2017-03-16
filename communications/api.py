from rest_framework import viewsets, serializers

from communications.permissions import IsChatParticipant
from .models import Chat, Message
from core.api import UserSerializer
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
            print(user_id)
            chat.users.add(user_id)
        chat.users.add(self.context['request'].user.id)
        return chat

    class Meta:
        fields = ('users',)
        model = Chat


class ChatViewSet(viewsets.ModelViewSet):

    serializer_class = ChatSerializer

    def get_serializer_class(self):
        serializer_class = super(ChatViewSet, self).get_serializer_class()
        if self.request.method == 'POST':
            return ChatCreateSerializer
        else:
            return serializer_class

    def get_queryset(self):
        return Chat.objects.all().filter(users=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):

    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [IsChatParticipant,
                          ]

    def get_queryset(self):
        qs = super(MessageViewSet, self).get_queryset()
        qs = qs.filter(chat__users=self.request.user)
        return qs


router.register('chat', ChatViewSet, 'chat')
router.register('message', MessageViewSet, 'message')