from polls.models import Rate
from django.db import connections
cursor = connections['default'].cursor()

def saveRate(idproduct,value,iduser):
    cursor.execute('''INSERT INTO rate (idProduct,idUser,value) 
        VALUES (%s,%s,%s)''',[idproduct,iduser,value])