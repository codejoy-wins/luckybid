from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^loginreg$', views.loginreg),
    url(r'^loginreg2$', views.loginreg2),
    url(r'^login$', views.login),
    url(r'^db$', views.db),
    url(r'^logintrue$', views.logintrue),
    url(r'^welcome$', views.welcome),

    url(r'^logout$', views.logout),

    url(r'^', views.odell),
]