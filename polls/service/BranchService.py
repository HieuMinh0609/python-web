from polls.models import Branch, Product
from django.db import connections
cursor = connections['default'].cursor()

def getAllBranch () : 
    return  Branch.objects.all() 

def getAllProductByBranch(id):
    return Product.objects.raw('SELECT * FROM db_shopee_django.product where idBranch=%s',[id])