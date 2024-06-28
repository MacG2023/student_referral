from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Admission, AdmissionTransaction, Agent, Course, Student, Institution

class AgentCreationForm(UserCreationForm):
    class Meta:
        model = Agent
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_no', 'type', 'default_rate', 'admin']


class AgentChangeForm(UserCreationForm):
    class Meta:
        model = Agent
        fields = [ 'first_name', 'last_name', 'email', 'phone_no', 'type', 'default_rate', 'admin']



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
        fields = ['name', 'location', 'country', 'email', 'contact_no']
        



class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        # fields = [
        #     'start_year', 'student', 'institution', 'course', 'fee', 
        #     'agent_rate_applied', 'agency_rate_applied', 
        #     'no_of_installments_planned', 'status'
        # ]
        fields = ['start_year', 'month', 'student', 'institution', 'course', 'fee', 'agent_rate_applied',
                  'agency_rate_applied', 'no_of_installments_planned', 'status', 'commission_rate']
        
        


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_fee', 'duration']



class AdmissionTransactionForm(forms.ModelForm):
    class Meta:
        model = AdmissionTransaction
        fields = ['admission', 'installment_no', 'installment_amt', 'agent_commission', 'agency_commission', 'agent_rate_applied', 'agency_rate_applied']
