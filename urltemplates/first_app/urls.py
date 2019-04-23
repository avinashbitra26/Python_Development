from django.conf.urls import url
from first_app import views

app_name = 'first_app'

urlpatterns = [
    url(r'^other/$', views.other, name='other'),
    url(r'^url_template/$', views.url_template, name='url_template'),
]
