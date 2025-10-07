from django.contrib import admin 
from .models import Member, Recp, Department, StudentID, Student,Subject_M,Subject

# Register your models here.
admin.site.register(Member)
admin.site.register(Recp)
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Subject_M)
admin.site.register(Subject)