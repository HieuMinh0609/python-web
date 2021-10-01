from polls.models import Cart,Infomationcart,Orders,User,Payment
from django.db import connections
from polls.service.ProductService import *
import datetime
cursor = connections['default'].cursor()

def getItemInCart(iduser) :
    checkExist = Cart.objects.filter(iduser=iduser).filter(status=1)
    if(checkExist) :
        cart = checkExist[0]
        cursor.execute("SELECT *  FROM db_shopee_django.infomationcart where idCart=%s",[cart.id])
        rows = cursor.fetchall()
        return rows
    return []



def makeCart (iduser) : 
    cursor.execute('INSERT INTO cart (status,iduser) VALUES (%s,%s)',[1,iduser])
    cartNewInsert = Cart.objects.all().last()
    return cartNewInsert

def deleteItemInCart(iditem) :
    cursor.execute('DELETE FROM db_shopee_django.infomationcart WHERE id = %s ',[iditem])

def makeNewInfomationCartFromCart(idproduct,total_sold,iduser) :
    cartNewInsert  = makeCart(iduser)
    product = findById(idproduct)
    image = product.image 
    nameproduct = product.nameproduct
    price_sold = product.purchaseprice*product.saleprice
    realmoney = int(total_sold)*price_sold

    cursor.execute('''INSERT INTO infomationcart (idProduct,idCart,total_sold,image,price_sold,nameproduct,realmoney) 
    VALUES (%s,%s,%s,%s,%s,%s,%s)''',[idproduct,cartNewInsert.id,total_sold,image,price_sold,nameproduct,realmoney])
    return cartNewInsert


# hàm này đagn làm dở mai xây dựng tiếp 
# xây dựng giỏ hàng 
# lịch ngày mai 
# làm đăng ksy  tài khoản 
# chức năng đổi mật khẩu 
# chức năng xem lịch sử giao dịch 
# tích hợp AI
# Dự kiện thười gian khoảng 2 ->  2.5 ngày
def checkExistCart(idUser,idproduct,total_sold) :
    checkExist = Cart.objects.filter(iduser=idUser).filter(status=1)
    product =Product.objects.get(id=idproduct)
    price_sold = product.purchaseprice*product.saleprice
    total_product_now = product.quantity-product.amountsold
    if (total_product_now-int(total_sold)>0) :
        cart = None
        if(checkExist) :
            cart = checkExist[0]
            checkExistRowInInfomationCart = Infomationcart.objects.filter(idproduct=idproduct).filter(idcart=cart.id)
            if(checkExistRowInInfomationCart) :
                row = checkExistRowInInfomationCart[0]
                total_sold_old = row.total_sold
              
                total_sold_new = total_sold_old+int(total_sold)
                realmoney = total_sold_new*price_sold
                cursor.execute('''update infomationcart set total_sold=%s,realmoney=%s  where idCart= %s and idProduct=%s ''',[total_sold_new,realmoney,cart.id,idproduct])
            else :
              
                image = product.image 
                nameproduct = product.nameproduct
                realmoney = int(total_sold)*price_sold
                cursor.execute('''INSERT INTO infomationcart (idProduct,idCart,total_sold,image,price_sold,nameproduct,realmoney) 
                VALUES (%s,%s,%s,%s,%s,%s,%s)''',[idproduct,cart.id,total_sold,image,price_sold,nameproduct,realmoney])
                
        else :
            cart =makeNewInfomationCartFromCart(idproduct,total_sold,idUser)
        return True
    return False

def updateCart(iditem,total_sold):
    informationCart =  Infomationcart.objects.get(id=iditem)
    realmoney = int(total_sold)*informationCart.price_sold
    cursor.execute('''update infomationcart set total_sold=%s,realmoney=%s  where id= %s  ''',[total_sold,realmoney,iditem])

def checkoutMethod(iduser,idpayment):
    checkExist = Cart.objects.filter(iduser=iduser).filter(status=1)
    datetimenow = datetime.datetime.now()
    payment=Payment.objects.get(id=idpayment)
    user=User.objects.get(id=iduser)
    status = 0 
    if checkExist :
        cart = checkExist[0]
        if int(idpayment)==4 :
            status+=0
        else :
            status+=1
        order= Orders(datemade=datetimenow, iduser=user,idcart=cart,idpayment=payment,status=status)
        order.save()
        # cursor.execute('''INSERT INTO orders (datemade,idUser,idCart,idPayment) 
        #     VALUES (%s,%s,%s,%s)''',[datetimenow,iduser,cart.id,idpayment])
        cursor.execute('''update cart set status=%s where id=%s''',[0,cart.id])
        return 1
    return 0 
