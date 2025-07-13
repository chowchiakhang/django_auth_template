from django.urls import path, include
from .views import LoginView, RegisterView, UserView
urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
]
