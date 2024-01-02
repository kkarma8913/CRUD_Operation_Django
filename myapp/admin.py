from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Student)
# admin.site.register(Teacher)
# admin.site.register(employee)
# admin.site.register(Course)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_no','name','course','mobile_no','city','student_image']
    list_filter = ['city','course']
    search_fields =['roll_no','name']
    list_per_page = 2
admin.site.register(Student,StudentAdmin)

admin.site.register(employee )

admin.site.site_header = 'CDGi'
admin.site.site_title='College'
