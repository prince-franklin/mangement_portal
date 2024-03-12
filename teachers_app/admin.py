from django.contrib import admin
from .models import student_profile
from .models import courses_detail
from.models import department_mod

# Register your models here.
admin.site.register(student_profile)
admin.site.register(courses_detail)
admin.site.register(department_mod)