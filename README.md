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
2) set configuration in setting.py 
3) create model Student. Create superuser
4) Create a serializer class in seprate file serializer.py 
5) Create a seprate application to send JSON data, which received by our app. my_seprate_app.py 
6) Write a view to receive data. And also send msg in JSON form if data insrted in db successfully. 

CRUD operation with API:
1) GET/READ
    1) create project drf3, app api 
    2) create Student(name, roll, city) model. create superuser.
    3) create serailizer class in serializer.py file.  
    4) create seprate application to send GET request for single id or all students. my_separate_app.py
    5) Write view. 
            get json data if any(id), 
            stream data, 
            get id of student if any, 
            get data from db, 
            serialize data (many =True),
            render data JSONRenderer().render() 
    6) create URL

    Cases Handled: 1) request.body can be empty so use if else     
                   2) models.object.all() can also be empty so use .exists()

2) POST/Create/insert: 
    1) create function create() in StudentSerializer class 
    2) Write a function in seprate application my_separate_app.py to send json data
    3) Write view.
            get json data, 
            stream data,
            parse data, 
            deserailize data (data = python_data), 
            add the deserialized data to db, 
            if any errors send the reponse

3) PUT/Update/partial/complete update:
    //Instead of PATCH we are using partial =True in DRF serializer 
    1) create function update in Studentserializer class
    2) Write a function in seprate application to make update request/ send data
    3) Write view.
        get json data,
        stream data,
        parse data, 
        get id of student from parse data,
        find the orginal model object with idz,
        for partial update 
            serialzie data serializer(originalModelObject, parsedPythonData, partial = True)
        for complete update 
            serialzie data serializer(originalModelObject, parsedPythonData)


