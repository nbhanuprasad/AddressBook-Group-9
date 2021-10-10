"""addressbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Contacts import views
from Contacts.views import ContactList,ContactDetail,ContactCreate
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ContactList.as_view(),name='contacts'),
    path('contactcreate/',ContactCreate.as_view(),name='createcontact'),
<<<<<<< HEAD
    path('contactinfo/<int:pk>/', ContactDetail.as_view(),name='contactinfo'),
=======
    #path('contactinfo/<int:pk>/', ContactDetail.as_view(),name='contactinfo'),
>>>>>>> 876d6433e989dd094055f5bdfe2cdf74c2191f5b

    #path('',views.home_view, name='home'),
]
