from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.list,name='list'),
    path('create/',views.create,name='create')
]
