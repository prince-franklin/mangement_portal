from django.shortcuts import render,redirect
from . models import student_profile
from . models import courses_detail
from .form import studentForm, courseForm, departmentForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    student=student_profile.objects.all()
    courses= courses_detail.objects.all()
    
    return render(request, 'dashboard.html', {'student': student, 'courses':courses})


def View_student_profile(request, task_id):
    profile=student_profile.objects.get(pk=task_id)

    return render(request,'profile.html', {'profile': profile})

def add_student(request):
    if request.method=="POST":
        form=studentForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ('profile added successfully'))
        return redirect('add_student') 
    else:
         return render (request, 'add_student.html')
     
def add_course(request):
        if request.method=="POST":
            form_c=courseForm(request.POST or None)
            if form_c.is_valid():
                form_c.save()
            messages.success(request,('course detail added successfully'))
            return redirect('add_course')
        else:
            return render(request,'add_course.html')
            
        
           
def view_course_details(request, task_id):
    course=courses_detail.objects.get(pk=task_id)
    return render(request, 'course.html',{'course':course})


def del_student(request, task_id):
    profile=student_profile.objects.get(pk=task_id)
    profile.delete()
    return redirect('dashboard')

def del_course(request, task_id):
    course=courses_detail.objects.get(pk=task_id)
    course.delete()
    return redirect('dashboard')

def edit_course(request, task_id):
    if request.method=="POST":
        course=courses_detail.objects.get(pk=task_id)
        form=courseForm(request.POST or None, instance= course)
        if form.is_valid():
            form.save()
        messages.success(request, ('Course Updated Successfully'))
        return redirect('dashboard')
    else:
        course_up=courses_detail.objects.get(pk=task_id)
        return render(request,'edit_course.html',{'course_up':course_up} )
    
def edit_profile(request, task_id):
    if request.method=="POST":
        profile=student_profile.objects.get(pk=task_id)
        form=studentForm(request.POST or None, instance= profile)
        if form.is_valid():
            form.save()
        messages.success(request, ('Profile Updated Successfully'))
        return redirect('dashboard')
    else:
        profile_up=student_profile.objects.get(pk=task_id)
        return render(request,'edit_profile.html',{'profile_up':profile_up} )
    
def add_department(request):
    if request.method=="POST":
        form=departmentForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,('Department Added successfully'))
        return redirect('add_department')
    else:
        return render(request,'department.html')