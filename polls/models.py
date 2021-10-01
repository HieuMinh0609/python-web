from django.db import models

class Address(models.Model):
    recipientphone = models.CharField(db_column='recipientPhone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    addressdetail = models.CharField(db_column='addressDetail', max_length=200, blank=True, null=True)  # Field name made lowercase.
    recipientname = models.CharField(db_column='recipientName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iduser = models.IntegerField(blank=True, null=True)
    choosed = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'address'


class Cart(models.Model):
    totalprice = models.IntegerField(db_column='totalPrice', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='iduser', blank=True, null=True)

    class Meta:
        db_table = 'cart'



class Category(models.Model):
    name = models.CharField(max_length=255)
    note = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=30, blank=True, null=True)
    class Meta:
        db_table = 'category'




class Color(models.Model):
    namecolor = models.CharField(db_column='nameColor', max_length=30, blank=True, null=True) 
 # Field name made lowercase.
    idproduct = models.ForeignKey('Product', models.DO_NOTHING, db_column='idProduct', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'color'


class Comment(models.Model):
    comment = models.CharField(max_length=255, blank=True, null=True)
    datecomment = models.DateTimeField(db_column='dateComment', blank=True, null=True)  # Field name made lowercase.
    idproduct = models.ForeignKey('Product', models.DO_NOTHING, db_column='idProduct', blank=True, null=True)  # Field name made lowercase.
    iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='idUser', blank=True, null=True)  # Field name made lowercase.
    rate = models.IntegerField(blank=True, null=True)

    class Meta:
 
        db_table = 'comment'


class Recomment(models.Model):
    datecomment = models.DateTimeField(db_column='dateComment', blank=True, null=True)  # Field name made lowercase.
    idcomment = models.ForeignKey(Comment, models.DO_NOTHING, db_column='idcomment', blank=True, null=True)
    iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='idUser', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'recomment'
        
class Imageproduct(models.Model):
    url = models.CharField(max_length=100, blank=True, null=True)
    idproduct = models.ForeignKey('Product', models.DO_NOTHING, db_column='idProduct', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'imageproduct'


class Infomationcart(models.Model):
    idproduct = models.ForeignKey('Product', models.DO_NOTHING, db_column='idProduct', blank=True, 
null=True)  # Field name made lowercase.
    idcart = models.ForeignKey(Cart, models.DO_NOTHING, db_column='idCart', blank=True, null=True) 
 # Field name made lowercase.
    total_sold = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    price_sold = models.IntegerField(blank=True, null=True)
    nameproduct = models.CharField(max_length=255, blank=True, null=True)
    realmoney = models.FloatField(blank=True, null=True)

    class Meta:
      
        db_table = 'infomationcart'


class Informationproduct(models.Model):
    idproduct = models.ForeignKey('Product', models.DO_NOTHING, db_column='idProduct', blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(max_length=30, blank=True, null=True)
    warrantyperiod = models.CharField(db_column='warrantyPeriod', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pin = models.CharField(max_length=30, blank=True, null=True)
    rom = models.CharField(max_length=30, blank=True, null=True)
    ram = models.CharField(max_length=30, blank=True, null=True)
    chip = models.CharField(max_length=30, blank=True, null=True)
    desciption = models.TextField(blank=True, null=True)

    class Meta:
   
        db_table = 'informationproduct'



class Orders(models.Model):
    priceshipping = models.FloatField(db_column='priceShipping', blank=True, null=True)  # Field name made lowercase.
    datemade = models.DateTimeField(blank=True, null=True)
    iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='idUser', blank=True, null=True)  # Field name made lowercase.
    idcart = models.ForeignKey(Cart, models.DO_NOTHING, db_column='idCart', blank=True, null=True)  # Field name made lowercase.
    idpayment = models.ForeignKey('Payment', models.DO_NOTHING, db_column='idPayment', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'orders'


class Payment(models.Model):
    method = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'payment'


class Branch(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'branch'

class Product(models.Model):
    nameproduct = models.CharField(db_column='nameProduct', max_length=255)  # Field name made lowercase.
    purchaseprice = models.FloatField()
    saleprice = models.FloatField()
    quantity = models.IntegerField(blank=True, null=True)
    idcate = models.ForeignKey(Category, models.DO_NOTHING, db_column='idCate', blank=True, null=True)  # Field name made lowercase.
    amountsold = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    idbranch = models.ForeignKey(Branch, models.DO_NOTHING, db_column='idBranch', blank=True, 
null=True)  # Field name made lowercase.
    hot = models.IntegerField(blank=True, null=True)
    view = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'product'


class Rate(models.Model):
    value = models.IntegerField(blank=True, null=True)
    idproduct = models.IntegerField(db_column='idProduct', blank=True, null=True)  # Field name made lowercase.
    iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='idUser', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'rate'


class Role(models.Model):
    namerole = models.CharField(db_column='nameRole', max_length=100)  # Field name made lowercase.

    class Meta:
        db_table = 'role'

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    fullname = models.CharField(max_length=30, blank=True, null=True)
    idaddress = models.ForeignKey(Address, models.DO_NOTHING, db_column='idAddress', blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(max_length=255, blank=True, null=True)
    male = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
    
        db_table = 'user'


class Userrole(models.Model):
    iduser = models.ForeignKey(User, models.DO_NOTHING, db_column='idUser')  # Field name made lowercase.
    idrole = models.ForeignKey(Role, models.DO_NOTHING, db_column='idRole')  # Field name made lowercase.
    class Meta:
        db_table = 'userrole'