from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .candidate import Candidate
from .job_position import JobPosition


class ScreeningResult(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='screening_results')
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE, related_name='screening_results')
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    strengths = models.JSONField(default=list)
    missing_skills = models.JSONField(default=list)
    recommendation = models.CharField(max_length=7, choices=[
        ('proceed', 'Proceed'),
        ('hold', 'Hold'),
        ('reject', 'Reject'),
    ])
    summary = models.TextField()
    raw_report = models.JSONField(default=dict, blank=True)
    generated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'screening_results'
        ordering = ['-generated_at']

    def __str__(self):
        return f"{self.candidate.full_name} - {self.score}"