from django.urls import path
from reports.views import trigger_csv_task, check_csv_task, trigger_generate_csv_task

urlpatterns = [
    path("generate-csv/", trigger_csv_task, name="generate_csv"),
    path("generate-csv-status/<str:task_id>/", check_csv_task, name="check_csv_task"),
    path("generate_csv_task/", trigger_generate_csv_task, name="generate_csv_task"),
]