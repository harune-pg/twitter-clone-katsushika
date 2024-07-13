from rest_framework.generics import CreateAPIView

from .serializers import UserCreateSerializer


class SignUpView(CreateAPIView):
    permission = []
    serializer_class = UserCreateSerializer
