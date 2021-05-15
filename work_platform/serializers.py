"""
    Serializers
"""
from rest_framework import serializers
from .models import JobTitles, Skills

class SkillSerializer(serializers.ModelSerializer):
    """
        Serializer class for Skill Model
    """
    @staticmethod
    def get_or_create(skills):
        skills_data=[]
        for skill in skills:
            s, _ = Skills.objects.get_or_create(name=skill)
            skills_data.append(s)
        return skills_data
    
    class Meta:
        model = Skills
        fields = ['id', 'name']

class JobTitlesSerializer(serializers.ModelSerializer):
    """
        Serializer class for JobTitles Model
    """
    class Meta:
        model = JobTitles
        fields = ['id', 'title']

class JobSkillSerializer(serializers.ModelSerializer):
    """
        Netsted Custom Serializer to combine Jobtitle and Skills Model
    """
    skills = SkillSerializer(many=True)

    @staticmethod
    def getjob_by_skills():
        pass

    @staticmethod
    def getskills_by_job():
        pass

    class Meta:
        model = JobTitles
        fields = ['id', 'title', 'skills']