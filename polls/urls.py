from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('checkout', views.checkout, name='checkout'),  
    path('cart', views.cart, name='cart'), 
    path('products', views.products, name='products'), 
    path('search', views.search, name='search'), 
    path('products/<int:id>', views.detailProduct, name='detailProduct'), 
    path('category/<int:id>', views.detailCate, name='detailCate'), 
    path('branch/<int:id>', views.detailBranch, name='detailBranch'), 
    path('getListCommentByRateApi', views.getListCommentByRateApi, name='getListCommentByRateApi'),
    path('addToCartAPI', views.addToCartAPI, name='addToCartAPI'),  
    path('getAmountItemApi', views.getAmountItemApi, name='getAmountItemApi'),
    path('deleteItemInCartApi', views.deleteItemInCartApi, name='deleteItemInCartApi'),
    path('updateCartApi', views.updateCartApi, name='updateCartApi'), 
    path('checkoutApi', views.checkoutApi, name='checkoutApi'),
    path('login/', views.login, name='login'),
    path('purchase', views.purchase, name='purchase'),
    path('address', views.address, name='purchase'),
    path('infomationUser', views.infomationUser, name='infomationUser'),
    path('logout', views.logout, name='logout'),
    path('uploadFileApi', views.uploadFileApi, name='uploadFileApi'),
    path('registerApi', views.registerApi, name='registerApi'),
    path('loginApi', views.loginApi, name='loginApi'),
    path('forgetPassApi', views.forgetPassApi, name='forgetPassApi'),
    path('pageProductApi', views.pageProductApi, name='pageProductApi'),
    path('soldproductsApi', views.soldproductsApi, name='soldproductsApi'),
    path('hotproductsApi', views.hotproductsApi, name='hotproductsApi'),
    path('productsOrderByApi', views.productsOrderByApi, name='productsOrderByApi'),
    
    path('soldproductsSearchApi', views.soldproductsSearchApi, name='soldproductsSearchApi'),
    path('hotproductsSearchApi', views.hotproductsSearchApi, name='hotproductsSearchApi'),
    path('productsOrderBySearchApi', views.productsOrderBySearchApi, name='productsOrderBySearchApi'),


    path('categoryApi', views.categoryApi, name='categoryApi'),
    path('changeAdressApi', views.changeAdressApi, name='changeAdressApi') ,
    path('addAddressApi', views.addAddressApi, name='addAddressApi') ,
    path('updateProfileApi', views.updateProfileApi, name='updateProfileApi') ,
    path('getAdressApi', views.getAdressApi, name='getAdressApi'),
    path('updateAddressApi', views.updateAddressApi, name='updateAddressApi'),
    path('getAllBillApi', views.getAllBillApi, name='getAllBillApi'),
    path('getDetailOrderApi', views.getDetailOrderApi, name='getDetailOrderApi'),
    path('updateOrderApi', views.updateOrderApi, name='updateOrderApi'),
    path('voteApi', views.voteApi, name='voteApi'),

    
    path('getRecommentByIdcommentApi', views.getRecommentByIdcommentApi, name='getRecommentByIdcommentApi'),

] 

