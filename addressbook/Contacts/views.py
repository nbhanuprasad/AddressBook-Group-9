from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import ContactInfo
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
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

class ContactList(LoginRequiredMixin,ListView):
    model= ContactInfo
    context_object_name= 'contacts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts']= context['contacts'].filter(user=self.request.user)
        context['count']=context['contacts'].count()
        return context
class ContactDetail(LoginRequiredMixin,DetailView):
    model= ContactInfo
    context_object_name= 'contactdetail'

class ContactCreate(LoginRequiredMixin,CreateView):
    model= ContactInfo
    fields = ['fname','lname']
    success_url= reverse_lazy('contacts')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(ContactCreate, self).form_valid(form)

class ContactUpdate(LoginRequiredMixin,UpdateView):
    model= ContactInfo
    fields = '__all__'
    context_object_name='contact'
    success_url= reverse_lazy('contacts')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(ContactUpdate, self).form_valid(form)

class ContactDelete(LoginRequiredMixin,DeleteView):
    model=ContactInfo
    context_object_name='delcontact'
    success_url= reverse_lazy('contacts')
