# Django-REST-Framework-API-Project
Django REST API project for learning purposes. It has been developed following this [tutorial](https://www.youtube.com/watch?v=GE0Q8YNKNgs).
Below I explain some of the steps followed, as a way to internalize what has been learned and as notes that will be useful in case Iwant to carry out a new similar project.


## Setup Steps

Assuming Python has been installed previously:


1. ### Creation of Virtual Environment

Enter the following commands on a console placed in your project folder (using VSC console directly in my case):

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


3. ### Installing Django and DjangoREST Frameworks

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

Then, go to `settings.py` inside the folder of our django project and add the name of the created app to the list of "INSTALLED_APPS".

6. ### Add REST framework module to Settings.py

Just like in the previous step: go to `settings.py` inside the folder of our django project and add "rest_framework" to the list of "INSTALLED_APPS".

7. ### Running the project into a local server

We can use the following command to run our project in a local server whenever we want:

```console
py manage.py runserver
```

Sepecifications about the IP adress and port will be displayed after entering the command.


## Development Steps

1. ### Creating Models

Inside the app folder, we can create models, that will be converted to tables, on the `models.py` file.
To migrate this models to a database we must enter the following commands:

```console
py manage.py makemigrations
py manage.py migrate
```

> [!NOTE]
> Below sections are pending completion

2. ### Creating serializers.py

Inside the app folder we create a `serializers.py` file. Serializers allow us to call an special model of REST framework.

<!-- UserViewSet, es una forma de convertir los datos de Python en JSON, y seleccionar quien podrá ver los datos. -->


3. ### Creating api.py


4. ### Creating urls. py

Routes

Add app routes to the project by using `include()` into the urlpatterns of `urls.py` file into the project folder.

5. ### Creating urls. py