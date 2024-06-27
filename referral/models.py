from django.db import models
from django.contrib.auth.models import AbstractUser

class Agent(AbstractUser):
    TYPE_CHOICES = [
        ('Branch', 'Branch'),
        ('Individual', 'Individual'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    default_rate = models.DecimalField(max_digits=5, decimal_places=2)
    phone_no = models.CharField(max_length=15)
    email_id = models.EmailField()
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='agent_creator')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='agent_modifier')
    modified_date = models.DateTimeField(auto_now=True)

class Student(models.Model):
    student_id = models.CharField(max_length=15, unique=True)
    given_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=15)
    email = models.EmailField()
    created_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='student_creator')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='student_modifier')
    modified_date = models.DateTimeField(auto_now=True)

class Institution(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    created_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='institution_creator')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='institution_modifier')
    modified_date = models.DateTimeField(auto_now=True)

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_fee = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)
    created_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='course_creator')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='course_modifier')
    modified_date = models.DateTimeField(auto_now=True)

class Admission(models.Model):
    start_year = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    agent_rate_applied = models.DecimalField(max_digits=5, decimal_places=2)
    agency_rate_applied = models.DecimalField(max_digits=5, decimal_places=2)
    no_of_installments_planned = models.IntegerField()
    status = models.CharField(max_length=50)
    created_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='admission_creator')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='admission_modifier')
    modified_date = models.DateTimeField(auto_now=True)

class AdmissionStatus(models.Model):
    status_name = models.CharField(max_length=50)
    created_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='admission_status_creator')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='admission_status_modifier')
    modified_date = models.DateTimeField(auto_now=True)

class AdmissionTransaction(models.Model):
    admission = models.ForeignKey(Admission, on_delete=models.CASCADE)
    installment_no = models.IntegerField()
    installment_amt = models.DecimalField(max_digits=10, decimal_places=2)
    agent_commission = models.DecimalField(max_digits=10, decimal_places=2)
    agency_commission = models.DecimalField(max_digits=10, decimal_places=2)
    agent_rate_applied = models.DecimalField(max_digits=5, decimal_places=2)
    agency_rate_applied = models.DecimalField(max_digits=5, decimal_places=2)
    created_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='admission_transaction_creator')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='admission_transaction_modifier')
    modified_date = models.DateTimeField(auto_now=True)
