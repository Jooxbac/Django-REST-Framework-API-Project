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


5. ### Start and Add App to settings.py

Enter this command:

```console
py manage.py startapp [app-name]
```

Then, go to `settings.py` inside the folder of our django project and add the name of the created app to the list of `INSTALLED_APPS`.


6. ### Add REST Framework Module to settings.py

Just like in the previous step: go to `settings.py` inside the folder of our django project and add `rest_framework` to the list of `INSTALLED_APPS`.


7. ### Running the Project Into a Local Server

We can use the following command to run our project in a local server whenever we want:

```console
py manage.py runserver
```

Sepecifications about the IP adress and port will be displayed after entering the command.


## Development Steps


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


4. ### Creating and Adding URLs

Create urls.py file in the app's folder. Import routers module from Django REST and our before created ModelViewSet, create a router, generate the CRUD routes and add them to the files URLs in urlpatterns:

![URLs generation example in urls.py](/images/04_urls_app.jpg)

Then, in project's folder `urls.py` file import include module and add the app's routes by using `include()` into the urlpatterns of this file.

![Adding URLs to urls.py in project's folder](/images/05__urls_project.jpg)


## Accesing the API

If we enter the `py manage.py runserver` command, now we can access to the "api/projects/" route of the project, where we can view, write, update and delete data.

![Adding URLs to urls.py in project's folder](/images/06_access.jpg)

If we want to access to a project's specific data, we just need to enter the id into the URL:

![Adding URLs to urls.py in project's folder](/images/07_access_by_id.jpg)


## Accesing the API Using a REST Client

VSC extension Thunder Client. REST API Client Extension


## Deploy Using Render Cloud Application Platform

> [!WARNING]
> These steps are better followed directly from the [tutorial](https://www.youtube.com/watch?v=GE0Q8YNKNgs), what I encourage to do, as is needed to create accounts on external services and use these services, which I won't cover, etc.
> Information given below covers just general aspects and some troubleshooting.  

Create a [render.com](https://render.com/) account and use free trial
Create a git repository and edit .gitignore (I didn't edit .gitignore as recommended, which may had affected to the database data showing when I deployed the app)

The tutorial follows some of the [Deploy Django](https://docs.render.com/deploy-django) Render's article. From here we should pay attention to the following sections: [Adding basic security](https://docs.render.com/deploy-django#adding-basic-security), [Adding PostgreSQL support](https://docs.render.com/deploy-django#adding-postgresql-support), [Set up static file serving](https://docs.render.com/deploy-django#set-up-static-file-serving), [Create a build script](https://docs.render.com/deploy-django#create-a-build-script).

Some of the commands needed while following the Render's article are:

`pip install whitenoise[brotli]` for installing whitenoise, as Render cannot serve static files

`pip install gunicorn` for installing gunicorn, a Web Server Gateway Interface (WSGI) which Render uses for deployment.

`pip freeze > requirements.txt` for creating requirements.txt including all dependencies: 


### Troubleshooting

While following Adding PostgreSQL support section, I had trouble using the `pip install psycopg2-binary` command, here is what I did to resolve it:

- Installed [PostgrSQL](https://www.postgresql.org/download/).
- Added the PostgreSQL installation folder route plus "/bin" to the systems `$PATH`.
- Then, anyways, used the command: `pip install psycopg2-binary --global-option=build_ext --global-option="-I [folder location for PostgreSQL + /bin]` (in my case, it showed another error related with C++).
- Installed [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/), selecting the option labelled with "Desktop development with C++".

I also had trouble when trying to change build.sh permissions, as I was using Windows and changing permissions don't work the same as Linux there. Using the `chmod a+x build.sh` command seemed useless, as `ls -l build.sh` showed no execution permissions for the file. Anyways, I tried following along the tutorial and everything worked fine.