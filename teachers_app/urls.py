from django.urls import path, include
from . import views




urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('view_profile/<task_id>', views.View_student_profile, name='view_profile'),
    path('view_course/<task_id>', views.view_course_details, name='view_course'),
    path('del_course/<task_id>', views.del_course, name='del_course'),
    path('del_student/<task_id>', views.del_student, name='del_student'),
    path('add_student', views.add_student, name='add_student'),
    path('add_course', views.add_course, name='add_course'),
    
]