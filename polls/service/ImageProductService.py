from polls.models import Imageproduct
from django.db import connections
cursor = connections['default'].cursor()

def getAllImageByIdProduct (idProduct) : 
    return  Imageproduct.objects.raw("SELECT * FROM db_shopee_django.imageproduct where idProduct=%s",[idProduct])