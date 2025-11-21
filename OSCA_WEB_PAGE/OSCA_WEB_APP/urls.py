from django.urls import path
from . import views

urlpatterns = [
    path('Dashboard/', views.Dashboard, name='__main.html'),
    path('Registration_Category/', views.Registration_Category, name='Registration_Category.html'),
]