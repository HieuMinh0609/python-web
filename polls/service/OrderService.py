from polls.models import Orders
from django.db import connections
cursor = connections['default'].cursor()


# ENUM : status : 0 - Chờ thanh toán 
# status : 1 - Đã thanh toán
# statú : 2 - Đơn hủy
def getAllOrderByIdUser (iduser) : 
    cursor.execute("SELECT * FROM db_shopee_django.orders where idUser =%s",[iduser])
    rows = cursor.fetchall()
    return rows

def getAllOrderByIdUserAndStatus(iduser,status):
    cursor.execute("SELECT * FROM db_shopee_django.orders where idUser =%s and status=%s",[iduser,status])
    rows = cursor.fetchall()
    return rows


def getAllItemInCart(idcart):
    cursor.execute("SELECT * FROM db_shopee_django.infomationcart where idcart = %s",[idcart])
    rows = cursor.fetchall()
    return rows

def updateOrder(idorder):
    cursor.execute('''update db_shopee_django.orders set status=%s where id=%s''',[2,idorder])
    