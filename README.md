# Django-Task
- Job Interview task: web application created with Django framework
- Application contains form that you can write informations to, such as: Name, email and IČO number. Then you can store those informations by clicking button.
- Email and IČO number are validated if the format of those is right and then if record is already stored in database. IČO number has one more special check wich is provided by external register to check if this number is real and not random fake.
- After the clicking button, you will be informed by propper message if storing info into database was successful or no.

# Language:
- Python            >= 3.7.1

# Packages:

- pip               >= 21.1.1
- Django            >= 3.2.3

- xmltodict         >= 0.12.0
- urllib3           >= 1.26.4
- typing-extensions >= 3.10.0.0
- sqlparse          >= 0.4.1
- setuptools        >= 56.2.0
- pytz              >= 2021.1
- asgiref           >= 3.3.4

# IDE used:
- PyCharm

# Installation:
## PyCharm users:
- For packages: 
In PyCharm IDE you can simply create new project and use build-in Python Packages instaler for searching and installing packages that you need to build your project.
- For this application: There is a build in terminal which you can use to navigate through your file system into a project folder that you got from this repo, you need to make sure that you are in folder that has manage.py file in it and then run command: ```python manage.py migrate```.
It will check INSTALLED_APPS setting and creates any necessary database tables. Then we use command: ```python manage.py runserver```. It will start dev server where this application is hosted. 
## Standard terminal users:
- For packages: You need to make sure that you have up to date pip, then you can install those packages by instruction that are listed in their description
- For this application: Use your standard OS terminal to navigate  through your file system into a project folder that you got from this repo, you need to make sure that you are in folder that has manage.py file in it and then run command: ```python manage.py migrate```. It will check INSTALLED_APPS setting and creates any necessary database tables. Then we use command: ```python manage.py runserver```. It will start dev server where this application is hosted. 

## Database:
- For this app was used SQLite which is build-in Django framework

## Important: 
### For using database in this repo:
- If you using database file wich is part of this repo then just run command given in previous articles to check if everything is OK, then run server with previously given command aswell. 
- Credentials for Django amin are:
- name: admin
- pass: heslo123
### For using fresh-new database
- If you are not using this database contained in this repo run command given in previous articles (```python manage.py migrate```) to create a new one.
- Then if you want to have access to django admn site you need to create superuser for your fresh-new database
- To do so just write command ```python manage.py createsuperuser```
- Then you will be asked for add name of supersuer acc and password
- After a creation of superuser for your fresh-new database just run command for starting server ```python manage.py runserver``` and check urls down below.

## URLs:
- This app can be found at: http://127.0.0.1:8000/ukol 
- Django admin site can be found at: http://127.0.0.1:8000/admin
