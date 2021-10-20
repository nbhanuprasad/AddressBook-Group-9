from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import ContactInfo
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
import os.path
# Create your views here.
#def home_view(request,*args, **kwargs):
    #return HttpResponse("<h1> Hello World</h1>")
#    return render(request, "login.html", {})
class CustomLoginView(LoginView):
    template_name='login.html'
    field='__all__'
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy('contacts')

class ContactList(ListView):
    model= ContactInfo
    context_object_name= 'contacts'
class ContactDetail(DetailView):
    model= ContactInfo
    context_object_name= 'contactdetail'

class ContactCreate(CreateView):
    model= ContactInfo
    fields = '__all__'
    success_url= reverse_lazy('contacts')
class ContactUpdate(UpdateView):
    model= ContactInfo
    fields = '__all__'
    context_object_name='contact'
    success_url= reverse_lazy('contacts')
class ContactDelete(DeleteView):
    model=ContactInfo
    context_object_name='delcontact'
    success_url= reverse_lazy('contacts')
