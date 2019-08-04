from django.urls import path
from cities import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_region', views.new_region, name='new_region'),
    path('update_region/<int:id>/', views.update_region, name='update_region'),
    path('delete_region/<int:id>/', views.delete_region, name='delete_region')
    ]
