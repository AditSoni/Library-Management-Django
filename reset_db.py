import os
import shutil


base = os.getcwd()
if os.path.exists(base+'/library/migrations'):

    shutil.rmtree(base+'/library/migrations')
    print('Removed Migrations folder')

if os.path.exists(base+'/db.sqlite3'):

    os.remove(base+'/db.sqlite3')
    print('Removed DB file')

os.system('py manage.py makemigrations library')
os.system('py manage.py migrate')