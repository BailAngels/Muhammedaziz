from django.urls import path

from apps.blogs import views


urlpatterns = [
    path('', views.homepage, name = 'index'),
    path('create/', views.create, name = 'create'),
    path('update/<int:pk>/', views.update, name = 'update'),
    path('retrieve/<int:pk>/', views.retrieve, name = 'retrieve'),
    path('delete/<int:pk>/', views.delete, name = 'delete'),
]
