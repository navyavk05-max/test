from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def test_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        return JsonResponse({
            "message": "API working",
            "received": data
        })
    return JsonResponse({"error": "POST only"})
