from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import ContactInfo
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import csv
from django.conf.urls.static import static
import os.path
# Create your views here.
#def home_view(request,*args, **kwargs):
    #return HttpResponse("<h1> Hello World</h1>")
#    return render(request, "login.html", {})
def home_view(request):
    redirect_authenticated_user=True
    return render(request, 'home.html')


class CustomLoginView(LoginView):
    template_name='login.html'
    field='__all__'
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy('contacts')

class RegisterPage(FormView):
    template_name='register.html'
    form_class = UserCreationForm
    fields = '__all__'
    redirect_authenticated_user=True
    success_url=reverse_lazy('contacts')

    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('contacts')
        return super(RegisterPage, self).get(*args, **kwargs)

class ContactList(LoginRequiredMixin,ListView):
    model= ContactInfo
    context_object_name= 'contacts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts']= context['contacts'].filter(user=self.request.user)
        context['count']=context['contacts'].count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            fna=context['contacts'].filter(fname__icontains=search_input)
            lna=context['contacts'].filter(lname__icontains=search_input)
            phn=context['contacts'].filter(phnumber__icontains=search_input)
            context['contacts'] = fna | lna | phn
        return context
class ContactDetail(LoginRequiredMixin,DetailView):
    model= ContactInfo
    context_object_name= 'contactdetail'

class ContactCreate(LoginRequiredMixin,CreateView):
    model= ContactInfo
    fields = ['photo','fname','lname','DOB','phnumber','phnumberalt','email_address','Staddress','city','state','zipcode','country']
    success_url= reverse_lazy('contacts')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(ContactCreate, self).form_valid(form)

class ContactUpdate(LoginRequiredMixin,UpdateView):
    model= ContactInfo
    fields = ['photo','fname','lname','DOB','phnumber','phnumberalt','email_address','Staddress','city','state','zipcode','country']
    context_object_name='contact'
    success_url= reverse_lazy('contacts')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(ContactUpdate, self).form_valid(form)

class ContactDelete(LoginRequiredMixin,DeleteView):
    model=ContactInfo
    context_object_name='delcontact'
    success_url= reverse_lazy('contacts')

def DeleteImage(request, pk):
    model = ContactInfo
    cont = ContactInfo.objects.get(cid=pk)
    if cont.photo!='default.png':
        os.remove(cont.photo.path)
        cont.photo = 'default.png'
        cont.save()
    return HttpResponse("Image has been deleted and set to Default")

def ContactCSV(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attatchment; filename=Contacts.csv'
    writer = csv.writer(response)
    contacts=ContactInfo.objects.filter(user=request.user)
    writer.writerow(['First Name','Last Name','Date of Birth','Phone Number','Alternate Phone Number','Email ID','Street Address','City','State','Zipcode','Country'])
    for contact in contacts:
        writer.writerow([contact.fname,contact.lname,contact.DOB,contact.phnumber,contact.phnumberalt,contact.email_address,contact.Staddress,contact.city,contact.state,contact.zipcode,contact.get_country_display()])
    return response
