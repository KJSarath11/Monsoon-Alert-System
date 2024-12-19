from django.urls import path
from .views import flood_warning,user_report,submit_report

urlpatterns = [
    path('flood_warining/',flood_warning,name="flood_warning"),
    path('user_report/',user_report,name="user_report"),
    path('submit_report/',submit_report,name="submit_report"),
]