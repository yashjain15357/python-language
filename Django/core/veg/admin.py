from django.contrib import admin 
from .models import Member, Recp, Department, StudentID, Student,Subject_M,Subject

# Register your models here.
admin.site.register(Member)
admin.site.register(Recp)
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)
class Subject_MAdmin(admin.ModelAdmin):
    list_display = ['student' , 'subject' , 'marks' ]
admin.site.register(Subject_M ,Subject_MAdmin)
admin.site.register(Subject)