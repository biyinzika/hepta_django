from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404


def index(request):
    return HttpResponse("Hello World you're at the momo index.")

#####################################################################################

def homepage_view(request, *args, **kwargs): 
    print(args, kwargs)
    return HttpResponse("<h2>Biyinzika home page</h2>")
#     return render(request, "templates.momo.index.html", {})

def about_page(*args, **kwargs):
    return HttpResponse("<h3>This is a test Django product</h3>")
