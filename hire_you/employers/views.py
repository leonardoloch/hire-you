from rest_flex_fields import FlexFieldsModelViewSet, is_expanded
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Employer
from .serializers import EmployerSerializer


class EmployerViewSet(FlexFieldsModelViewSet):
    queryset = Employer.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = EmployerSerializer
