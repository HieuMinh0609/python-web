from polls.models import Color
from django.db import connections
cursor = connections['default'].cursor()

def getAllColorByIdProduct (idProduct) : 
    return  Color.objects.raw("SELECT * FROM db_shopee_django.color where idProduct=%s",[idProduct])