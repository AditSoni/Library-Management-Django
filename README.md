# Library-Management-Django
A simple Library Management System with basic CRUD operations

Python version used == Python 3.7.8

## How To Run
1. pip install -r requirements.txt to install all dependencies
2. while in base directory ,the directory with manage.py  ,Run following in terminal

    -->python3 reset_db.py  ,this setups database
    
    -->python3 populate.py  ,this fills models with fake data
    
    -->python3 manage.py createsuperuser  ,this creates the user
    
  3. Now Run  -->python3 manage.py runserver  and open the link


### Optional Future updates
1. Current system has infinite stock,ie,a book can be issued any number of times
2. Add Users who can view books and request issue
3. Add Images of Book Covers,Person ID while adding records
4. Limit Number of Books currently issued by Person
