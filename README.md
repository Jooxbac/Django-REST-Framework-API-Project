# Django-REST-Framework-API-Project
Django REST API project for learning purposes. It has been developed following this [tutorial](https://www.youtube.com/watch?v=GE0Q8YNKNgs).
Below I explain some of the steps followed, as a way to internalize what has been learned and as notes that will be useful in case I want to carry out a new similar project.


## Setup Steps

Is assumed Python has been installed previously and the used IDE is Visual Studio Code (VSC).


1. ### Creation of Virtual Environment

Enter the following commands on a console placed in your project folder (using the console offered by VSC directly):

```console
pip install virtualenv
py -m virtualenv venv
```


2. ### Using the Virtual Environment

One option is to enter the following command:

```console
.\venv\Scripts\activate
```

For convenience, best option is to select the specific Python interpreter for out virtual environment. We can select it, on VSC, pressing "F1" and searching for "Python select interpreter". The adequate Python interpreter should be higlighted as the recommended one.


3. ### Installing Django and Django REST Frameworks

Enter the following commands:

```console
pip install django
pip install djangorestframework
```


4. ### Start Django Project

Enter this command:

```console
django-admin startproject [project-name] .
```

> [!NOTE]
> Notice the use of ".". If we are working in a folder already, that avoids the need to create an extra folder.


5. ### Start and Add App to Settings.py

Enter this command:

```console
py manage.py startapp [app-name]
```

Then, go to `settings.py` inside the folder of our django project and add the name of the created app to the list of `INSTALLED_APPS`.


6. ### Add REST framework module to Settings.py

Just like in the previous step: go to `settings.py` inside the folder of our django project and add `rest_framework` to the list of `INSTALLED_APPS`.


7. ### Running the project into a local server

We can use the following command to run our project in a local server whenever we want:

```console
py manage.py runserver
```

Sepecifications about the IP adress and port will be displayed after entering the command.


## Development Steps

> [!WARNING]
> These steps are better followed directly from the [tutorial](https://www.youtube.com/watch?v=GE0Q8YNKNgs), what I encourage to do, as is needed to modify files, create accounts on external services, etc.
> Information given below covers just general aspects and some troubleshooting.  


1. ### Creating Models

In the app's folder we can create models, that will be converted to database tables, adding them to the `models.py` file. Each class will be a table, and each attribute will be a column. id column will be created by default. We can specify the type of data for each attribute using `models` class methods (eg: models.CharField()).

![Model creation example in models.py](/images/01_models.jpg)

To migrate this models to a database we must enter the following commands:

```console
py manage.py makemigrations
py manage.py migrate
```

`makemigrations`command scans models changes on the apps registered on the projects `INSTALLED_APPS`, on `settings.py`, and create a .py file in the app's migrations folder, describing the changes to be made to the database.
`migrate`command applies the specified changes: reads pending migrations files and executes them orderly to synchonize the models with the database, modifying the actual structure of the database. It also updates the Django's migrations register, to make sure this is applied just once.


2. ### Creating Serializer

In the app's folder we create a `serializers.py` file. There, we import Django REST's serializers and our before created model and create a serializer:

![Serializer creation example in serializers.py](/images/02_serializers.jpg)

Django REST serializers transform complex data (like instances of Django models) to smple Python types that can be then easily rendered to formats like JSON or XML, that are more suitable to be send as a response when using an API. They also perform the opposite operation: transforming simple data to complex data.
Moreover, serializers will allow us to call an special model of REST framework ([ModelSerializer](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer)).

Take a look at docs for more info on [Django's REST framework serializer](https://www.django-rest-framework.org/api-guide/serializers/).


3. ### Creating ViewSet

Create api.py file in the app's folder. First, import our Project model and our ProjectSerializer serializer and viewsets and permissions from Django REST. Then, create a ViewSet ([ModelViewSet](https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset)), which has CRUD functionalities, and where we can specify data to be consulted, permissions for viewing the data and the serializer used to transform the data:

![ViewSet creation example in api.py](/images/03_api.jpg)


4. ### Creating urls. py

Routes

Add app routes to the project by using `include()` into the urlpatterns of `urls.py` file into the project folder.


5. ### Creating urls. py

Content


### Using REST client

VSC extension Thunder Client. REST API Client Extension


### Deploy using render.com

Create account and use free trial
Create a git repository and edit .gitignore

https://docs.render.com/deploy-django
Follow Adding basic security section

Follow Adding PostgreSQL support section

`pip install dj-database-url psycopg2-binary`

Had different problems installing psycopg2-binary:

What I did to resolve it:

- Install PostgrSQL (https://www.postgresql.org/download/)
- Added the installation folder plus "/bin" to the `$PATH`
- Tried using the command: `pip install psycopg2-binary --global-option=build_ext --global-option="-I [folder location for PostgreSQL + /bin]` (In my case, it shows another error related with C++)
- Installed [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/). We must select the option labelled with "Desktop development with C++".


Follow Set up static file serving section
As render cannot serve static files:
Install whitenoise
`pip install whitenoise[brotli]`

Follow Create a build script section

Open a git bach on VSC and enter `chmod a+x build.sh`, after creating this file. Problems in Windows... Using ls -l on build.sh shows the permissions remain the same...

`pip install gunicorn`

Create requirements.txt: `pip freeze > requirements.txt`