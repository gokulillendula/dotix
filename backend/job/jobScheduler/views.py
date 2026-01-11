from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import JobSerializer
from .models import Job
import threading
from .runner import run_job
# Create your views here.

class CreateJob(APIView):
    def post(self, request):
        serializer = JobSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status="pending")
        return Response(serializer.data)
class ListJobs(APIView):
    def get(self, request):
        jobs = Job.objects.all().order_by("-createdAt")
        return Response(JobSerializer(jobs, many=True).data)
class JobDetail(APIView):
    def get(self, request, id):
        job = Job.objects.get(id=id)
        return Response(JobSerializer(job).data)




class RunJob(APIView):
    def post(self, request, id):
        t = threading.Thread(target=run_job, args=(id,))
        t.start()
        return Response({"message":"Job started"})
