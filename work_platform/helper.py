"""
    Helper functions for the work_platform api's
    It has only context of work_platform apis
"""
from work_platform.common import parse_skill, strip_bad_character, strip_lines


def get_clean_request(data):
    """Cleans Jobs and Titles from bad character"""

    if data["title"] and type(data["title"]) == "str":
        data["title"] = clean_title(data["title"])

    if data["skills"] and type(data["skills"]) == "list":
        data["skills"] = clean_words(data["skill"])
        data["skills"] = clean_skills(data["skills"])

    return data

def clean_title(title):
    stripped_title = strip_bad_character(title)
    stripped_title = strip_lines(title)
    return stripped_title

def clean_skills(skills):
    skills_data = []
    for skill in skills:
        temp = strip_bad_character(skill)
        temp = strip_lines(skill)
        skills_data.append(temp)
    return skills_data

def clean_words(skills):
    skills_data = []
    for skill in skills:
        skills.data.append(parse_skill(skill))
    return skills_data