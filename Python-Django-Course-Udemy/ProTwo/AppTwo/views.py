from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    nu={"help_me":"This help notice is coming from a dictionary inside the app's view function."}
    return render(request, 'app_two/help.html',context=nu)
# Create your views here.
