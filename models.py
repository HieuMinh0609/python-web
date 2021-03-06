# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    recipientphone = models.CharField(db_column='recipientPhone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    addressdetail = models.CharField(db_column='addressDetail', max_length=200, blank=True, null=True)  # Field name made lowercase.
    recipientname = models.CharField(db_column='recipientName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'address'


class Cart(models.Model):
    totalprice = models.IntegerField(db_column='totalPrice', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart'


class Category(models.Model):
    name = models.CharField(max_length=255)
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Color(models.Model):
    namecolor = models.CharField(db_column='nameColor', max_length=30, blank=True, null=True)  # Field name made lowercase.
    idproduct = models.ForeignKey('Product', models.DO_NOTHING, db_column='idProduct', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'color'


class Comment(models.Model):
    comment = models.CharField(max_length=255, blank=True, null=True)
    datecomment = models.DateTimeField(db_column='dateComment', blank=True, null=True)  # Field name made lowercase.
    idproduct = models.IntegerField(db_column='idProduct', blank=True, null=True)  # Field name made lowercase.
    iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='idUser', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comment'


class Imageproduct(models.Model):
    url = models.CharField(max_length=100, blank=True, null=True)
    idproduct = models.ForeignKey('Product', models.DO_NOTHING, db_column='idProduct', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'imageproduct'


class Infomationcart(models.Model):
    idproduct = models.ForeignKey('Product', models.DO_NOTHING, db_column='idProduct', blank=True, null=True)  # Field name made lowercase.
    idcart = models.ForeignKey(Cart, models.DO_NOTHING, db_column='idCart', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'infomationcart'


class Informationproduct(models.Model):
    idproduct = models.ForeignKey('Product', models.DO_NOTHING, db_column='idProduct', blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(max_length=30, blank=True, null=True)
    warrantyperiod = models.DateTimeField(db_column='warrantyPeriod', blank=True, null=True)  # Field name made lowercase.
    pin = models.CharField(max_length=30, blank=True, null=True)
    rom = models.CharField(max_length=30, blank=True, null=True)
    ram = models.CharField(max_length=30, blank=True, null=True)
    chip = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'informationproduct'


class Orders(models.Model):
    priceshipping = models.FloatField(db_column='priceShipping', blank=True, null=True)  # Field name made lowercase.
    datemade = models.DateTimeField(blank=True, null=True)
    iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='idUser', blank=True, null=True)  # Field name made lowercase.
    idcart = models.ForeignKey(Cart, models.DO_NOTHING, db_column='idCart', blank=True, null=True)  # Field name made lowercase.
    idpayment = models.ForeignKey('Payment', models.DO_NOTHING, db_column='idPayment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Payment(models.Model):
    method = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'


class Product(models.Model):
    nameproduct = models.CharField(db_column='nameProduct', max_length=255)  # Field name made lowercase.
    purchaseprice = models.FloatField()
    saleprice = models.FloatField()
    quantity = models.IntegerField(blank=True, null=True)
    idcate = models.ForeignKey(Category, models.DO_NOTHING, db_column='idCate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'


class Rate(models.Model):
    value = models.IntegerField(blank=True, null=True)
    idproduct = models.IntegerField(db_column='idProduct', blank=True, null=True)  # Field name made lowercase.
    iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='idUser', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rate'


class Role(models.Model):
    namerole = models.CharField(db_column='nameRole', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'role'


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    fullname = models.CharField(max_length=30, blank=True, null=True)
    idaddress = models.ForeignKey(Address, models.DO_NOTHING, db_column='idAddress')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class Userrole(models.Model):
    iduser = models.ForeignKey(User, models.DO_NOTHING, db_column='idUser')  # Field name made lowercase.
    idrole = models.ForeignKey(Role, models.DO_NOTHING, db_column='idRole')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userrole'
