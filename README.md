# Django-Task
- Job Interview task: web application created with Django framework
- Application contains form that you can write informations to, such as: Name, email and IČO number. Then you can store those informations by clicking button.
- Email and IČO number are validated if the format of those is right and then if record is already stored in database. IČO number has one more special check wich is provided by external register to check if this number is real and not random fake.
- After the clicking button, you will be informed by propper message if storing info into database was successful or no.

# Language:
- Python            >= 3.7.1

# Packages:

- Django            >= 2.1.3
- requests          >= 2.25.1


# Used IDE:
- PyCharm

# Installation:
## PyCharm users:
- For packages: 
In PyCharm IDE you can simply create new project and use build-in Python Packages instaler for searching and installing packages that you need to build your project

## Standard terminal users:
- For packages: You need to make sure that you have up to date pip, then you can install those packages by instruction that are listed in their documentation

- How to install Django if you using standard terminal option: https://docs.djangoproject.com/en/3.2/intro/install/

## Database:
- For this app was used SQLite which is build-in Django framework

## Important: 
### For using database in this repo:
- If you using database file wich is part of this repo then just run commands: 
- ```python manage.py makemigrations ukol``` 
- ```python manage.py migrate```
- ```python manage.py runserver```

### Credentials for Django amin are:
- name: admin
- pass: heslo123

### For using fresh-new database
- If you are not using database contained in this repo run commands:
- ```python manage.py migrate```
-  ```python manage.py makemigrations ukol```
-  ```python manage.py migrate``` for second time.

- Then if you want to have access to django admin site you need to create superuser for your fresh-new database
- To do so just write command ```python manage.py createsuperuser```
- Then you will be asked for add name of supersuer acc and password
- After a creation of superuser for your fresh-new database just run command for starting server ```python manage.py runserver``` and check urls down below.

## URLs:
- This app can be found at: http://127.0.0.1:8000/ukol 
- Django admin site can be found at: http://127.0.0.1:8000/admin
