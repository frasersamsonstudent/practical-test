from django.http import HttpResponse
from django.shortcuts import render
from courses.models import Course

# Create your views here.
def index(request):
    context = dict()
    courses = Course.objects.order_by('start_date')

    context['courses'] = courses

    return render(request, 'courses/index.html', context=context)
