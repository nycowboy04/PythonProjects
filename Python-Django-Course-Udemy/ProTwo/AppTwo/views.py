from django.shortcuts import render
from django.http import HttpResponse

from .models import User
from .forms import UserForm

def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    nu={"help_me":"This help notice is coming from a dictionary inside the app's view function."}
    return render(request, 'app_two/help.html',context=nu)

def users(request):
    user_list=User.objects.order_by('last_name')
    user_dict={'user_record': user_list}
    return render(request, 'app_two/users.html', context=user_dict)

def contactform(request):
    form=UserForm()

    if request.method == "POST":
        form=UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('Error. Form Invalid')
        

    return render(request, 'app_two/userform.html', {'form':form})
# Create your views here.
