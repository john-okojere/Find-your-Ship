from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from .views import UserDetailAPI, signup, profile, members, search_memberlist, ResetPasswordView

urlpatterns = [
    path("register/",signup , name="register"),
     path('Login/', LoginView.as_view(template_name="account/form.html"), name="login" ),
    path('Logout/', LogoutView.as_view(), name="logout" ),
    path('password-reset/', ResetPasswordView.as_view(), name="password-reset" ),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/password/reset_confirm.html'),
         name='reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password/reset_complete.html'),
         name='password_reset_complete'),

]
