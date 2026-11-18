
from django.urls import path

from .views.department import CreateDepartmentAPIView
from .views.job_position import CreateJobPositionAPIView
from .views.candidate import CreateCandidateAPIView
from .views.resume import UploadResumeAPIView
from .views.screening_result import ViewScreeningResultAPIView
from .views.interview_question_set import ViewInterviewQuestionsAPIView


urlpatterns = [
    path('departments/', CreateDepartmentAPIView.as_view()),
    path('job-positions/', CreateJobPositionAPIView.as_view()),
    path('candidates/', CreateCandidateAPIView.as_view()),
    path('resumes/', UploadResumeAPIView.as_view()),
    path('screening-results/<int:pk>/', ViewScreeningResultAPIView.as_view()),
    path('interview-questions/<int:pk>/', ViewInterviewQuestionsAPIView.as_view()),
]
