
from rest_framework.response import Response
from portal.serializers.project_serializer import ProjectSerializer
from portal.models.project import Project
from rest_framework.views import APIView
from rest_framework.decorators import action
import json
from django.contrib.auth import get_user_model
from portal.helpers.filter_helper import filter_query

User = get_user_model()

filter_fields = [ {"value": "name", "type": "contains"}, 
                 {"value": "client_name", "type": "contains"}, 
                 {"value": "budget", "type": "range"}, 
                 {"value": "due_date", "type": "range"}, 
                 {"value": "started_on", "type": "range"}, 
                 ]

class ProjectView(APIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    http_method_names = ['get', 'head', 'post', 'put', 'patch']
    
    @action(detail=True, methods=['get'])
    def get(self, request):
        id = None
        try:
            id = request.GET.get("id")
        except:
            print("id not present")
        if not id:
            projects = Project.objects.all()
            serializer = ProjectSerializer(projects, many=True)
        else:
            projects = Project.objects.get(pk=id)
            serializer = ProjectSerializer(projects, many=False)
        if request.GET.get("custom_filter"):
            manager = Project.objects
            projects = filter_query(request,filter_fields,manager)
            serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
        
    @action(detail=True, methods=['post'])
    def post(self, request, *args, **kwargs):
        try:
            request = request.body.decode('utf-8')
            request = json.loads(request)
            user = User.objects.get(pk=request['user'])
            project = Project.objects.create(name=request['name'], client_name=request['client_name'], budget=request['budget'],due_date=request['due_date'], started_on=request['started_on'])
            project.users.add(user)
            project.save()
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
            Project.objects.filter(pk=request['id']).update(**update_fields)
            return Response({"status": True})
        except Exception as e:
            print(e)
            return Response({"status": False})