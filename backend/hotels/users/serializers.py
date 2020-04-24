from rest_framework import serializers
from .models import User, DjangoUser

# Serializers define the API representation.
class DjangoUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DjangoUser
        fields = ('username', 'first_name', 'last_name', 'email')



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number', 'user')
    user = DjangoUserSerializer(required=True)
