from django.db import models
from .department import Department

class JobPosition(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='job_positions')
    title = models.CharField(max_length=100)
    description = models.TextField()
    required_skills = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'job_positions'
        ordering = ['-created_at']

    def __str__(self):
        return self.title