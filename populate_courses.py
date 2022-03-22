import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practical_test_project.settings')

import django
django.setup()
from courses.models import Course

def populate():
    courses = [
        {'title': 'Web Application Systems',
            'description': 'This is the most useful, most valuable and most inspiring course ever!',
            'start_date': '2022-04-01'},
        {'title': 'Software Engineering',
            'description': 'This course is about good software engineering practices',
            'start_date': '2022-06-01'},
    ]

    for course in courses:
        add_course(course['title'], course['description'], course['start_date'])

def add_course(title, description, start_date):
    course = Course.objects.get_or_create(title=title, description=description, start_date=start_date)[0]
    course.save()
    return course

if __name__ == '__main__':
    print('Starting population script')
    populate()