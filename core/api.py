from rest_framework import serializers, viewsets

from .models import User
from .permissions import OwnerOrSafeMethods
from application.api import router


class UserSerializer(serializers.HyperlinkedModelSerializer):

    friends_count = serializers.ReadOnlyField()

    class Meta:
        fields = ('url', 'username', 'email', 'friends_count')
        model = User
        extra_kwargs = {
            'url': {'view_name': 'user-detail'}
        }


class UserCreateSerializer(UserSerializer):
    repeat_password = serializers.CharField(allow_blank=False, write_only=True)

    class Meta:

        fields = ('email', 'username', 'password', 'repeat_password')
        model = User
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['repeat_password']:
            raise serializers.ValidationError('PasswordsDoNotMatch')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [OwnerOrSafeMethods,
                          ]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'POST':
            serializer_class = UserCreateSerializer
        return serializer_class

router.register('user', UserViewSet, base_name='user')
