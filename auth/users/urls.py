from django.urls import path, include
from .views import LoginView, RegisterView, ResetView, UserView, LogoutView, ForgotView
urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('forgot', ForgotView.as_view()),
    path('reset', ResetView.as_view()),
]
