from rest_framework import serializers, viewsets, permissions
from rest_framework.reverse import reverse
from restframework_serializer_factory.serializers import modelserializer_factory

from application.api import router
from .models import LikableMixin, Like


class LikeSerializer(serializers.ModelSerializer):

    target = serializers.SerializerMethodField()

    def get_target(self, obj):
        viewname = '%s-detail' % obj.content_type.name
        return reverse(viewname, (obj.object,), request=self.context['request'])

    class Meta:
        model = Like
        fields = 'id', 'target', 'author', 'content_type', 'object'
        extra_kwargs = {'content_type': {'write_only': True},
                        'object': {'write_only': True}}


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super(LikeViewSet, self).get_queryset()
        if 'ct' in self.request.query_params:
            qs = qs.filter(content_type_id=self.request.query_params['ct'])
        if 'id' in self.request.query_params:
            qs = qs.filter(object=self.request.query_params['id'])
        return qs


router.register('like', LikeViewSet)
