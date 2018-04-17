from django.shortcuts import render
from django.http import HttpResponse

from .models import User

def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    nu={"help_me":"This help notice is coming from a dictionary inside the app's view function."}
    return render(request, 'app_two/help.html',context=nu)

def users(request):
    user_list=User.objects.order_by('last_name')
    user_dict={'user_record': user_list}
    return render(request, 'app_two/users.html', context=user_dict)

# Create your views here.
