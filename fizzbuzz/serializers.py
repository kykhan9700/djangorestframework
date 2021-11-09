from django.contrib.auth.models import User, Group
from fizzbuzz.models import FizzBuzz
from rest_framework import serializers
from django_filters import rest_framework as filters


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    UserSerializer for model User
    """
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    GroupSerializer for model Group
    """
    class Meta:
        model = Group
        fields = ['url', 'name']


class FizzBuzzSerializer(serializers.ModelSerializer):
    """
    FizzBuzzSerializer for model Group
    """
    class Meta:
        model = FizzBuzz
        fields = ['fizzbuzz_id','message','creation_date','user_agent']   
