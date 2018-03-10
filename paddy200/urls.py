"""paddy200 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from th.views import *
app_name='th'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', test),
    url(r'^login/', login),
    url(r'^login/', login),
    url(r'^sidebar_init/', sidebar_init),
    url(r'^clubuserinit/', clubuserinit),
    url(r'^registerclub/', registerclub),
    url(r'^usercash/', usercash),
    url(r'^operator/', operator),
    url(r'^operator_setup/', operator_setup),
    url(r'^operator_group_setup/', operator_group_setup),
    url(r'^add_operator_group/', add_operator_group),
    url(r'^operator_group_subs_list/', operator_group_subs_list),
    url(r'^operater_setup/', operater_setup),
    url(r'^operator_subs_list/', operator_subs_list),
    url(r'^add_operator/', add_operator),
    url(r'^operator_relation/', operator_relation),
    url(r'^operator_relation_setup/', operator_relation_setup),
]
