from polls.models import Address,User,Userrole
from django.db import connections
cursor = connections['default'].cursor()

def getAllAddressByIduser (iduser) : 
    return  Address.objects.raw("SELECT * FROM db_shopee_django.address where iduser=%s",[iduser])

def getAddressDefaultByIduser (iduser) : 
    return  Address.objects.raw("SELECT * FROM db_shopee_django.address where iduser=%s and choosed =%s",[iduser,1])

def register(newuser) :
    newuser.save()
    newUserInsert = User.objects.all().last()
    cursor.execute('''INSERT INTO userrole (idUser,idRole)  VALUES (%s,%s)''',[newUserInsert.id,1])

def updatePass(iduser,newPass) :
    cursor.execute('''update user set password=%s   where id= %s ''',[newPass,iduser])

def changeAddressDefault(idAddress,addressDefault):
    cursor.execute('''update address set choosed=%s   where id= %s ''',[0,addressDefault])
    cursor.execute('''update address set choosed=%s   where id= %s ''',[1,idAddress])

def countAddressOfUser(iduser) :
    cursor.execute("SELECT count(id) FROM db_shopee_django.address where iduser=%s",[iduser])
    row = cursor.fetchone()
    return row[0]

def addAddress(username,phone,newAddess,iduser):
    countAddress = countAddressOfUser(iduser)
    if int(countAddress)>0 :
        cursor.execute('''INSERT INTO address (recipientPhone,addressDetail,recipientName,idUser,choosed)  VALUES (%s,%s,%s,%s,%s)'''
        ,[phone,newAddess,username,iduser,0])
    else :
        cursor.execute('''INSERT INTO address (recipientPhone,addressDetail,recipientName,idUser,choosed)  VALUES (%s,%s,%s,%s,%s)'''
        ,[phone,newAddess,username,iduser,1])

def updateAdress(username,phone,newAddess,idAddess):
    cursor.execute('''update address set recipientPhone=%s,addressDetail=%s,recipientName=%s   where id= %s ''',
    [phone,newAddess,username,idAddess])

def findUserById(idUser):
    return User.objects.get(id=idUser)

def updateProfile(username,fullname,email,male,image,iduser):
    cursor.execute('''update user set username=%s,fullname=%s,email=%s,male=%s,image=%s   where id= %s ''',
    [username,fullname,email,male,image,iduser])

def getAllRoleOfUser(iduser):
    roles =[]
    cursor.execute('''SELECT * FROM db_shopee_django.userrole where idUser=%s''', [iduser])
    rows = cursor.fetchall()
    for item in rows:
        roles.append(item[2])
    return roles