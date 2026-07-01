from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    # Slide 6 & 15: FBV Home
    path('', views.home, name='home'),
    
    # Slide 6: Direct HttpResponse demo
    path('simple/', views.simple_http_demo, name='simple_http'),
    
    # Slide 16: Class-Based View demo
    path('cbv/', views.HomeView.as_view(), name='home_cbv'),
    
    # Slide 14 & 23: CRUD Operations & List
    path('list/', views.employee_list, name='list'),
    path('create/', views.employee_create, name='create'),
    path('update/<int:pk>/', views.employee_update, name='update'),
    path('delete/<int:pk>/', views.employee_delete, name='delete'),
    
    # Slide 19: Session Demo
    path('session/', views.session_demo, name='session_demo'),
]
