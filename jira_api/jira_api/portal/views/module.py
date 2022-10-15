
from rest_framework.response import Response
from portal.serializers.module_serializer import ModuleSerializer
from portal.models.module import Module
from portal.models.project import Project
from portal.helpers.request_response_helper import sendResponse
from rest_framework.views import APIView
from rest_framework.decorators import action
import json


class ModuleView(APIView):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    http_method_names = ['get', 'head', 'post', 'put', 'patch']
    
    @action(detail=True, methods=['get'])
    def get(self, request):
        id = None
        try:
            id = request.GET.get("id")
        except:
            print("id not present")
        print(request.GET.get("id"))
        if not id:
            modules = Module.objects.all()
            serializer = ModuleSerializer(modules, many=True)
        else:
            modules = Module.objects.get(pk=id)
            serializer = ModuleSerializer(modules, many=False)
        
        return Response(serializer.data)
        
    @action(detail=True, methods=['post'])
    def post(self, request, *args, **kwargs):
        try:
            request = request.body.decode('utf-8')
            request = json.loads(request)
            project = Project.objects.get(pk=request['project'])
            module = Module.objects.create(name=request['name'], project=project, due_date=request['due_date'], started_on=request['started_on'])
            module.save()
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
            Module.objects.filter(pk=request['id']).update(**update_fields)
            return Response({"status": True})
        except Exception as e:
            print(e)
            return Response({"status": False})