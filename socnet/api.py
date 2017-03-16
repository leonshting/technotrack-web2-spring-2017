from rest_framework import serializers, viewsets, permissions
from django.db.models import Q

from application.api import router
from socnet.models import Friendship, Friend
from .permissions import IsParticipant, RestrictNotSafeAllowDelete, IsFoobar
from core.api import UserSerializer


class FriendshipSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)
    friend = UserSerializer(read_only=True, source='recipient')

    class Meta:
        model = Friendship
        fields = ('friend', 'author', 'approved', 'pk', 'recipient')
        read_only_fields = ('approved',)
        extra_kwargs={
            'recipient': {'write_only': True, 'required': False}
        }


class FriendSerializer(serializers.ModelSerializer):

    foofriend = UserSerializer(read_only=True)
    barfriend = UserSerializer(read_only=True)

    class Meta:
        model = Friend
        fields = ('foofriend', 'barfriend', 'pk')


class FriendshipViewSet(viewsets.ModelViewSet):

    http_method_names = ['get', 'post', 'head', 'put']
    serializer_class = FriendshipSerializer
    queryset = Friendship.objects.all()
    permission_classes = [permissions.IsAuthenticated,
                          IsParticipant,
                          ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(recipient=self.request.user, approved=True)

    def get_queryset(self):
        qs = super(FriendshipViewSet, self).get_queryset()
        if 'approved' in self.request.query_params:
            qs = qs.filter(approved=self.request.query_params['approved']).filter(recipient=self.request.user.id)
        return qs


class FriendViewSet(viewsets.ModelViewSet):

    http_method_names = ['get', 'delete']
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()
    permission_classes = [permissions.IsAuthenticated,
                          IsFoobar,
                          RestrictNotSafeAllowDelete
                          ]

    def get_queryset(self):
        qs = super(FriendViewSet, self).get_queryset()
        if 'user' in self.request.query_params:
            qs = qs.filter(Q(foofriend_id=self.request.query_params['user']))
        if 'mine' in self.request.query_params:
            qs = qs.filter(Q(foofriend_id=self.request.user))
        return qs


router.register('friendship', FriendshipViewSet)
router.register('friend', FriendViewSet)