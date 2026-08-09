from django.urls import path

from main_app import views

# from . import views

urlpatterns = [
    path('', views.index),
    # path('hello/', views.index),
    path('item/', views.item),
    path('<int:id>/', views.detail),
]
