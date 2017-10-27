from django.conf.urls import url, include

from . import views

app_name = 'customer'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^withdraw/',views.withdraw, name='withdraw'),
    url(r'^amount/',views.amount, name='amount'),
    url(r'^deposit/', views.deposit, name='deposit'),
    url(r'^amount2/', views.amount2, name='amount2'),
    url(r'^transfer/', views.transfer, name='transfer'),
    url(r'^result/',views.result, name='result'),
    url(r'^edit/',views.edit, name='edit'),
]