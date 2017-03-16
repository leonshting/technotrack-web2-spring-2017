from django.db.models import Q
from rest_framework import serializers, viewsets, permissions
from rest_framework.reverse import reverse

from feed.models import Event, EventType
from application.api import router
from .permissions import OwnerOrFriend, IsSafeMethod
from .settings import SHOWN_EVENTS, CTYPES


class EventTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventType
        fields = ('event_name',)


class EventSerializer(serializers.ModelSerializer):

    target = serializers.SerializerMethodField()
    event_type = EventTypeSerializer()

    def get_target(self, obj):
        print(obj)
        viewname = '{}-detail'.format(obj.content_type.name)
        return reverse(viewname, (obj.object,), request=self.context['request'])

    class Meta:
        model = Event
        fields = ('author', 'event_type', 'target')


class EventViewSet(viewsets.ModelViewSet):

    http_method_names = ['get']
    serializer_class = EventSerializer
    queryset = Event.objects.all().filter(related_author_id__isnull=True)

    permission_classes = [OwnerOrFriend,
                          IsSafeMethod,
                          ]

    def get_queryset(self):
        qs = super(EventViewSet, self).get_queryset().filter(content_type__in=CTYPES)\
            .filter(event_type__modified=False)\
            .filter(Q(author__in=self.request.user.friends.all()) | Q(author=self.request.user))

        if 'user' in self.request.query_params:
            qs = qs.filter(author_id=self.request.query_params['user'])
        return qs


class FeedbackViewSet(viewsets.ModelViewSet):

    serializer_class = EventSerializer
    queryset = Event.objects.all().filter(related_author_id__isnull=False)

    permission_classes = [IsSafeMethod,
                          ]

    def get_queryset(self):
        qs = super(FeedbackViewSet, self).get_queryset()
        qs = qs.filter(related_author=self.request.user)
        return qs

router.register('feed', EventViewSet, base_name='feed')
router.register('feedback', FeedbackViewSet, base_name='feedback')
