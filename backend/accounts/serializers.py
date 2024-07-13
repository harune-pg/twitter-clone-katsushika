from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.core import exceptions as django_exceptions


User = get_user_model()

# 参考: djoser
class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    re_password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "re_password"]

    def validate(self, attrs):
        password = attrs.get("password")
        re_password = attrs.pop("re_password")

        # validate password
        user = User(**attrs)
        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError({"password": serializer_error["non_field_errors"]})

        # validate re_password
        if password != re_password:
            raise serializers.ValidationError({"re_password": "確認用パスワードが一致しません。"})

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
