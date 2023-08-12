from django.urls import path
from utilisateurs.views import acceuil, user_logout, user_login, register
from django.contrib.auth import views
#app_name = 'utilisateurs'
urlpatterns = [
    path('', acceuil, name="acceuil"),
    path('register', register, name="register"),
    path('login', user_login, name="login"),
    path('logout', user_logout, name="logout"),

    path('reset_password', views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_send', views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete', views.PasswordResetCompleteView.as_view(), name="reset_password_complete"),
]