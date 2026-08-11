from django.urls import path

from main_app import views

app_name = 'main_app'

# from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('hello/', views.index),
    # path('item/', views.item),
    path('<int:id>/', views.detail, name='detail'),
    path('add/', views.create_item),
]
