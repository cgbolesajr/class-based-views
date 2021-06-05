from django.urls import path
from .views import HomePageView, CourseView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('courses', CourseView.as_view(), name='courses' ),
    path('coursenow', views.course_view, name='coursenow')
]
