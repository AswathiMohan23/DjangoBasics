from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
   # return HttpResponse("Hello World")
   return render(request,'home.html',{'name':'Tom'}) # render is used to call html page because we need to render the template because template is a file and
                            # it may have some dynamic content