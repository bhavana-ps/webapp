RUNNING THE PROJECT:

1. Recommended to use a virtual environment
1. Install the requirements 
	
	pip install -r requirements.txt
1. Apply the migrations 
	
	python manage.py makemigrations
	
	python manage.py migrate
1. Install Redis from 	https://github.com/microsoftarchive/redis/releases 
1. Run the server python manage.py runserver
	
	or run the server and worker separately using 
	
	python manage.py runserver --noworker
	
	and in a different terminal run the worker using
	
	python manage.py runworker
