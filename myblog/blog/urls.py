from django.urls import path
from . import views


urlpatterns = [
        path('', views.PostView.as_view(), name='posts'),
        path('post/<pk>', views.PostDetailView.as_view(), name='detail'),
        path('write/', views.WriteView.as_view(success_url="/"), name='write')

    ]
