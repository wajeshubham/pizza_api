**REST api using DjangoREST framework**



_open up your terminal and create virtual environment (make sure you are in the project's directory)_

`pip install virtualenv`

`virtualenv env`

`env\Scripts\activate.bat`

now you can see _**env**_ file in your project's directory

_Now install all the necessary packages_

`pip install -r requirements.txt`



_**Configure your PostgreSQL database**_

**please go to line no 85 in pizza_api/settings.py and add necessary configs in the 'DATABASES'**

After setting up the database you have to make migrations to the database, run following commands to make migrations

`python manage.py makemigrations`

`python manage.py migrate`

_**Now you can run the project by following command**_

`python manage.py runserver`

_**ENDPOINTS (URLS) :**_

create a pizza order:
(fields uou have to pass in postman:

customer_name,

size,

shape,

toppings (comma separated words, e.g. : Corn,Tomato,Mushroom,Olives,Onion)
)

`POST http://127.0.0.1:8000/pizza/`

get all pizza orders:

`GET http://127.0.0.1:8000/pizza/`

get pizza order by size: (size options: (small/medium/large))

`GET http://127.0.0.1:8000/pizza/size/<size_you_want>/`

get pizza order by shape: (shape options: (regular/square))

`GET http://127.0.0.1:8000/pizza/size/<shape_you_want>/`

delete a pizza order: (you have to pass id of pizza on the place of <id_of_pizza>)

`DELETE http://127.0.0.1:8000/pizza/delete/<id_of_pizza>/`