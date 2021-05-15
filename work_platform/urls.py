from work_platform.views import create_job_and_skills, search_by_job, search_by_skills
from django.urls import path

urlpatterns = [
    path('create_job', create_job_and_skills),
    path("search_job", search_by_job),
    path("search_skills", search_by_skills)
]