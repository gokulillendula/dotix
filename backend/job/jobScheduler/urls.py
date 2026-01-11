from django.urls import path,include
from .views import CreateJob, ListJobs, JobDetail, RunJob,DeleteJob
urlpatterns = [
    path("jobs", CreateJob.as_view()),
    path("jobs/list", ListJobs.as_view()),
    path("jobs/<int:id>", JobDetail.as_view()),
    path("jobs/delete/<int:id>", DeleteJob.as_view()),
    path("run-job/<int:id>", RunJob.as_view()),
]