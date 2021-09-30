from django.http import HttpResponse

def readme(request):
  f = open('./stockapi/readme.txt', 'r')
  data = f.read()
  f.close()
  return HttpResponse(data)