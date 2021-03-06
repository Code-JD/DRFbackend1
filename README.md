# DRFbackend1

This is the backend API for Kandu

- Here is the link to the frontend repo [DRFfrontend1](https://github.com/Code-JD/DRFfrontend1)

- [YouTube Tutorial](https://www.youtube.com/playlist?list=PLOLrQ9Pn6caw0PjVwymNc64NkUNbZlhFw)

First we start the Virtual Environment

```python
py -m venv venv
```

Then we Activate the virtual environment we created called ``venv``

```python
venv\Scripts\activate
```

---

---

<div align='center'>

## ~~~  Pro-Tip  ~~~

</div>

Use tab to auto complete this command, instead of typing `venv\Scripts\activate` you can press the `V` key then the `TAB` key. Now you have `venv\` typed out with only pressing two keys. Finish the command with 4 more keystrokes. `S`+`TAB` `A`+`TAB`. There you go just 6 keystokes (`V`+`TAB`+`S`+`TAB`+`A`+`TAB`+`ENTER`), technically that's 7 if you count hitting the Enter key at the end, to start the virtual environment. You are now a Hacker, welcome to the club.

---

---

Then we update pip

```python
python -m pip install --upgrade pip
```

Then we install Django

```python
pip install django
```

Create a new Project with ```django-admin``` inside the current folder. We will call the Project ```core``` and use the ```.``` at the end to install in the current directory.

```python
django-admin startproject core .
```

Now we run the `startapp` script, one for the Kandu app and one for the api

```python
manage.py startapp kandu 
manage.py startapp kandu_api
```

Then we connect the urls from these two apps to the `core` Django Project

In the `urls.py` file inside the `core` directory add the `include` import and add the two paths from the apps we created in the `urlpatterns`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kandu.urls', namespace='kandu')),
    path('api/', include('kandu_api.urls', namespace='kandu_api')),
]
```

Install Django REST Framework

```python
pip install djangorestframework
```

Install Coverage for Testing

```python
pip install coverage
coverage run --omit='*/venv/*' manage.py test
coverage html
```

```python
pip install django-cors-headers
