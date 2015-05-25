from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^logged/$',views.logged,name='logged'),
    url(r'^logout/$',views.logout,name='logout'),
   # url(r'^login/$','login_demo_app.views.login')
]