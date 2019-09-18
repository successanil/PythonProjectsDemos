from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import employees


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = employees
        # fields = ['firstname','lastname'];   # you want to display only few info
        fields = '__all__'


