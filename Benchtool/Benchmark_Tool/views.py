from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Userdata
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

 
def search(request):
    error = False
    if 'user' in request.GET and request.GET.get('user'):
        user = request.GET.get('user')
        try:
            data = Userdata.objects.get(username=user)
        except Userdata.DoesNotExist:
            error = True
            return render(request, 'user.html', {'error': error})
        else:
            return render(request, 'chart.html', {'user': user, 'data': data})
    else:
        error = False
        return render(request, 'user.html', {'error': error})

    