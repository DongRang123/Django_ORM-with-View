from django.urls import path
from . import views
app_name ='garages'

urlpatterns = [
    path('new/',views.new,name='new'),
    path('',views.index,name='index'),
    path('/create',views.create,name='create')
]
