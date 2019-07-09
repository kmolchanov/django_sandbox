from django.http import HttpResponse


def index(request):
    return HttpResponse("<center>Hello, world! You are on Polls index page.</center>")
