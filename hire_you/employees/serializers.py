from rest_flex_fields import FlexFieldsModelSerializer

from .models import Employee


class EmployeeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ('created', 'modified', 'id')