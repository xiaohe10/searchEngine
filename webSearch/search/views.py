# Create your views here.
from  django.shortcuts  import  render_to_response
from django.http import HttpResponseRedirect
def search_home(request):
    return render_to_response('home.html',locals())
def search_result(request):
    try:
        args = request.GET['args']
    except:
        return HttpResponseRedirect('/')
    return render_to_response('result.html',locals())