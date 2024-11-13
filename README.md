# Django-REST-Framework-API-Project
Django REST API project for learning purposes.


## Steps

Assuming Python has been installed previously:


### Creation of Virtual Environment

Enter the following commands on a console placed in your project folder (using VSC console directly in my case):

```console
pip install virtualenv
py -m virtualenv venv
```


### Using the Virtual Environment

One option is to enter the following command:

`.\venv\Scripts\activate`

But for convenience, best option is to select the specific Python interpreter for out virtual environment. We can select it, on VSC, pressing "F1" and searching for "Python select interpreter". The adequate Python interpreter should be higlighted as the recommended one.


### Installing Django and DjangoREST frameworks

Enter the following commands:

```console
pip install django
pip install djangorestframework
```

### Start Django Project

Enter this command:

`django-admin startproject [project-name] .`

> [!NOTE]
> Notice the use of ".". If we are working in a folder already, that avoids the need to create an extra folder.