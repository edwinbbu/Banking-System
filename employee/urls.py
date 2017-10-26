from django.conf.urls import url

from employee import views

app_name='employee'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^customer/', views.customer, name='customer'),
    url(r'^profile/(?P<acc>[A-Z0-9]+)/$', views.details, name='details'),
    url(r'^search/',views.search, name='search')
]