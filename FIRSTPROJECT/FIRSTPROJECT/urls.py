from django.conf.urls import include, url
from django.contrib import admin
from FIRSTAPPLICATION import views
from django.conf.urls import include

urlpatterns = [
    # Examples:
    # url(r'^$', 'FIRSTPROJECT.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
]
