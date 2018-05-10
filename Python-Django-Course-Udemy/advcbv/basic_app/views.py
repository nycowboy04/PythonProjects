from django.shortcuts import render
from django.views.generic import TemplateView, View,ListView,DetailView

from . import models
class IndexView(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['injectme']='Basic Injection'
        return context

class SchoolListView(ListView):
    model = models.School
    context_object_name = 'schools'
    
class SchoolDetailView(DetailView):
    model=models.School
    context_object_name='school_detail'
    template_name='basic_app/school_detail.html'
