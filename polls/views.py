import re
from django.urls.conf import path
from polls.service.CartService import makeCart
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.utils.translation import ngettext, templatize
from polls.models import Category,Product,Branch,Address
from .forms import AddForm
from django.http import HttpResponseRedirect
from django.db import connections
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core import serializers
import pandas as pd
from django.db.models import Case, When
import math 
from polls.service.ProductService import *
from polls.service.CategoryService import *
from polls.service.ColorService import *
from polls.service.ImageProductService import*
from polls.service.CommentService import *
from polls.service.CartService import *
from polls.service.UserService import *
from polls.service.PaymentService import *
from polls.dto.listDTO import *
from polls.service.OrderService import *
from polls.service.RateService import *

from polls.service.BranchService import *
from polls.processor.recommend.recommendService import *
from polls.processor.recommend.recommendProcessor import * 
# import thuw vieen de viet api
from django.http import HttpResponse
import json
from json import JSONEncoder
import bcrypt
from django.conf import settings
from django.core.mail import send_mail
# To get similar movies based on user rating
import numpy as np
# Controller

def index(request):

    # sản phẩm xem nhiều nhất 
    # sản phẩm hót
    # sản phẩm bán chạy 
    # thương hiệu nổi tiếng
    # sản phẩm đề xuất
    # Danh mục 
    # matrix_recommend = makeRatingMatrix()


    # matrix_recommend = np.array([[7, 6, 7, 4, 5, 4], 
    #                        [6, 7, nan, 4, 3, 4],
    #                        [nan, 3, 3, 1, 1, nan],
    #                        [1, 2, 2, 3, 3, 4],
    #                        [1, nan, 1, 2, 3, 3]])
    # print(predict_top_k_items_of_user(2,2,matrix_recommend))

    
    categories = getAllCategory()
    list_view_products = getListViewProduct()
    list_hot_branch = getListHotBranch()
    list_sold_products = getListSoldProduct()
    list_hot_products  = getListHotProduct()
    print("list_hot_products",getListHotProduct())
    return render(request,"home/index.html",{"categories":categories,'list_view_products': list_view_products,
    'list_hot_branch' :list_hot_branch,'list_sold_products' : list_sold_products,'list_hot_products':list_hot_products})


def checkout(request):
    userinfo  = request.session.get('userinfo')
    iduser = userinfo[2]
    list_address_user = getAllAddressByIduser(iduser)
    address_default = getAddressDefaultByIduser(iduser)
    list_payment = getAllPayment()
    return render(request,"home/checkout.html",{"list_address_user":list_address_user,'address_default':address_default
    ,"list_payment":list_payment})


def address (request) :
    userinfo  = request.session.get('userinfo')
    iduser = userinfo[2]
    list_address_user = getAllAddressByIduser(iduser)
    return render(request,"home/addresUser.html",{'list_address_user':list_address_user})

def login (request) :
    return render(request,"home/login.html")

def infomationUser(request):
    userinfo  = request.session.get('userinfo')
    iduser = userinfo[2]
    print("iduse",iduser)
    user = findUserById(iduser)
    print(user)

    return render(request,"home/infomationUser.html",{"users":user})

def purchase(request):
    return render(request,"home/listOrder.html")


def cart(request):
    return render(request,"home/cart.html")

def products(request):
    return render(request,"home/products.html")

def logout(request):
    del request.session['userinfo']
    return render(request,"home/login.html")


def detailProduct(request,id) :
    product = findById(id)
    list_comment = getInfoCommentAndRatingByIdProduct(id)
    list_color = getAllColorByIdProduct(id)
    list_image = getAllImageByIdProduct(id)
    list_sold_products = getListSoldProduct()
    InfomationProduct = findDetailProductByIdProduct(id)
    totalRate = countRateofProduct(id)
    totalProductNow = product.quantity- product.amountsold
    return render(request,"home/detail-product.html",{"product":product,'list_comment': list_comment,
    'list_color' :list_color,'list_sold_products' : list_sold_products,
    'list_image':list_image,'infomationProduct':InfomationProduct,'totalRate':totalRate,'totalProductNow':totalProductNow})


def detailBranch (request,id) :
    categories = getAllBranch()
    first_products = getAllProductByBranch(id)
    return render(request,"home/branch.html",{"categories":categories,"idcate":id,'first_products':first_products})

