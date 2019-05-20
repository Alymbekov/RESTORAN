from rest_framework.generics import RetrieveAPIView, ListAPIView
from users.user.serializers import UserDetailSerializer
from ..models import User


class UserDeatilAPIView(RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = "username"

    def get_serializer_context(self):
        return {'request': self.request}
