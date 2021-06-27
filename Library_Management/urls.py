"""Library_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('issued/', views.issued, name='issued'),
    path('persons/', views.persons, name='persons'),
    path('', include('django.contrib.auth.urls')),
    path('books/delete-book/<task_id>', views.delete_book, name='delete_book'),
    path('persons/delete-person/<task_id>', views.delete_person, name='delete_person'),
    path('issued/delete-issued/<task_id>', views.delete_issued, name='delete_issued'),
    path('books/edit-book/<task_id>', views.edit_book, name='edit_book'),
    path('books/edit-person/<task_id>', views.edit_person, name='edit_person'),
    path('books/edit-issued/<task_id>', views.edit_issue, name='edit_issued'),
]