def search(request) :
    if request.method == 'POST':
        key=request.POST['key']
        
        first_products = searchProduct(key)
        return render(request,"home/searchProduct.html",{'first_products':first_products,'key':key})


def detailCate(request,id) :
    categories = getAllCategory()
    first_products = pageProduct(10,1,id)
    totalPage = math.ceil(countAllByIdCate(id)/2)
    return render(request,"home/products.html",{"categories":categories,"idcate":id,"totalPage":totalPage,'first_products':first_products})


# API
def getListCommentByRateApi(request):
    if request.method == 'GET':
        idproduct=request.GET['idproduct']
        rate = request.GET['rate']
        print("idproduct",idproduct)
        print("rate",rate)
        datas = getListCommentByRate(idproduct,rate)
        list_datas = json.dumps(datas,indent=4, sort_keys=True, default=str) # truy vấn băng cusor
        return  HttpResponse(list_datas, content_type="application/json") 

#addToCartAPI

def addToCartAPI(request):
    if request.method == 'GET':
        idproduct=request.GET['idproduct']
        number_sold = request.GET['number_sold']
        iduser = request.GET['iduser']
        if(checkExistCart(iduser,idproduct,number_sold)):
            return  HttpResponse("200", content_type="application/json") 
        return  HttpResponse("500", content_type="application/json") 
        #json.ejnor() 
        #customer from product

def getAmountItemApi(request):
    if request.method == 'GET':
        iduser = request.GET['iduser']
        item_in_cart = getItemInCart(iduser)
        categories =getAllNameCategory()
        objectData= {
            'item_in_cart' :item_in_cart,
            'categories':categories
        }
        return  HttpResponse(json.dumps(objectData), content_type="application/json") 

def deleteItemInCartApi(request):  # thay giá trị user
    if request.method == 'GET':
        iditem = request.GET['iditem']
        deleteItemInCart(iditem)
        userinfo  = request.session.get('userinfo')
        iduser = userinfo[2]
        item_in_cart = getItemInCart(iduser)

        return  HttpResponse(json.dumps(item_in_cart), content_type="application/json") 

def updateCartApi(request) :
    if request.method == 'GET':
        iditem = request.GET['iditem']
        total_sold =request.GET['total_sold']
        #iditem='+id+'&idcart='+idcart+'&total_sold='+number_product
        updateCart(iditem,total_sold)
        userinfo  = request.session.get('userinfo')
        iduser = userinfo[2]
        item_in_cart = getItemInCart(iduser)

        return  HttpResponse(json.dumps(item_in_cart), content_type="application/json") 

def checkoutApi(request):
    if request.method == 'GET':
        idpayment = request.GET['idpayment']
        userinfo  = request.session.get('userinfo')
        iduser = userinfo[2]
        boolcheckout = checkoutMethod(iduser,idpayment)
        return  HttpResponse(boolcheckout, content_type="application/json") 

def uploadFileApi(request):
    if request.method == "GET":
        return render(request,"home/login.html")
    else:
        file_obj = request.FILES.get('file') 
        # print("The name of the uploaded file is:", file_obj.name)
        # print("The size of the uploaded file is:", file_obj.size)
        f = open('polls/static/img/' + file_obj.name + "", 'wb')    
        for line in file_obj.chunks():                    
            f.write(line)                                  
        f.close()
        return HttpResponse(file_obj.name)

def registerApi(request):
    if request.method == "GET":
        return render(request,"home/login.html")
    else:
        
        username = request.POST['username']

        fullname = request.POST['fullname']
        password = request.POST['password']
        email = request.POST['email']
        image = request.POST['image']
        hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        if(image == None):
            image='userqk.jpg'
    

        user = User(username=username,password=hashed,email=email,fullname=fullname,image=image)
        register(user)
        return  HttpResponse("200", content_type="application/json") 


def loginApi(request) :
    if request.method == "GET":
        return render(request,"home/login.html")
    else:
        password = request.POST['password']
        email = request.POST['email']
       # hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt(14))
        user_login = User.objects.filter(email=email)
   
        if(user_login) :
            password_db = user_login[0].password[2:len(user_login[0].password)-1]
            if bcrypt.checkpw(password.encode('utf-8') ,password_db.encode('utf-8')):
                userinfo = []
                userinfo.append(user_login[0].username)
                userinfo.append(user_login[0].image)
                userinfo.append(user_login[0].id)
                userinfo.append(getAllRoleOfUser(user_login[0].id))

                print(userinfo)
                request.session['userinfo'] = userinfo
                return  HttpResponse(json.dumps(userinfo), content_type="application/json") 
            else :  return  HttpResponse("500", content_type="application/json") 
        return  HttpResponse("500", content_type="application/json") 

