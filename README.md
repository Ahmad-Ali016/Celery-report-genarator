# Asynchronous CSV report generation

This project implements asynchronous CSV report generation using Django, 
Celery, and Redis. Instead of generating reports during an HTTP request 
(which can block the server), the system delegates the work to a 
background worker.

When a client calls the API endpoint, Django queues a task in Redis, and 
a Celery worker processes the task asynchronously. The task generates a 
CSV file containing randomly generated data and saves it to a local 
folder. The API immediately returns a task ID, which can later be used 
to check the task status and retrieve the generated file path.

The workflow enables non-blocking report generation, making it suitable 
for handling long-running operations such as exporting large datasets.

## Key capabilities:

- Trigger background CSV report generation via API 
- Process tasks asynchronously with Celery 
- Use Redis as the message broker and result backend 
- Generate unique CSV files with random data 
- Poll task status using a task ID 
- Retrieve the generated report location once completed 
- This setup demonstrates a common backend architecture for scalable 
task processing in Django applications.

----------------------------------------------------------------------

## System Summary

Implemented an asynchronous CSV report generation system using Django 
+ Celery + Redis.
 
### Components

#### Django

- Provides API endpoints to trigger background jobs. 
- Handles HTTP requests from clients (Postman).

#### Celery

- Executes heavy tasks asynchronously (CSV generation). 
- Prevents blocking the Django request/response cycle.

#### Redis

- Works as:
  - Message broker (task queue)
  - Result backend (stores task results)

----------------------------------------------------------------------


## Tech Stack

- Django
- Celery
- Redis
- Faker (for random data generation)

---


## Architecture

Client → Django API → Celery Task → Redis Queue → Celery
Worker → CSV File

Celery handles long-running tasks in the background, keeping 
Django API responses fast.

---


## Features

- Asynchronous report generation
- Background task processing
- Random dataset generation
- Task status polling
- Unique CSV file generation

---

## Workflow

### 1- Trigger CSV Generation

**Endpoint:**

    GET /reports/generate_csv_task/

**Response example:**

```json
{
  "task_id": "uuid"
}
```

### 2- Check Task Status

**Endpoint:**

    GET /reports/generate-csv-status/<task_id>/

### Possible responses:

**Pending:**

```json
{
  "status": "pending"
}
```

**Completed:**

```json
{
  "status": "finished",
  "file": "report_20260311_021533.csv",
  "path": "generated_csvs/report_20260311_021533.csv"
}
```

### 3- CSV Generation Task

**Celery task:**

    reports.tasks.generate_csv_task

**Responsibilities:**

- Creates generated_csvs/ folder 
- Generates a unique CSV file 
- Uses random data (Faker + random module)
- Writes rows into CSV 
- Returns the file path

**Example CSV:**

```csv
ID,Name,Score
1,John Doe,84
2,Sarah Smith,91
3,Michael Brown,73
```

----------------------------------------------------------------------

## URLs in the System

| Endpoint                                  | Purpose                                         |
| ----------------------------------------- | ----------------------------------------------- |
| `/reports/generate_csv_task/`             | Trigger asynchronous CSV generation             |
| `/reports/generate-csv-status/<task_id>/` | Check Celery task result                        |
| `/reports/generate-csv/`                  | Older trigger endpoint (can be kept or removed) |

