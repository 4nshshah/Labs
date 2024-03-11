from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),

    path('add_category/', views.add_category, name='add_category'),

    path('add_website/', views.add_website, name='add_website'),

    path('category/<int:category_id>/', views.category, name='category'),

    path('insert_works/', views.insert_works, name='insert_works'),

    path('retrieve_works_lives/', views.retrieve_works_lives, name='retrieve_works_lives'),
    
    path('add_data/', views.add_data, name='add_data'),

    path('retrieve_data/', views.retrieve_data, name='retrieve_data'),

    path('index2/', views.index2, name='index2'),

    path('add_product/', views.add_product, name='add_product'),
    path('human_view/', views.human_view, name='human_view'),

    path('get_human/<int:id>/', views.get_human, name='get_human')

]