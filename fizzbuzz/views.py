from django.contrib.auth.models import User, Group
from rest_framework import viewsets, serializers, permissions
from fizzbuzz.models import FizzBuzz
from fizzbuzz.serializers import UserSerializer, GroupSerializer, FizzBuzzSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



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

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/fizzbuzz/',
        'List Detail' : '/fizzbuzz/<str:pk>',
        'Create' : '/fizzbuzz/'
    }
    return Response(api_urls)

@api_view(['GET','POST'])
def fizzbuzzList(request):
    if request.method == 'GET':
        fizzbuzz = FizzBuzz.objects.all()
        serializer_class = FizzBuzzSerializer(fizzbuzz,many=True)
         
    if request.method == 'POST':
        print(request.META['HTTP_USER_AGENT'])
        print(request.data)
        user_agent = request.META['HTTP_USER_AGENT']
        creation_date = serializers.timezone.now()
        serializer_class = FizzBuzzSerializer(data={'user_agent':user_agent,'creation_date':creation_date,'message':request.data['message']})

        if serializer_class.is_valid():
            serializer_class.save()

    return Response(serializer_class.data)     


@api_view(['GET'])
def fizzbuzzDetail(request,pk):
    fizzbuzz = FizzBuzz.objects.get(fizzbuzz_id = pk)
    serializer_class = FizzBuzzSerializer(fizzbuzz,many=False)
    return Response(serializer_class.data)  