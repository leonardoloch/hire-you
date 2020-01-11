from rest_flex_fields import FlexFieldsModelSerializer

from .models import User


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('created', 'modified', 'id')