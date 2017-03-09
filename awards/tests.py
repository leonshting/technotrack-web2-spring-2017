from django.test import TestCase
from django.contrib.contenttypes.models import ContentType

from core.models import User
from feed.models import EventType
from public.models import Post
from likes.models import Like
from .models import Award, AwardType


class AwardTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        EventType.objects.create(event_name='blblbl',
                                 content_type=ContentType.objects.get_for_model(Like),
                                 created=True
                                 )
        EventType.objects.create(event_name='blblbla',
                                 content_type=ContentType.objects.get_for_model(Award),
                                 created=True
                                 )
        AwardType.objects.create(award_name='blabla',
                                 related_content=ContentType.objects.get_for_model(Post),
                                 related_value=10,
                                 target=ContentType.objects.get_for_model(Like)
                                 )

        cls.test_users = [User(username='test{}'.format(i)) for i in range(10)]
        for user in cls.test_users:
            user.save()

        post = Post.objects.bulk_create([Post(content='test content', author_id=1)])
        # will not throw pre and post save

        likes = []
        for i in range(10):
            likes.append(Like(author_id=cls.test_users[i].id,
                              content_type=ContentType.objects.get_for_model(Post),
                              object=1))
            likes[i].save()

    def test_likeshock(self):
        award_type = AwardType.objects.get(award_name='blabla')
        assert Award.objects.all().filter(award_type=award_type).exists()
        self.assertEqual(Award.objects.all().filter(award_type=award_type).first().object, 1)

    def tearDown(self):
        pass
