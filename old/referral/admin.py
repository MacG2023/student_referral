from django.contrib import admin
from .models import Agent, Student, Institution, Course, Admission, AdmissionStatus, AdmissionTransaction

admin.site.register(Agent)
admin.site.register(Student)
admin.site.register(Institution)
admin.site.register(Course)
admin.site.register(Admission)
admin.site.register(AdmissionStatus)
admin.site.register(AdmissionTransaction)
