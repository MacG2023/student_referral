from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    path('agents/', views.agent_list_view, name='agent_list'),
    path('agents/create/', views.create_agent_view, name='create_agent'),
    path('agents/<int:agent_id>/', views.edit_agent_view, name='edit_agent'),
    
    path('add-student/', views.add_student_view, name='add_student'),
    path('students/', views.student_list_view, name='student_list'),
    path('edit-student/<int:pk>/', views.edit_student_view, name='edit_student'),
    path('add-institution/', views.add_institution_view, name='add_institution'),
    path('institutions/', views.institution_list_view, name='institution_list'),
    path('edit-institution/<int:pk>/', views.edit_institution_view, name='edit_institution'),
    path('add-admission/', views.add_admission_view, name='add_admission'),
    path('admissions/', views.admission_list_view, name='admission_list'),
    path('edit-admission/<int:pk>/', views.edit_admission_view, name='edit_admission'),
    path('add-course/', views.add_course_view, name='add_course'),
    path('courses/', views.course_list_view, name='course_list'),
    path('edit-course/<int:pk>/', views.edit_course_view, name='edit_course'),
]
