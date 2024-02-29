from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cores.authentication.serializers.token import TokenSerializer  # type: ignore # noqa: I100

from ..serializers.user import UserReadSerializer, UserWriteSerializer


class UserDetailView(APIView):

    @staticmethod
    def post(request):
        serializer = UserWriteSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            reponse = {
                'authentication': TokenSerializer(user).data,
                'user': UserReadSerializer(user).data,
            }

        return Response(reponse, status=status.HTTP_201_CREATED)
