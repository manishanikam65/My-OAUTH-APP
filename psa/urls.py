from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'psa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/', include('login_demo_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logged/$','login_demo_app.views.logged'),
    url(r'^logout/$','login_demo_app.views.logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
]
