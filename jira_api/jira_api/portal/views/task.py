
from rest_framework.response import Response
from portal.serializers.task_serializer import TaskSerializer
from portal.models.task import Task
from portal.models.module import Module
from portal.helpers.request_response_helper import sendResponse
from rest_framework.views import APIView
from rest_framework.decorators import action
import json
from django.contrib.auth import get_user_model
from portal.helpers.filter_helper import filter_query

User = get_user_model()

filter_fields = [ {"value": "name", "type": "contains"}, 
                 {"value": "status", "type": "equal"}, 
                 {"value": "due_date", "type": "range"}, 
                 {"value": "started_on", "type": "range"}, 
                 {"value": "user", "type": "equal"}, 
                 ]

class TaskView(APIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    http_method_names = ['get', 'head', 'post', 'put', 'patch']
    
    @action(detail=True, methods=['get'])
    def get(self, request):
        id = None
        try:
            id = request.GET.get("id")
        except:
            print("id not present")
        if not id:
            task = Task.objects.all()
            serializer = TaskSerializer(task, many=True)
        else:
            task = Task.objects.get(pk=id)
            serializer = TaskSerializer(task, many=False)
        if request.GET.get("custom_filter"):
            manager = Task.objects
            projects = filter_query(request,filter_fields,manager)
            serializer = TaskSerializer(projects, many=True)
        
        return Response(serializer.data)
        
    @action(detail=True, methods=['post'])
    def post(self, request, *args, **kwargs):
        try:
            request = request.body.decode('utf-8')
            request = json.loads(request)
            module = Module.objects.get(pk=request['module'])
            user = User.objects.get(pk=request['user'])
            task = Task.objects.create(name=request['name'], description=request['description'], due_date=request['due_date'], started_on=request['started_on'], module=module, user=user)
            task.save()
            return Response({"status": True})
        except Exception as e:
            print(e)
            return Response({"status": False})
    
    @action(detail=True, methods=['put'])
    def put(self, request, *args, **kwargs):
        try:
            request = request.body.decode('utf-8')
            request = json.loads(request)
            update_fields = request['update_fields']
            # Convert Dictionary to positional arguments
            Task.objects.filter(pk=request['id']).update(**update_fields)
            return Response({"status": True})
        except Exception as e:
            print(e)
            return Response({"status": False})