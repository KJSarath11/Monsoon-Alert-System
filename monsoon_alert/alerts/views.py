from django.shortcuts import render
from django.http import JsonResponse
from .models import FloodWarning,UserReport
from django.views.decorators.csrf import csrf_exempt
import json

#Create your views here.
#!Flood Warning view
# Fetches all FloodWarning objects from the database.Renders them to an HTML template (flood_warnings.html).
def flood_warning(request):
    warning=FloodWarning.objects.all()
    return render(request,"alerts/flood_warning.html",{"warning":warning})

#! User_Report view
# Fetches all UserReport objects from the database.Renders them to an HTML template (user_reports.html).
def user_report(request):
    reports=UserReport.objects.all()
    return render(request,"alerts/user_report.html",{"reports":reports})

#! Submit Report view
# Retrieves all user reports from the UserReport model.Displays the data in a template.
@csrf_exempt
def submit_report(request):
    if request.method=="POST":
        try:
            data=json.loads(request.body)
            report_type=data.get("report_type")
            description=data.get("description")

            if not report_type or not description:
                return JsonResponse({"error":"Invalid Data Provided"},status=400)
            
            UserReport.objects.create(report_type=report_type,description=description)
            return JsonResponse({"message":"Report Submitted Successfully"},status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({"error":"Invalid Json format"},status=400)
    return JsonResponse({"error":"Only POST requests are allowed"},status=405)
