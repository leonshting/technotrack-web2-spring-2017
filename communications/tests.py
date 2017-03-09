from django.test import TestCase

from .models import Message, Chat
from core.models import User

class ChatTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_users = [User(username='test{}'.format(i)) for i in range(3)]
        for user in cls.test_users:
            user.save()
        cls.chat = Chat(author_id=1, pk=1)
        cls.chat.save()
        Chat.objects.get(pk=1).users.add(*cls.test_users)

    def test_chat_create(self):
        assert Chat.objects.get(pk=self.chat.pk) is not None

    def test_message_test(self):
        msg = Message(content='test_message', author_id=1, chat_id=1)
        msg.save()
        self.assertEqual(Message.objects.get(pk=msg.pk),second=msg)

    def test_chat_delete(self):
        Chat.objects.get(pk=1).delete()
        assert Chat.objects.filter(pk=1).exists() is False

    def tearDown(self):
        pass
