from django.db import models

# Create your models here.
class FloodWarning(models.Model):
    area=models.CharField(max_length=100)
    warning_level=models.CharField(max_length=100)
    alert_date=models.DateTimeField()

    def __str__(self):
        return f"Flood warning in {self.area}: {self.warning_level}"
    
class UserReport(models.Model):
    report_type=models.CharField(max_length=100)
    report_date=models.DateTimeField(auto_now_add=True)
    description=models.TextField()

    def __str__(self):
        return f"Report: {self.report_type} on {self.report_date}"