from polls.models import Comment
from polls.service.ProductService import *
from django.db import connections
cursor = connections['default'].cursor()
import datetime

x = datetime.datetime.now()
def getAllCommentByIdProduct (idProduct) : 
    return  Comment.objects.raw("SELECT * FROM db_shopee_django.comment where idProduct = %s",[idProduct])

def saveComment(idproduct,comment,iduser,rate):
    cursor.execute('''INSERT INTO comment (idProduct,idUser,comment,dateComment,rate) 
        VALUES (%s,%s,%s,%s,%s)''',[idproduct,iduser,comment,x,rate])

def getListRecommentByIdComment(idComment):
    cursor.execute("SELECT * FROM db_shopee_django.recomment where idcomment = %s" ,[idComment])
    rows = cursor.fetchall()
    return rows 

def getInfoCommentAndRatingByIdProduct(idProduct):
    sql = """
    select bangphu.id as idcomment , bangphu.comment as comment , bangphu.dateComment as datecomment,
    bangphu.rate as rate , bangphu2.username as username , bangphu2.image as image 
    from 
    (SELECT * FROM db_shopee_django.comment where idProduct = %s) bangphu 
    left join 
    (select username , id ,image from user ) bangphu2 
    on bangphu.idUser = bangphu2.id
    """
    cursor.execute(sql,[idProduct])
    rows = cursor.fetchall()
    return rows

# đang làm dở
def listDataComment(idproduct) :
    listCommentByIdproduct = getInfoCommentAndRatingByIdProduct(idproduct)
    list_data = []
    for item in listCommentByIdproduct :
        list_object=[]
        key = []
        list_recommet_by_idcomment = getListRecommentByIdComment(item[0])
        key.append(item[0])
        key.append(item[1])
        key.append(item[3])
        key.append(item[4])
        key.append(item[5])

        list_object.append(key)
        list_object.append(list_recommet_by_idcomment)
        list_data.append(list_object)
    
    return list_data
