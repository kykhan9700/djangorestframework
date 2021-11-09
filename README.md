# FizzBuzz Api using Django Rest Framework


## API Documentation
https://fizzbuzz.docs.apiary.io/

## Project Setup


Create a virtual environment to isolate your application dependencies from any other project. 

```
python3 -m venv env
source env/bin/activate
```

Now that we're inside a virtual environment, we can install our package requirements.

```
pip install django
pip install djangorestframework
pip install django-filter
```

We also need to create Initial migration for our FizzBuzz model and sync the database for the first time.

``` 
python3 manage.py migrate
```

After successful migration we need to now create a superuser to access the API. 

```
python3 manage.py createsuperuser --email admin@example.com --username admin
```

Once the user is created we can now run the server.

```
python3 manage.py runserver
```

We can now access our API, both from the command-line, using tools like postman or Or directly through the browser, by going to the URL http://127.0.0.1:8000/fizzbuzz

If you're working through the browser, make sure to login using the control in the top right corner.

Great, that was easy!



