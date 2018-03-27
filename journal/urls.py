from django.conf.urls import url

from . import views

app_name = 'journal'

urlpatterns = [
    url(r'^test/$',),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^$',views.index, name='index'),
]

