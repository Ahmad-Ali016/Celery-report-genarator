import os
from celery.result import AsyncResult
from django.http import JsonResponse
from .tasks import generate_csv, generate_csv_task


# Create your views here.

def trigger_csv_task(request):
    task = generate_csv.delay()
    return JsonResponse({"task_id": task.id})

def check_csv_task(request, task_id):
    result = AsyncResult(task_id)
    if result.ready():
        # Task finished
        file_path = result.get()
        file_name = os.path.basename(file_path)
        return JsonResponse({
            "status": "finished",
            "file": file_name,
            "path": file_path
        })
    else:
        return JsonResponse({"status": "pending"})

def trigger_generate_csv_task(request):
    task = generate_csv_task.delay()
    return JsonResponse({"task_id": task.id})