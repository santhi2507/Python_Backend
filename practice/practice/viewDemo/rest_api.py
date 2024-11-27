from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserModelSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class List_users(APIView):

    def get(self, request):
        users = User.objects.all()
        serialized = UserModelSerializer(users, many=True)
        print(serialized.data)
        return Response(serialized.data)
    
    def post(self, request):
        serialized = UserModelSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors)


@api_view(('Patch',))
def update_user(request, id: int):
    user = User.objects.get(id=id)
    serialized = UserModelSerializer(user, data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data)
    return Response(serialized.errors)


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer    







