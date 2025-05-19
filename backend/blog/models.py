from django.db import models


class FeedbackForm(models.Model):
    name=models.CharField(blank=True, max_length=100)
    email=models.EmailField(blank=True)
    message=models.TextField(blank=False)
    submitted_at=models.DateTimeField(auto_now_add=True)
