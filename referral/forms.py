from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Admission, Agent, Course, Student, Institution

class AgentCreationForm(UserCreationForm):
    class Meta:
        model = Agent
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_no', 'type', 'default_rate', 'admin']



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_id',
            'given_name', 
            'surname', 
            'country', 
            'contact_no', 
            'email'
        ]


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['name', 'location', 'country']
        



class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = [
            'start_year', 'student', 'institution', 'course', 'fee', 
            'agent_rate_applied', 'agency_rate_applied', 
            'no_of_installments_planned', 'status'
        ]
        
        


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_fee', 'duration']
