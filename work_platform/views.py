from work_platform.logger import log
from work_platform.helper import clean_skills, clean_title, get_clean_request
from django.db.models import query
from rest_framework.decorators import api_view
from rest_framework import authentication, permissions, status
from rest_framework.response import Response
from work_platform.models import JobTitles, Skills
from work_platform.serializers import JobSkillSerializer, JobTitlesSerializer, SkillSerializer
from django.db.models import Count

# Create your views here.

@api_view(['POST'])
def create_job_and_skills(request):
    """
        Create Jobs title and required Skills
        Input Request {}
            eg: {
                title: "frontend"
                skills: ["html", "css"]
            }
        Returns 
            Created Jobs & Skills in the Input Request Format
    """
    try:
        data = request.data
    
        if len(data) > 0 and data["title"] and data["skills"]:
            data = get_clean_request(data)
            job_title_serializer = JobTitlesSerializer(data={"title":data["title"]})
            
            if job_title_serializer.is_valid():

                job_title = job_title_serializer.save()
                
                skills = SkillSerializer.get_or_create(data["skills"])
                
                job_title.skills.add(*skills)
                job_skill_serializer = JobSkillSerializer(instance=job_title)
                return Response(job_skill_serializer.data)
        
            return Response(job_title_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
 
        return Response({"message":
            "Missing title or skills"}, status = status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        log(
            request.user.id, 
            "create_job_skill", 
            e
        )
        return Response("Internal Server Error", status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def search_by_job(request):
    """
    List skills that are required for the job
    Input Query Params
        title:string (Job title)
        url?title=frontend
    Returns 
        [Skills]: List of skills
    """
    try:
        title = request.GET.get("title", None)
        if title is not None:
            title = clean_title(title)
            queryset = Skills.objects.filter(jobtitles__title=title)
            skill_serializer = SkillSerializer(instance=queryset,many=True)
            return Response(skill_serializer.data)
        
        return Response({"message":
            "Missing job_tile field in the Query Param"}, status = status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        log(
            request.user.id, 
            "search_by_job", 
            e
        )
        return Response("Internal server error", status = status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def search_by_skills(request):
    """
    List Jobs that are fit by the skills
    Input Request
        skills: obj
        eg {skills:["html", "css"]}
    Returns
        [JobTitles]: List of Jobs
    """
    try:
        skills = request.data.get('skills', None)

        if skills is not None:
            skills = clean_skills(skills)
            jobs = JobTitles.objects
            queryset = jobs.annotate(c=Count('skills')).filter(c=len(skills))
            for skill in skills:
                queryset = queryset.filter(skills__name=skill)
            job_serializer = JobTitlesSerializer(instance=queryset, many=True)
            return Response(job_serializer.data)

        return Response({"message": "Missing skills field in the Request"}, status = status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        log(
            request.user.id, 
            "search_by_skills", 
            e
        )
        return Response("Internal server error", status = status.HTTP_500_INTERNAL_SERVER_ERROR)