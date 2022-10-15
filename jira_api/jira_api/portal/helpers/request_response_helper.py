from django.http import JsonResponse
from django.core.serializers import serialize




def sendResponse(response_dict):
    return JsonResponse(response_dict.items(), safe=False)