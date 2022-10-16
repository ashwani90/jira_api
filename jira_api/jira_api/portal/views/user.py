from django.contrib.auth import get_user_model
from rest_framework.response import Response
from portal.serializers.user_serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.decorators import action
import json
from django.contrib.auth import authenticate, login
from rest_framework.decorators import  renderer_classes, api_view
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        user = User.objects.get(username=user)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    else:
        return Response({"status": False})
    
@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def register(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    user = User.objects.create_user(username, email, password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    if user is not None:
        login(request, user)
        user = User.objects.get(username=user)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    else:
        return Response({"status": False})

class UserView(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ['get', 'head', 'post', 'put', 'patch']
        
    
    @action(detail=True, methods=['get'])
    def get(self, request):
        id = None
        try:
            id = request.GET.get("id")
        except:
            print("id not present")
        if not id:
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
        else:
            user = User.objects.get(pk=id)
            serializer = UserSerializer(user, many=False)
        
        return Response(serializer.data)
    
    @action(detail=True, methods=['put'])
    def put(self, request, *args, **kwargs):
        try:
            request = request.body.decode('utf-8')
            request = json.loads(request)
            update_fields = request['update_fields']
            # Convert Dictionary to positional arguments
            User.objects.filter(pk=request['id']).update(**update_fields)
            return Response({"status": True})
        except Exception as e:
            print(e)
            return Response({"status": False})