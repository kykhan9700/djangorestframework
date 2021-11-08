from django.contrib.auth.models import User, Group
from fizzbuzz.models import FizzBuzz
from rest_framework import serializers
from django_filters import rest_framework as filters


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# class FizzBuzzSerializer(serializers.HyperlinkedModelSerializer):
#     creation_date = serializers.timezone.now()
#     # user_agent = serializers.CharField(source = "test")
#     print('jai telangana')
#     print(serializers)
#     class Meta:
#         model = FizzBuzz
#         fields = ['fizzbuzz_id','message','creation_date','user_agent']   


class FizzBuzzSerializer(serializers.ModelSerializer):
    creation_date = serializers.timezone.now()
    # user_agent = serializers.CharField(source = "test")
    class Meta:
        model = FizzBuzz
        fields = ['fizzbuzz_id','message','creation_date','user_agent']   

