from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def home(request):
    context = RequestContext(request)
    return render_to_response('home/home.html', {}, context)