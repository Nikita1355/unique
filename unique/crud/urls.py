from django.urls import path
from . import views 

urlpatterns = [
    
    path('crud', views.crud, name='crud'),
    path('add', views.ADD, name='add'),
    path('edit', views.Edit, name='edit'),
    path('update/<str:id>', views.Update, name='update'),
    path('delete/<str:id>', views.Delete, name='delete'),
    path('add_page', views.Add_page, name='add_page'),
    path('manage_courses', views.Manage_courses, name='manage_courses'),

    
]