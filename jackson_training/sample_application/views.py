# from django.http import HttpResponse

from django.shortcuts import render
from .forms import *

from .models import *
def index(request):
     # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']= form
    # return HttpResponse("welcome to the index page")
    return render(request,'index.html',context)

def view_data(request):
    context = {}
    # add the dictionary during initialization
    context['dataset'] = Blog.objects.all()
    # can be used for logs        
    return render(request,'view_data.html',context)

# ---------------------------------------------------------------------------------------------------------------------
#                               for rest api
# ---------------------------------------------------------------------------------------------------------------------

from rest_framework import viewsets

from .serializers import *

class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer