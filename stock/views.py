from django.http import HttpResponse
import json


def index(request):
    di = {"xxx":"123","yyy":"456"}
    return HttpResponse(
      json.dumps(di),
      headers={'Content-Type': 'application/json; charset=UTF-8'}
    )
