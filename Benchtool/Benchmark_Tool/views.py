from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Userdata
from Benchtool.settings import BASE_DIR
import mimetypes
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'


 
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
            return render(request, 'chartist.html', {'user': user, 'data': data})
    else:
        error = False
        return render(request, 'user.html', {'error': error})

def filedl(request):
    filename = 'benchtool.exe'
    fl_path = str(BASE_DIR.joinpath('Benchmark_Tool/files/benchtool.exe'))    

    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
