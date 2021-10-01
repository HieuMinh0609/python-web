from polls.models import Category
from django.db import connections
cursor = connections['default'].cursor()

def getAllCategory () : 
    return  Category.objects.all() 

def getAllNameCategory() :
    cursor.execute("SELECT id,name FROM db_shopee_django.category limit 8")
    rows = cursor.fetchall()
    return rows