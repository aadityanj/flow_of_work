# Assignment
Assignment project has been done in python3.7 (Django Rest Framework) and sqlite as datastore

## Features
- Login & Logout with JWT
- Post JobTitles and Skills 
- Search JobTitles by Skills
- Search Skills by JobTitle

####  Project Structure in abstract level
1. flow_of_work
    - app settings
    - urls
2. work_platform(app)
    - migrations
    - models.py (Have all the table information)
    - helper.py (Helper functions to validate and parse request)
    - common.py (Common utilty functions)
    - serializer.py (Helps Serialize and Deserialize the request and response, it also valid against table constracints and raise right exceptions)
    - views.py (Entry point for all the apis after routed from url)
    - logger.py (Log all the info in single place)
    - urls.py (Router)
3. gitignore, sqlite, requirements.txt


Assignment project requires the following
- Python3.7 

Install the packages to start the server.

```sh
cd flow_of_work
pip install -r requirements.txt
python manage.py runserver
```

For production environments...
```sh
python manage.py runserver --settings=prod.settings.py
```

### API Links
After starting the projects, you can easily test the below apis with the help of Django's document package. Also have included all the sample request to test
 - http://localhost:8000/api/v1/create_job
 - http://localhost:8000/api/v1/search_job
 - http://localhost:8000/api/v1/search_skills
Note - For easy testing, Have already added mock datas on it
Credentials - adithya/Test@1234

### What would i do if have more time ?
1. Convert all skills and jobs in smallercase to reduce duplicates accross the user ( need to think through) 
2. Create apis to do bulk inserts of skills and jobs
3. Include pagination
4. Would add Custom Exceptions
5. Enable logout feature and invalidate the jwt token
6. Dockerize the application
7. Analyse and enhance the feature 
