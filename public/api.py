from django.db.models import Q
from rest_framework import serializers, viewsets, permissions, pagination
from rest_framework.reverse import reverse

from application.api import router
from .models import Post, Comment
from .permissions import IsOwnerOrReadOnly, TimeFromCreation, IsFriend, IsCommentRelatedToFriendObject


class CommentSerializer(serializers.ModelSerializer):

    target = serializers.SerializerMethodField()
    author = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    def get_target(self, obj):
        viewname = '{}-detail'.format(obj.content_type.name)
        return reverse(viewname, (obj.object,), request=self.context['request'])

    def create(self, validated_data):
        comment = Comment.objects.create(author_id=self.context['request'].user.id, **validated_data)
        return comment

    class Meta:
        model = Comment
        fields = 'id', 'target', 'author', 'content', 'content_type', 'object'
        extra_kwargs = {'content_type': {'write_only': True},
                        'object': {'write_only': True}}


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,
                          TimeFromCreation,
                          IsCommentRelatedToFriendObject
                          ]
    queryset = Comment.objects.all()

    def get_queryset(self):
        qs = super(CommentViewSet, self).get_queryset()
        if 'author' in self.request.query_params:
            qs = qs.filter(auhtor_id=self.request.query_params['author'])
        if 'ct' in self.request.query_params and 'id' in self.request.query_params:
            qs = qs.filter(content_type=self.request.query_params['ct'], object=self.request.query_params['id'])
        return qs


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author_id')

    class Meta:
        model = Post
        fields = 'author', 'content', 'pk'


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,
                          IsFriend,
                          ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super(PostViewSet, self).get_queryset()\
            .filter(Q(author__in=self.request.user.friends.all()) | Q(author=self.request.user))
        if 'author' in self.request.query_params:
            qs = qs.filter(author=self.request.query_params['author'])
        return qs


router.register('post', PostViewSet, base_name='post')
router.register('comment', CommentViewSet, base_name='comment')
