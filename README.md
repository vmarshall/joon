# JOON TakeHome

## Overview

[Takehome](https://docs.google.com/document/d/1ZqXTFazI782Ked0mD7UT2lac3O_Nang0/edit) 
## Setup

1. Unzip the repository

   `tar xvfz joon_takehome.tar.gz`
2. Create virtual environment

	`virtualenv -p python3 venv`
3. Install requirements
	
   `pip install -r requirements.txt`
4. Migrate the database
	
   `python manage.py migrate`
4. Load the data

	`python manage.py loaddata fixtures/dump.json`
5. 
5. Run the server

	`python manage.py runserver`

```bash

