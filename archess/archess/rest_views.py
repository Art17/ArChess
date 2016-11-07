from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework import views
from rest_framework import permissions
from userprofile.serializers import ProfileSerializer, StatisticsSerializer
from userprofile.models import Profile


class UsersAPI(views.APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data)



@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(api_view(['GET', 'DELETE']), name='dispatch')
class UserAPI(views.APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
