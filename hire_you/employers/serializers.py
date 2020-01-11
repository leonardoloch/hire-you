from rest_flex_fields import FlexFieldsModelSerializer

from .models import Employer


class EmployerSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'
        read_only_fields = ('created', 'modified', 'id')