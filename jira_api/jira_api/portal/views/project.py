from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from portal.models.project import Project
import json

class ProjectView(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse({"status": True})
    
    def post(self, request, *args, **kwargs):
        try:
            request = request.body.decode('utf-8')
            request = json.loads(request)
            project = Project.objects.create(name=request['name'], client_name=request['client_name'], budget=request['budget'], due_date=request['due_date'], started_on=request['started_on'])
            project.save()
            return JsonResponse({"status": True})
        except Exception as e:
            print(e)
            return JsonResponse({"status": False})
        
    def put(self, request, *args, **kwargs):
        try:
            request = request.body.decode('utf-8')
            request = json.loads(request)
            update_fields = request['update_fields']
            # Convert Dictionary to positional arguments
            Project.objects.filter(pk=request['id']).update(**update_fields)
            return JsonResponse({"status": True})
        except Exception as e:
            print(e)
            return JsonResponse({"status": False})