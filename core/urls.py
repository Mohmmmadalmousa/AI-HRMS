from django.urls import path

from .views.department import create_department
from .views.job_position import create_job_position
from .views.candidate import create_candidate
from .views.resume import upload_resume
from .views.screening_result import view_screening_result
from .views.interview_question_set import view_interview_questions


urlpatterns = [
    path('departments/', create_department),
    path('job-positions/', create_job_position),
    path('candidates/', create_candidate),
    path('resumes/', upload_resume),
    path('screening-results/<int:pk>/', view_screening_result),
    path('interview-questions/<int:pk>/', view_interview_questions),
]