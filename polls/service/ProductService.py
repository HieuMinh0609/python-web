from django.utils import translation
from polls.models import Product,Branch,Informationproduct,Rate
from django.db import connections

cursor = connections['default'].cursor()


def getListHotProduct () :
    return Product.objects.raw("SELECT  * FROM  db_shopee_django.product where hot = 1 limit 5")

def getListViewProduct() :
    return Product.objects.raw("SELECT  * FROM  db_shopee_django.product order by hot desc  limit 6")

def getListSoldProduct() :
    return Product.objects.raw("SELECT  * FROM  db_shopee_django.product order by amountsold desc  limit 3")

def getListHotBranch () :
    return  Branch.objects.raw("SELECT * FROM db_shopee_django.branch limit 3")

def findById(id) :
    return Product.objects.get(id=id)

def findDetailProductByIdProduct(idProduct) :
    return Informationproduct.objects.raw("SELECT * FROM db_shopee_django.informationproduct where idProduct = %s",[idProduct])

def countRateofProduct(idProduct) :
    cursor.execute("SELECT count(id) as count FROM db_shopee_django.rate where idProduct=%s",[idProduct])
    row = cursor.fetchone()
    return row[0]

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


def getListCommentByRate(idProduct,rate):
    sql = """
    select bangphu.id as idcomment , bangphu.comment as comment , bangphu.dateComment as datecomment,
    bangphu.rate as rate , bangphu2.username as username , bangphu2.image as image 
    from 
    (SELECT * FROM db_shopee_django.comment where idProduct = %s  and rate=%s) bangphu 
    left join 
    (select username , id ,image from user ) bangphu2 
    on bangphu.idUser = bangphu2.id
    """
    cursor.execute(sql,[idProduct,rate])
    rows = cursor.fetchall()
    return rows

def searchProduct(key):
    return Product.objects.raw('SELECT * FROM db_shopee_django.product where nameProduct LIKE %s' ,['%'+key+'%'])

def pageProduct(pagesize,pagecurrent,idcate):
    startPage = (int(pagecurrent)-1)*int(pagesize)
    return Product.objects.raw('SELECT * FROM db_shopee_django.product where idCate=%s limit  %s,%s',[idcate,startPage,pagesize])

def listHotPageProduct(pagesize,pagecurrent,idcate):
    startPage = (int(pagecurrent)-1)*int(pagesize)
    return Product.objects.raw('SELECT * FROM db_shopee_django.product where idCate=%s and hot=1 limit  %s,%s',[idcate,startPage,pagesize])

def listSoldPageProduct(pagesize,pagecurrent,idcate):
    startPage = (int(pagecurrent)-1)*int(pagesize)
    return Product.objects.raw('SELECT * FROM db_shopee_django.product where idCate=%s and amountsold>0 limit  %s,%s',[idcate,startPage,pagesize])

def listProductOrderByDesc(pagesize,pagecurrent,idcate,orderBy):
    startPage = (int(pagecurrent)-1)*int(pagesize)
    if(orderBy==1):
        return Product.objects.raw('SELECT * FROM db_shopee_django.product where idCate =  order by purchaseprice desc limit 0,10',[idcate,startPage,pagesize])
    return Product.objects.raw('SELECT * FROM db_shopee_django.product where idCate =  order by purchaseprice esc limit 0,10',[idcate,startPage,pagesize])


def countAllByIdCate(idcate):
    cursor.execute("SELECT count(id) FROM db_shopee_django.product where idCate=%s",[idcate])
    row = cursor.fetchone()
    return row[0]

def countAllHotListProduct(idcate):
    cursor.execute("SELECT count(id) FROM db_shopee_django.product where idCate=%s and hot=1",[idcate])
    row = cursor.fetchone()
    return row[0]

def countAllListSoldProduct(idcate):
    cursor.execute("SELECT count(id) FROM db_shopee_django.product where idCate=%s and amountsold>0",[idcate])
    row = cursor.fetchone()
    return row[0]  


def listpageProductApi(pagesize,pagecurrent,idcate):
    startPage = (int(pagecurrent)-1)*int(pagesize)
    cursor.execute('SELECT * FROM db_shopee_django.product where idCate=%s limit  %s,%s',[idcate,startPage,pagesize])
    rows = cursor.fetchall()
    return rows


def listHotPageProductApi(pagesize,pagecurrent,idcate):
    startPage = (int(pagecurrent)-1)*int(pagesize)
    cursor.execute('SELECT * FROM db_shopee_django.product where idCate=%s and hot=1 limit  %s,%s',[idcate,startPage,pagesize])
    rows = cursor.fetchall()
    return rows

def listHotPageProductSearchApi(pagesize,pagecurrent,key):
    startPage = (int(pagecurrent)-1)*int(pagesize)  
    cursor.execute('SELECT * FROM db_shopee_django.product where nameProduct like %s and hot=1 limit  %s,%s',['%'+key+'%',startPage,pagesize])
    rows = cursor.fetchall()
    return rows

def listSoldPageProductApi(pagesize,pagecurrent,idcate):
    startPage = (int(pagecurrent)-1)*int(pagesize)
    cursor.execute('SELECT * FROM db_shopee_django.product where idCate=%s and amountsold>0 limit  %s,%s',[idcate,startPage,pagesize])
    rows = cursor.fetchall()
    return rows

def listSoldPageProductSearchApi(pagesize,pagecurrent,key):
    startPage = (int(pagecurrent)-1)*int(pagesize)
    cursor.execute('SELECT * FROM db_shopee_django.product where nameProduct like %s and amountsold>0 limit  %s,%s',['%'+key+'%',startPage,pagesize])
    rows = cursor.fetchall()
    return rows



def listProductOrderByDescApi(pagesize,pagecurrent,idcate,orderBy):
    startPage = (int(pagecurrent)-1)*int(pagesize)
    if(int(orderBy)==1):

        cursor.execute('SELECT * FROM db_shopee_django.product where idCate =%s  order by purchaseprice desc limit %s,%s',[idcate,startPage,pagesize])
        rows = cursor.fetchall()
        return rows
    cursor.execute('SELECT * FROM db_shopee_django.product where idCate =%s  order by purchaseprice  limit %s,%s',[idcate,startPage,pagesize])
    rows = cursor.fetchall()
    return rows

def listProductOrderByDescSearchApi(pagesize,pagecurrent,key,orderBy):
    startPage = (int(pagecurrent)-1)*int(pagesize)
    if(int(orderBy)==1):

        cursor.execute('SELECT * FROM db_shopee_django.product where nameProduct like %s  order by purchaseprice desc limit %s,%s',['%'+key+'%',startPage,pagesize])
        rows = cursor.fetchall()
        return rows
    cursor.execute('SELECT * FROM db_shopee_django.product where nameProduct like %s  order by purchaseprice  limit %s,%s',['%'+key+'%',startPage,pagesize])
    rows = cursor.fetchall()
    return rows


def listCategoryApi(pagesize,pagecurrent,idcate):
    startPage = (int(pagecurrent)-1)*int(pagesize)
    cursor.execute('SELECT * FROM db_shopee_django.product where idCate=%s limit  %s,%s',[idcate,startPage,pagesize])
    rows = cursor.fetchall()
    return rows