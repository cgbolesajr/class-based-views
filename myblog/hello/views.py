from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.http import HttpResponse
import textwrap
# Create your views here.


class CourseView(TemplateView):
    template_name = 'course.html'

def course_view(request):
    return render(request, 'hello/course.html',{})

class HomePageView(View):
     def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Django</h1>
                <p>Django Course</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)
