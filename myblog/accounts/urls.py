from django.urls import path
from . import views
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
        path('signup', views.SignUpView.as_view(), name='signup'),
        path('password_change/', PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
        path('password_change/done', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
        path('password_reset/',PasswordResetView.as_view(template_name='registration/password_reset_form.html'),name='password_reset'),
        path('password_reset_done/',PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
        path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
        path('reset/done/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
]
