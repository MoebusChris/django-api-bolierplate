from cores.authentication.serializers.token import TokenSerializer
from cores.users.serializers.user import UserReadSerializer


def get_user_auth_data(user):
    return {
        'authentication': TokenSerializer(user).data,
        'user': UserReadSerializer(user).data,
    }
