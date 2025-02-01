Refer concept_django_rest_framework.txt for Theory. 
Readme consists code tracking. 

Serialization: 
1) created a project drf1, app api within it. 
2) installed djangorestframework - pip install djangorestframework
3) configured in settings.py INSTALLED_APPS = [ .., 'api','rest_framework'] 
4) created model Student, register in admin.py
5) created a serializer class StudentSerializer in a new file serializer.py. 
6) Written views to get student details. 
    - get student detail from db (create model object)
    - serialize data using StudentSerializer, get actual data using serialized_data.data
    - render serialized_data.data using JSONRenderer.render() 
    - return HttpResonse(json_data, content_type= 'application/json')
7) Used JSONResponse() insted of JSONRenderer.render() and HttpResponse 

Deserialization: 
Added deserialization concept in concept_django_rest_framework.txt
1) created a project drf2, app api within it. 