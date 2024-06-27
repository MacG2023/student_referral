from django.db import models
from django.contrib.auth.models import AbstractUser

class Agent(AbstractUser):
    TYPE_CHOICES = [
        ('Branch', 'Branch'),
        ('Individual', 'Individual'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    default_rate = models.DecimalField(max_digits=5, decimal_places=2 , null=True)
    phone_no = models.CharField(max_length=15)
    email_id = models.EmailField()
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='agent_creator')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='agent_modifier')
    modified_date = models.DateTimeField(auto_now=True)
    admin = models.BooleanField(default=False)
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Student(models.Model):
    student_id = models.CharField(max_length=15, unique=True)
    given_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
    created_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='student_creator')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='student_modifier')
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.given_name + " " + self.surname

class Institution(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    contact_no = models.CharField(max_length=20)
    
    created_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='institution_creator')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='institution_modifier')
    modified_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_fee = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)
    created_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='course_creator')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='course_modifier')
    modified_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.course_name

# class Admission(models.Model):
#     start_year = models.IntegerField()
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     fee = models.DecimalField(max_digits=10, decimal_places=2)
#     agent_rate_applied = models.DecimalField(max_digits=5, decimal_places=2)
#     agency_rate_applied = models.DecimalField(max_digits=5, decimal_places=2)
#     no_of_installments_planned = models.IntegerField()
#     status = models.CharField(max_length=50)
#     created_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='admission_creator')
#     created_date = models.DateTimeField(auto_now_add=True)
#     modified_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='admission_modifier')
#     modified_date = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.student.given_name + " " + self.student.surname


# from django.db import models

class Admission(models.Model):
    MONTH_CHOICES = [
        (1, 'Jan'),
        (2, 'Feb'),
        (3, 'Mar'),
        (4, 'Apr'),
        (5, 'May'),
        (6, 'Jun'),
        (7, 'Jul'),
        (8, 'Aug'),
        (9, 'Sep'),
        (10, 'Oct'),
        (11, 'Nov'),
        (12, 'Dec'),
    ]

    YEAR_CHOICES = [(year, year) for year in range(2000, 2101)]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Dropout', 'Dropout'),
        ('Payment Completed', 'Payment Completed'),
    ]

    start_year = models.IntegerField(choices=YEAR_CHOICES)
    month = models.IntegerField(choices=MONTH_CHOICES, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    agent_rate_applied = models.DecimalField(max_digits=5, decimal_places=2)
    agency_rate_applied = models.DecimalField(max_digits=5, decimal_places=2)
    no_of_installments_planned = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)  # Updated to use choices
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    created_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='admission_creator')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='admission_modifier')
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.institution} - {self.course}"


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
