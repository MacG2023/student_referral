from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Admission, AdmissionTransaction, Agent, Course
from .forms import AdmissionForm, AgentChangeForm, AgentCreationForm, CourseForm, StudentForm, InstitutionForm

from .models import Student,Institution



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'referral/login.html', {'error': 'Invalid username or password'})
    return render(request, 'referral/login.html')

@login_required
def home_view(request):
    transactions = AdmissionTransaction.objects.filter(created_by=request.user)
    return render(request, 'referral/home.html', {'transactions': transactions})



# from django.shortcuts import render, redirect
# 
# f

def admin_required(user):
    return user.is_authenticated and user.admin

@login_required
@user_passes_test(admin_required)
def create_agent_view(request):
    if request.method == 'POST':
        form = AgentCreationForm(request.POST)
        if form.is_valid():
            agent = form.save(commit=False)
            agent.created_by = request.user
            agent.modified_by = request.user
            agent.save()
            return redirect('agent_list')
    else:
        form = AgentCreationForm()
    return render(request, 'referral/create_agent.html', {'form': form})


def agent_list_view(request):
    agents = Agent.objects.all()
    return render(request, 'referral/agent_list.html', {'agents': agents})



def edit_agent_view(request, agent_id):
    agent = get_object_or_404(Agent, id=agent_id)
    if request.method == 'POST':
        form = AgentChangeForm(request.POST, instance=agent)
        if form.is_valid():
            form.save()
            return redirect('agent_list')  # Redirect to agent list after successful update
    else:
        form = AgentChangeForm(instance=agent)
    
    return render(request, 'referral/edit_agent.html', {'form': form, 'agent': agent})

@login_required
def add_student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.created_by = request.user
            student.modified_by = request.user
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'referral/add_student.html', {'form': form})



@login_required
def student_list_view(request):
    students = Student.objects.all()
    return render(request, 'referral/student_list.html', {'students': students})




@login_required
def add_institution_view(request):
    if request.method == 'POST':
        form = InstitutionForm(request.POST)
        if form.is_valid():
            institution = form.save(commit=False)
            institution.created_by = request.user
            institution.modified_by = request.user
            institution.save()
            return redirect('institution_list')
    else:
        form = InstitutionForm()
    return render(request, 'referral/add_institution.html', {'form': form})

@login_required
def institution_list_view(request):
    institutions = Institution.objects.all()
    return render(request, 'referral/institution_list.html', {'institutions': institutions})

@login_required
def edit_institution_view(request, pk):
    institution = get_object_or_404(Institution, pk=pk)
    if request.method == 'POST':
        form = InstitutionForm(request.POST, instance=institution)
        if form.is_valid():
            institution = form.save(commit=False)
            institution.modified_by = request.user
            institution.save()
            return redirect('institution_list')
    else:
        form = InstitutionForm(instance=institution)
    return render(request, 'referral/edit_institution.html', {'form': form})


@login_required
def edit_student_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.modified_by = request.user
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'referral/edit_student.html', {'form': form})



@login_required
def add_admission_view(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            admission = form.save(commit=False)
            admission.created_by = request.user
            admission.modified_by = request.user
            admission.save()
            return redirect('admission_list')
    else:
        form = AdmissionForm()
    return render(request, 'referral/add_admission.html', {'form': form})

@login_required
def admission_list_view(request):
    admissions = Admission.objects.all()
    return render(request, 'referral/admission_list.html', {'admissions': admissions})

@login_required
def edit_admission_view(request, pk):
    admission = get_object_or_404(Admission, pk=pk)
    if request.method == 'POST':
        form = AdmissionForm(request.POST, instance=admission)
        if form.is_valid():
            admission = form.save(commit=False)
            admission.modified_by = request.user
            admission.save()
            return redirect('admission_list')
    else:
        form = AdmissionForm(instance=admission)
    return render(request, 'referral/edit_admission.html', {'form': form})



@login_required
def add_course_view(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user
            course.modified_by = request.user
            course.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'referral/add_course.html', {'form': form})

@login_required
def course_list_view(request):
    courses = Course.objects.all()
    return render(request, 'referral/course_list.html', {'courses': courses})

@login_required
def edit_course_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save(commit=False)
            course.modified_by = request.user
            course.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'referral/edit_course.html', {'form': form})

