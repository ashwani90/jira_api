from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from portal.models.task import Task
from portal.models.module import Module
import json

class TaskView(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse({"status": True})
    
    def post(self, request, *args, **kwargs):
        try:
            request = request.body.decode('utf-8')
            request = json.loads(request)
            module = Module.objects.get(pk=request['module_id'])
            project = Task.objects.create(name=request['name'], description=request['description'], module=module,status=1, due_date=request['due_date'], started_on=request['started_on'])
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
            if 'module' in update_fields:
                update_fields['module'] = Module.objects.get(pk=request['module'])
            # Convert Dictionary to positional arguments
            Task.objects.filter(pk=request['id']).update(**update_fields)
            return JsonResponse({"status": True})
        except Exception as e:
            print(e)
            return JsonResponse({"status": False})