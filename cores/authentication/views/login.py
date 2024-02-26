from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken  # type: ignore # noqa: I201

from cores.users.serializers.user import UserReadSerializer  # type: ignore # noqa: I100

from ..serializers.login import LoginSerializer


class LoginView(APIView):

    @staticmethod
    def post(request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        reponse = {
            'authentication': {
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            },
            'user': UserReadSerializer(user).data,
        }

        return Response(reponse, status=status.HTTP_200_OK)
