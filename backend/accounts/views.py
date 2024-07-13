from rest_framework.generics import CreateAPIView

from .serializers import UserCreateSerializer


class SignUpView(CreateAPIView):
    """ユーザー登録API"""
    permission = []
    serializer_class = UserCreateSerializer
