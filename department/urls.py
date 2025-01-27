from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login/',views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('add/', views.add_department, name='add_department'),
    path('addUser/', views.register, name='addUser'),
    path('update/<int:id>/', views.update_department, name='update_department'),
    path('delete/<int:id>/', views.delete_department, name='delete_department'),
]
