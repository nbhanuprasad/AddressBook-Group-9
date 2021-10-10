from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import ContactInfo
from django.views.generic.detail import DetailView
# Create your views here.
#def home_view(request,*args, **kwargs):
    #return HttpResponse("<h1> Hello World</h1>")
#    return render(request, "login.html", {})
class ContactList(ListView):
    model= ContactInfo
    context_object_name= 'contacts'
class ContactDetail(DetailView):
    model= ContactInfo
    context_object_name= 'contactdetail'
    