def forgetPassApi(request):
    email = request.POST['email']
    user_login = User.objects.filter(email=email)

    if user_login :
        user_=  user_login[0]
        hashed =bcrypt.hashpw('12345'.encode('utf8'), bcrypt.gensalt())
        user_.password = hashed
        user_.save()
        # print(hashed)
        # updatePass(user_.id,hashed)
        subject = 'Lấy lại mật khẩu'
        message = f'Xin chào , {user_.fullname}, mật khẩu mới của bạn là : 12345 . Vui lòng đăng nhập vào website đổi lại thông tin mật khẩu của bạn .'
        email_from = settings.EMAIL_HOST_USER
       
        recipient_list = [email, ]
        try:
            send_mail( subject, message, email_from, recipient_list )
            return  HttpResponse("200", content_type="application/json") 
        except:
         
            return  HttpResponse("500", content_type="application/json") 
    return  HttpResponse("500", content_type="application/json") 

def pageProductApi(request):
    if request.method == "GET":
        pagecurent = 1
        idcate = request.GET['idcate']
        print("idcate",idcate)
        first_products = listpageProductApi(100,pagecurent,idcate)
        return  HttpResponse(json.dumps(first_products), content_type="application/json") 
    


#Api phần category product 

def soldproductsApi(request):
    if request.method == "GET":
        pagecurent = 1
        idcate = request.GET['idcate']

        first_products = listSoldPageProductApi(100,pagecurent,idcate)
        totalItem = countAllListSoldProduct(idcate)
        responseData = {
            'totalItem': totalItem,
            'first_products': first_products
        }
        return  HttpResponse(json.dumps(responseData), content_type="application/json") 
        

def soldproductsSearchApi(request):
    if request.method == "GET":
        pagecurent = 1
        key = request.GET['key']
        first_products = listSoldPageProductSearchApi(100,pagecurent,key)
        responseData = {
            'totalItem': 1,
            'first_products': first_products
        }
        return  HttpResponse(json.dumps(responseData), content_type="application/json") 

def hotproductsSearchApi(request):
    # hotproductsApi?pagecurent='+pagecurent+'&idcate='+idcate,
    if request.method == "GET":
        pagecurent = 1
        key = request.GET['key']

        first_products = listHotPageProductSearchApi(100,pagecurent,key)
        totalItem = 1
        responseData = {
            'totalItem': totalItem,
            'first_products':first_products
        }
        return  HttpResponse(json.dumps(responseData), content_type="application/json") 

def productsOrderBySearchApi(request):
    if request.method == "GET":
        pagecurent = 1
        key = request.GET['key']
        orderby = request.GET['orderBy']
        print("orderBy",orderby)
        first_products = listProductOrderByDescSearchApi(100,pagecurent,key,orderby)
        totalItem =1
        responseData = {
            'totalItem': totalItem,
            'first_products': first_products
        }
        return  HttpResponse(json.dumps(responseData), content_type="application/json")

def hotproductsApi(request):
    # hotproductsApi?pagecurent='+pagecurent+'&idcate='+idcate,
    if request.method == "GET":
        pagecurent = 1
        idcate = request.GET['idcate']

        first_products = listHotPageProductApi(100,pagecurent,idcate)
        totalItem = countAllHotListProduct(idcate)
        responseData = {
            'totalItem': totalItem,
            'first_products':first_products
        }
        return  HttpResponse(json.dumps(responseData), content_type="application/json") 

def productsOrderByApi(request):
    if request.method == "GET":
        pagecurent = 1
        idcate = request.GET['idcate']
        orderby = request.GET['orderBy']
        print("orderBy",orderby)
        first_products = listProductOrderByDescApi(100,pagecurent,idcate,orderby)
        totalItem = countAllByIdCate(idcate)
        responseData = {
            'totalItem': totalItem,
            'first_products': first_products
        }
        return  HttpResponse(json.dumps(responseData), content_type="application/json")

