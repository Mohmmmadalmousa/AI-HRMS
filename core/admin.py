from django.contrib import admin


from .models import (
    Department,
    JobPosition,
    Candidate,
    Resume,
    ScreeningResult,
    InterviewQuestionSet
)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    search_fields = ['name']


class JobPositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'department', 'created_at']
    search_fields = ['title']
    list_filter = ['department']


class CandidateAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'phone', 'created_at']
    search_fields = ['full_name', 'email']


class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'candidate', 'file', 'uploaded_at']
    search_fields = ['candidate__full_name']


class ScreeningResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'candidate', 'job_position', 'score', 'recommendation', 'generated_at']
    search_fields = ['candidate__full_name']
    list_filter = ['recommendation']


class InterviewQuestionSetAdmin(admin.ModelAdmin):
    list_display = ['id', 'candidate', 'job_position', 'screening_result', 'generated_at']
    search_fields = ['candidate__full_name']


admin.site.register(Department, DepartmentAdmin)
admin.site.register(JobPosition, JobPositionAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(ScreeningResult, ScreeningResultAdmin)
admin.site.register(InterviewQuestionSet, InterviewQuestionSetAdmin)
