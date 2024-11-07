"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('history/', views.history, name='history'),
    path('history/people/', views.famous_people, name='famous_people'),
    path('history/photos/', views.historical_photos, name='historical_photos'),

    re_path(r'^news(?:/.*)?/$', views.city_news, name='city_news'),

    re_path(r'^management(?:/.*)?/$', views.city_management, name='city_management'),

    path('table/<int:wrong>/', views.multy_table, name='multy_table'),

    re_path(r'^facts(?:/.*)?/$', views.city_facts, name='city_facts'),

    re_path(r'^contacts(?:/.*)?/$', views.contact_phone_services, name='contact_phone_services')
]