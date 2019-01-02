from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^loginreg$', views.loginreg),
    url(r'^loginreg2$', views.loginreg2),
    url(r'^login$', views.login),
    url(r'^db$', views.db),
    url(r'^db2$', views.db2),

    url(r'^logintrue$', views.logintrue),
    url(r'^welcome$', views.welcome),
    url(r'^product$', views.product),
    url(r'^money$', views.money),
    url(r'^snap/(?P<user_id>\d+)$', views.snap),
    url(r'^edit/(?P<user_id>\d+)$', views.edit),
    url(r'^editing$', views.editing),





    url(r'^addproduct$', views.addproduct),
    # url(r'^edit/(?P<player_id>\d+)$', views.edit),
    url(r'^destroy/(?P<product_id>\d+)$', views.destroy),
    url(r'^bid/(?P<master_id>\d+)/(?P<product_id>\d+)$', views.bid),
    url(r'^product/bid/(?P<master_id>\d+)/(?P<product_id>\d+)$', views.bid2),
    
    url(r'^product/(?P<product_id>\d+)$', views.productx),


    url(r'^logout$', views.logout),

    url(r'^', views.odell),
]