import time
import requests
from .models import Job
from django.conf import settings

WEBHOOK_URL = settings.WEBHOOK_URL

def run_job(job_id):
    job = Job.objects.get(id=job_id)

    # 1. Mark as running
    job.status = "running"
    job.save()

    # 2. Simulate work
    time.sleep(3)

    # 3. Mark as completed
    job.status = "completed"
    job.save()

    # 4. Fire webhook
    payload = {
        "jobId": job.id,
        "taskName": job.taskName,
        "priority": job.priority,
        "payload": job.payload,
        "completedAt": str(job.updatedAt)
    }

    response = requests.post(WEBHOOK_URL, json=payload)

    print("Webhook Status:", response.status_code)
    print("Webhook Response:", response.text)
