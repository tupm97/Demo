from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.main_view, name='home'),
    path('login/', views.login_view, name='login'),
]
