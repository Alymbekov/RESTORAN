from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from ..models import User
# from status.api.serializers import StatusInlineUserSerializer


class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'user_type',
            'uri',
        ]

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse("api-user:user-detail", kwargs={"username": obj.username}, request=request)
