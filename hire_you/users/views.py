from rest_flex_fields import FlexFieldsModelViewSet, is_expanded
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import User
from .serializers import UserSerializer


class UserViewSet(FlexFieldsModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