def categoryApi(request):
    if request.method == "GET":
        pagecurent = request.GET['pagecurent']
        idcate = request.GET['idcate']
      
        first_products = listCategoryApi(2,pagecurent,idcate)
        totalItem = countAllByIdCate(idcate)
        responseData = {
            'totalItem': totalItem,
            'first_products': first_products
        }
        return  HttpResponse(json.dumps(responseData), content_type="application/json")

def changeAdressApi(request):
    if request.method == "GET":
        idAddress = request.GET['idAddress']
        addressDefault  = request.GET['addressDefault']
        changeAddressDefault(idAddress,addressDefault)
        return  HttpResponse('200', content_type="application/json")

def addAddressApi(request) :
    if request.method == "GET":
        return render(request,"home/checkout.html")
    else:
        username = request.POST['username']
        phone= request.POST['phone']
        newAddress  = request.POST['newAddress']
        userinfo  = request.session.get('userinfo')
        iduser = userinfo[2]
        addAddress(username,phone,newAddress,iduser)
        return  HttpResponse("200", content_type="application/json")

def updateProfileApi (request) :
    if request.method == "GET":
        return render(request,"home/infomationUser.html")
    else:
        username = request.POST['username']
        fullname= request.POST['fullname']
        email  = request.POST['email']
        male = request.POST['male']
        image = request.POST['image']
      
        userinfo  = request.session.get('userinfo')
        iduser = userinfo[2]
        updateProfile(username,fullname,email,male,image,iduser)
        return  HttpResponse("200", content_type="application/json")

def getAdressApi(request):
    if request.method == "GET":
        idAddress = request.GET['idAddress']
        address = Address.objects.get(id=idAddress)
        addressDto = AddressDTO(address.recipientname, address.addressdetail, address.recipientphone,address.id)
        print(addressDto.recipientName)
        return  HttpResponse(json.dumps(addressDto,cls=AddressDTOEncoder), content_type="application/json") 

def updateAddressApi(request):
    if request.method == "POST":
        username = request.POST['username']
        phone= request.POST['phone']
        newAddress  = request.POST['newAddress']
        id_edit = request.POST['id_edit']
        updateAdress(username,phone,newAddress,id_edit)
        return  HttpResponse("200", content_type="application/json") 

def getAllBillApi(request):
    # ENUM : status : 0 - Chờ thanh toán 
    # status : 1 - Đã thanh toán
    # statú : 2 - Đơn hủy
    if request.method == "GET":
        userinfo  = request.session.get('userinfo')
        iduser = userinfo[2]
        listOrderByIdUser = getAllOrderByIdUser(iduser)
        listOrderPaid = getAllOrderByIdUserAndStatus(iduser,1)
        listOrderWaitPayment =  getAllOrderByIdUserAndStatus(iduser,0)
        listOrderCancel = getAllOrderByIdUserAndStatus(iduser,2)
        responseData = {
            'listOrderByIdUser': listOrderByIdUser,
            'listOrderPaid': listOrderPaid,
            'listOrderWaitPayment' : listOrderWaitPayment,
            'listOrderCancel' :listOrderCancel
        }
        return  HttpResponse(json.dumps(responseData,indent=4, sort_keys=True, default=str), content_type="application/json")

def getDetailOrderApi(request):
    if request.method == "GET":
        idcart =request.GET['idcart']
        cart = getAllItemInCart(idcart)      
        return  HttpResponse(json.dumps(cart,indent=4, sort_keys=True, default=str), content_type="application/json")

def updateOrderApi(request):
    if request.method == "GET":
        idorder =request.GET['idorder']
        updateOrder(idorder)
        return  HttpResponse('200', content_type="application/json")

def voteApi(request):
    if request.method == "POST":
        idproduct = request.POST['idproduct']
        comment = request.POST['comment']
        vote = request.POST['vote']
        userinfo  = request.session.get('userinfo')
        iduser = userinfo[2]
        saveComment(idproduct,comment,iduser,vote)
        # saveRate(idproduct,vote,1)
        return  HttpResponse("200", content_type="application/json") 


def getRecommentByIdcommentApi(request):
    if request.method == "GET":
        idcomment =request.GET['idcomment']
        listRecomment = getListRecommentByIdComment(idcomment)  
        # list_data = listDataComment(28)
        return  HttpResponse(json.dumps(listRecomment,indent=4, sort_keys=True, default=str), content_type="application/json")