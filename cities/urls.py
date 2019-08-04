from django.urls import path
from cities import views

"""
Here is all routes for invoke the views in the aplication
"""

urlpatterns = [
    path('', views.index, name='index'),
    path('new_region', views.new_region, name='new_region'),
    path('update_region/<int:id>/', views.update_region, name='update_region'),
    path('delete_region/<int:id>/', views.delete_region, name='delete_region'),
    path('new_city', views.new_city, name='new_city'),
    path('update_city/<int:id>/', views.update_city, name='update_city'),
    path('delete_city/<int:id>/', views.delete_city, name='delete_city'),
    ]
