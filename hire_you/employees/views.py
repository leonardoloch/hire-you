from rest_flex_fields import FlexFieldsModelViewSet, is_expanded
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Employee
from .serializers import EmployeeSerializer


class EmployerViewSet(FlexFieldsModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = EmployeeSerializer
