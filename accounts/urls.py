# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.login_view, name='login'),  # Update this line
    path('accounts/signup/', views.signup_view, name='signup'),  # Update this line
    path('accounts/logout/', views.logout_view, name='logout'), # Update this line
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  # Update this line
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # Update this line
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # Update this line
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  # Update this line
    path('accounts/password_change/', views.change_password, name='password_change'),  # Update this line
    path('accounts/dashboard/', views.dashboard, name='dashboard'),  # Update this line
    path('accounts/profile/', views.profile, name='profile'),  # Update this line
]