from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from fizzbuzz.models import FizzBuzz
from fizzbuzz.serializers import UserSerializer, GroupSerializer
from fizzbuzz.serializers import FizzBuzzSerializer
from django.http import HttpResponse, JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# class FizzBuzzViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows FizzBuzz to be viewed or edited.
#     """
#     print('test 2'+str(FizzBuzzSerializer.data.getter('message')))
#     queryset = FizzBuzz.objects.all()
#     serializer_class = FizzBuzzSerializer
#     permission_classes = [permissions.IsAuthenticated]
    

def fizzbuzz_list(request):
    if request.method == 'GET':
        fizzbuzz = FizzBuzz.objects.all()
        serializer = FizzBuzzSerializer(fizzbuzz,many = True)    
        return JsonResponse(serializer.data, safe = False)