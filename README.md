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

4) DELETE:
    Create a function in separate application to send data to delete records. 
    Write view.
    get json data,
    stream data,
    parse data,
    get id from parse data, 
    delete the model object with that id. 
    return response data deleted 


Validations:
1) Field Level Validation:
Add validation for roll no. If rollno > 200 then, raise error 'seats full'
    create function validate_roll(self, value):
    if rollno > 200: 
        if False return value
        else raise serializers.ValidationError('Seats Full')

2) Object Level Validation:
Add validation for name 'Amit' that his city must be 'Mumbai'
    create function validate(self, data):
        if name=='amit' and city != 'mumbai'
        if False return value
        raise serializers.ValidationError('Seats Full')

3) Validators:
Add validation that name must start with 'D'
    create function with any name 
    e.g.: def start_with_r(self,value)
    Mention function in serializer class field name
    e.g.: name = serilaizers.CharField(max_length=200, validators=[starts_with_r])


ModelSerializer:
1) create class StudentSerializer and use serializers.ModelSerialzer 
2) create class Meta inside StudentSerializer class 
3) Specify model name inside Meta class 
4) use fields = [] //to specifiy fields '__all__' for all fields 
5) use exclude = [] 


Special arguments in ModelSerializer class fields: 
1) class StudentSerializer(serializers.ModelSerializer):
	name = serializers.CharField(read_only=True)

    // read_only=True doesn't allow you to update name field 

2) Another 2nd way: 
	class Meta:
		model = Student
		fields = ['id', 'name', 'roll', 'city']
		read_only = ['name','roll']

3) Another 3rd way:
class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ['id', 'name', 'roll', 'city']
		extra_kwargs = {'name':{'read_only':True}}


Validation in ModelSerilaizer class:
    Used field level, object level, validatiors.


Function based api_view:
1) created proj drf8, app api
2) Used api_view to create api for simple GET, POST
3) Since using DRF now we have accessible browsable API. 

Function based api_view: CRUD
1) created proj drf9, app api 
2) created model, serializer, separate application.
3) created views. Written all CRUD operations using api_view.
4) Used my_separate_app for testing.


Class based APIView:
1) created proj drf10, app api 
2) created urls, model, serializer 
3) created views. Written all CRUD operations using APIView 
4) Used both my_separate_app, browsable api for testing.


GenericAPIView & Mixins:
1) created proj drf11, app api
2) created model, serializer
3) created urls, serializer. Written all CRUD operations using GenericAPIView & Mixins. 
    Separate class for each CRUD operation. 
4) Written all CRUD operations using GenericAPIView & Mixins, in 2 different class. 
    class seprated on basis of pk. One class uses pk (list, create) and other doesnt (retrive, update, destroy).
5) Used browsable api for testing.

Concrete API View Classes:
1) Created proj drf12, app api
2) Created model, serializer 
3) Created urls, serializer. Written all CRUD operations using Concrete API view classes. 
4) Finally created 2 classes which are enough to perform all CRUD operations.
5) Used browsable api for testing. 


Viewset & Router:
1) Created proj drf13, app api
2) Created model, serializer 