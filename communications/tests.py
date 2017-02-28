from django.test import TestCase

from .models import Message, Chat
from core.models import User


class ChatTestCase(TestCase):

    def setUp(self):
        self.test_users = [User.objects.create(username='test{}'.format(i)) for i in range(3)]

    def test_chat_create(self):
        self.chat = Chat(author_id=1)
        self.chat.users.add(*self.test_users)
        self.chat.save()
        assert Chat.objects.get(pk=self.chat.pk) is not None

    def test_message_test(self):
        msg = Message.objects.create(content='test_message', author_id=self.test_users[0].pk, chat=self.chat)
        assert Message.objects.get(pk=msg.pk) is not None

    def test_chat_delete(self):
        self.chat.delete()
        assert Chat.objects.get(pk=self.chat.pk) is None

    def tearDown(self):
        pass
