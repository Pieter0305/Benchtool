from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Userdata
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

def Chart(request):
    labels = []
    f64= []
    i64 = []
    i32 = []
    i16 = []

    return render(request, 'home.html')
 
