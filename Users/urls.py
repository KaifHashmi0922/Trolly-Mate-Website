
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from  .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('searchbar/',views.searchbar,name='searchbar'),
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('cart/',views.cart_view,name='cart'),
    path('profile/',views.profile_view,name='profile'),
    path('place_order/',views.place_order,name='place_order'),
    # path('viewproduct/',views.view_product,name='viewproduct'),
    # path('password_change/<id>',views.edit_password,name='password_change'),
    path('bynow/',views.bynow,name='bynow'),
    path('guest/',views.login,name='guest'),
    path('p_add/',views.prod_add,name='p_add'),
    path('p_minus/',views.prod_minus,name='p_minus'),
    path('cart_add/',views.cart_add,name='cart_add'),
    path('cart_minus/',views.cart_minus,name='cart_minus'),
    # path('shop/<id>',views.shop,name='shop'),
    path('toggle/',views.toggle_view,name='toggle'),
    path('check/',views.show,name='check')  ,
    path('update_cust/<id>',views.Cust_update,name='update_cust'),
    path('delete_img/<id>',views.image_delete,name='delete_img'),
    # path('test/<id>',views.test,name='test'),
    path('add_address/',views.add_address,name='add_address')  ,
    path('show_address/',views.show_address,name='show_address'), 
    path('save_address/',views.save_address,name='save_address') ,
    path('forget_pass_email/',views.forget_password_email,name='forget_pass_email'),
    path('forget_pass_phone/',views.forget_password_phone,name='forget_pass_phone'),
    path('email_varify/',views.email_otp_varify,name='email_varify'),
    path('phone_varify/',views.phone_otp_varify,name='phone_varify'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

