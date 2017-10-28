from django.conf.urls import url

from . import views,api

app_name='employee'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^customer/', views.customer, name='customer'),
    url(r'^profile/(?P<acc>[A-Z0-9]+)/$', views.details, name='details'),
    url(r'^search/$',views.search, name='search'),
    url(r'^api/list/',api.CustomerList.as_view()),
    url(r'^api/customer/$', api.GetCustomer.as_view()) #api/customer?acc='ACC5'
]