from django.http import HttpResponse
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")
def my_homepage_view(request):
    return HttpResponse("")
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
