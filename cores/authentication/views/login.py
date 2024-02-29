from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cores.users.serializers.user import UserReadSerializer  # type: ignore # noqa: I100

from ..serializers.login import LoginSerializer
from ..serializers.token import TokenSerializer


class LoginView(APIView):

    @staticmethod
    def post(request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        reponse = {
            'authentication': TokenSerializer(user).data,
            'user': UserReadSerializer(user).data,
        }

        return Response(reponse, status=status.HTTP_200_OK)
