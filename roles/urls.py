from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_roles,name="add_roles"),
]
