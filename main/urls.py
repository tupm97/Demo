from django.urls import path
from . import views
from main.ajax import book

app_name = 'main'
urlpatterns = [
    path('', views.main_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('book/', book.BookAjaxView.as_view(), name="book")
]
