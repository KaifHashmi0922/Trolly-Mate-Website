from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Customer
from admins.models import Products,Categorys,Companys
from .otp import*
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
# from django.template.response import TemplateResponse
# # Create your views here.
# class Const_t(Exception):
#     def __init__(self,msg):
#         self.msg=msg
        
otp_data=()

def index(request):
    prods=list(Products.objects.all())
    return render(request,"user/nindex.html/",{'prods':prods})

        
# def index(request):
#     try:
#         prods=list(Products.objects.all())
#         if not prods:
#             raise Const_t("Consatruction")
#     except:
#         return render(request,"user/nindex.html/",{'prods':prods})




def searchbar(request):
    query=request.GET.get('search')
    if query:
        cats=Categorys.objects.all()
        for d in cats:
            if str(query).lower()==str(d['name']).lower():
                query_id=d['id']
                prods=Products.objects.filter(category_id=query_id)
                return render(request,"user/index.html",{'prods':prods,'res':1})
        else:
            print("else")
            prods=Products.objects.all()
            return render(request,"user/index.html",{'prods':None,'msg':"This Item Is Not Available"})
    else:
        prods=Products.objects.all()
        print(list(prods))
        return render(request,"user/index.html",{'prods':prods,'res':0,'msg':"Pls Enter Item Name"})

def test(request,id):
    print(id)
    return redirect("/cart/")
    
def toggle_view(request):
    return render(request,"user/toggle.html")
    cat=Categorys.objects.all()
    return render(request,"user/test.html",{'cats':cat})

def shop(request,id):
    pcart=request.session.get('cart',{})
    if request.method=="POST":
        add_id=request.POST.get('plus')
       # bynow=request.POST.get(bynow)
        remove_id=request.POST.get('minus')
        # if add_id or remove_id:
        if pcart:
                qty=pcart.get(add_id)
                if qty:
                        if remove_id:
                            if qty<=1:
                                pcart.pop(add_id)
                            else:
                                qty=qty-1
                                pcart[add_id]=qty    
                        else:
                            qty=qty+1
                            pcart[add_id]=qty
                else:
                    pcart[add_id]=1    
        else:
                pcart[add_id]=1
        request.session['cart']=pcart
        print(request.session.get('cart'))
        return redirect('/')
        # else:
        #     plus_id=request.POST.get('plus')
        #     minus_id=request.POST.get('minus')
        #     print("icreemmmmm")
        #     if pcart:
        #         qty=pcart.get(plus_id)
        #         if qty:
        #                 if minus_id:
        #                     if qty<=1:
        #                         pcart.pop(plus_id)
        #                     else:
        #                         qty=qty-1
        #                         pcart[plus_id]=qty    
        #                 else:
        #                     qty=qty+1
        #                     pcart[plus_id]=qty
        #         else:
        #             pcart[plus_id]=1    
        #     else:
        #         pcart[plus_id]=1
        #     request.session['cart']=pcart
        #     print(request.session.get('cart'))
        #     return redirect('/cart/')
    cid=request.GET.get('category')
    if cid:
        prods=Products.objects.filter(category=cid)
    else:
        prods=Products.objects.all()   
    cats=Categorys.objects.all()
    data={'prods':prods,'cats':cats}
    return render(request,"user/shop.html",data)





def signup_view(request):
    # return HttpResponse("hi")
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        father=request.POST.get('father')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        phone=request.POST.get('phone')
        img=request.FILES['imag']
        if str(pass1)==str(pass2):
            cobj=Customer(fname=fname,lname=lname,father=father,email=email,pass1=pass1,Phone=phone,image=img)
            cobj.pass1=make_password(cobj.pass1)
            cobj.save()
            # return HttpResponse("Saved")
            return redirect('/')
        else:
            return HttpResponse("Password did not match")   
    return render(request,"user/signup.html")


def login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        upass=request.POST.get('password')
        if uname and upass:
            print(uname,upass)
            cust=Customer.objects.get(email=uname)   
            print(cust.email)
            print(cust.pass1)
            # return HttpResponse("Data fetched")
            if cust:
                print("if")
                if  str(upass)==str(cust.pass1):#check_password(upass,cust.pass1):
                    print("second if")
                    request.session['cust_id']=cust.id
                    print(cust.id)
                    request.session['cust_name']=cust.fname
                    request.session['cust_email']=cust.email
                    # url_image = cust.image
                    print("session set Successfully")
                    print(cust.image)
                    if cust.image:
                        request.session['cust_image']=cust.image.url
                    else:
                        request.session['cust_image']=""
                    return redirect('/')
            else:
                return redirect('/user/signup/')
        else:
            return render(request,"user/cust_login.html",{'msg':"Pls Enter Email And Pass "})
    return render(request,"user/cust_login.html")





def logout_view(request):
    request.session.clear()
    return redirect('/')

# @login_required(login_url='/userlogin/')
# def cart_view(request):
#     ids=[]
#     try:
#         ids=list(request.session.get('cart').keys())
#     except:
#         pass    
#     prods=list(Products.objects.filter(id__in=ids))
#     return render(request,"user/cart.html",{'prods':prods})

def profile_view(request):
    id=request.session.get('cust_id')    
    obj=Customer.objects.get(id=id)
    print(obj)
    return render (request,"user/profile.html",{'rec':obj})

def view_product(requset):
    r=list(requset.session.get('cart'))
    rec=Products.objects.filter(id__in=r)
    return render (requset,"user/viewproduct.html",{'value':rec,'count':r})


def guest_view(request):
    # return HttpResponse("hlo")
    return render (request,"user/guest_profile.html")


def edit_password(request,id):
    obj=Customer.objects.get(id=id)
    if request.method=="GET":
        cpass=request.GET.get('cpass')
        print(cpass)
    return HttpResponse("Edit Password")   
        # print(cpass,type(cpass))
        # print(obj.pass1,type(obj.pass1))
        # if obj.pass1==str(cpass):
        #     print("Success")
        # print("NOt Success")
    return HttpResponse("Edit Password")
    

def show(request):
    id=request.session.get('cust_name')
    em=request.session.get('cust_email')
    print(id,em)
    return HttpResponse("session Read")

def cart_view(request):
    p=request.session.get('cart').keys()
    if p:
        print(p)
        prods=Products.objects.filter(id__in=p)
        print(prods)
        return render(request,"user/cart.html",{'prods':prods})
    else:
        print("cart is empty")
        return render(request,"user/cart.html",{'msg':"CART IS EMPTY"})

def Cust_update(request,id):
    obj=Customer.objects.get(id=id)
    if request.method=="POST":
        obj.name=request.POST.get('name')
    return HttpResponse("")


def image_delete(request,id):
    cust=Customer.objects.get(id=id)
    cust.image.delete()
    cust.save()
    return redirect("/profile/")

def prod_add(request):
    pcart=request.session.get('cart',{})
    if request.method=="POST":
        plus_id=request.POST.get('plus')
        c_plus_id=request.POST.get('c_plus')
        # plus_id_m=request.POST.get('m_add')
        q=pcart.get(plus_id)
        if q:
            if q>=1:
                pcart[plus_id]+=1           
                request.session['cart']=pcart
                return redirect('/')
            else:
                pcart[plus_id]=1
                request.session['cart']=pcart   
        else:
            pcart[plus_id]=1 
            request.session['cart']=pcart    
    request.session['cart']=pcart
    return redirect('/')





def prod_minus(request):
    pcart=request.session.get('cart',{})
    if request.method=="POST":
        minus_id=request.POST.get('minus')
        q=pcart.get(minus_id)
        if q:
            if q==1:
                print(pcart.pop(minus_id))
                request.session['cart']=pcart
                return redirect('/')
            else:
                pcart[minus_id]-=1
                request.session['cart']=pcart
        else:     
            request.session['cart']=pcart
            return redirect('/')
    request.session['cart']=pcart
    return redirect('/')




def cart_add(request):
    pcart=request.session.get('cart',{})
    if request.method=="POST":
        c_plus_id=request.POST.get('c_plus')
        # plus_id_m=request.POST.get('m_add')
        q=pcart.get(c_plus_id)
        if q:
            if q>=1:
                pcart[c_plus_id]+=1           
                request.session['cart']=pcart
                return redirect('/cart/')
            else:
                pcart[c_plus_id]=1
                request.session['cart']=pcart   
        else:
            pcart[c_plus_id]=1 
            request.session['cart']=pcart    
    request.session['cart']=pcart
    return redirect('/cart/')




def cart_minus(request):
    pcart=request.session.get('cart',{})
    if request.method=="POST":
        c_minus_id=request.POST.get('c_minus')
        q=pcart.get(c_minus_id)
        if q:
            if q==1:
                print(pcart.pop(c_minus_id))
                request.session['cart']=pcart
                return redirect('/')
            else:
                pcart[c_minus_id]-=1
                pcart[c_minus_id]
                request.session['cart']=pcart
        else:     
            request.session['cart']=pcart
            return redirect('/cart/')
    request.session['cart']=pcart
    return redirect('/cart/')


def password_forget(request):
    pass

def change_password(request):
    pass
def bynow(request):
    pcart=request.session.get('cart',{})
    if request.method=="POST":
        bynow=request.POST.get('bynow')
        p=pcart.get(bynow)
        if p:
            print("Purchesd")
            return render(request,"user/shoping.html")
        else:
            print("NOT selected")
            return redirect('/')
    return redirect('/')












def varify_identity(request):
    c_id=request.session.get('cust_id')
    c_name=request.session.get('cust_name')
    c_email=request.session.get('cust_email')
    rec=Customer.objects.get(id=c_id)
    if rec:
        return render(request,"user/place_order.html",{'rec':rec})
    else:
    
        return redirect('user/login/')
    
    
    
    
    
    
# @login_required(login_url='/login/')
def place_order(request):
    c_id=request.session.get('cust_id')
    c_name=request.session.get('cust_name')
    c_email=request.session.get('cust_email')
    if c_id and c_email:
        print("valid")
        return render(request,"user/placeorder.html")
        # return HttpResponse("Customer valid")
    else:
        
        return redirect('user/login/')
           
def show_address(request):
    return render(request,"user/show_address.html")
def add_address(request):
    return render(request,"user/address_form.html")

def purchesed(request):
    pass


def save_address(request):
    v1=request.session.get('cust_id')
    v2=request.session.get('cust_email')
    if request.method == "POST":
        if v1 and v2:
            l=[]
            rec=Customer.objects.get(id=v1)
            
            name = request.POST.get('fullname')
            phone1 = request.POST.get('phone_no')
            a_phone = request.POST.get('alter_phone_no')
            pincode = request.POST.get('pincode')
            city = request.POST.get('city')
            state = request.POST.get('state')
            country = request.POST.get('country')
            area_info=request.POST.get('area_info')
            house_info=request.POST.get('house_info')
            # home = request.POST.get('home')
            # work = request.POST.get('work')
            if a_phone:
                a__phone=a_phone
            else:
                a__phone=None
            l.extend([name,phone1,a_phone,pincode,city,state,country,house_info,area_info])
            rec.address=l
            rec.save()
            # # if home:
            # #       a_type=home
            # # else:
            # #       a_type=work
            # address={'address1':{'full_name':name,'phone_number':phone1,'alter_phone_number':a__phone,'pincode':pincode,
            #                     'city':city,'state':state,'country':country,'house_info':house_info}}
        
            # print(address)
            # for i in address.keys():
            #     print(address[i])
            return HttpResponse("data Fectshed")
        else:
            return render (request,"user/cust_login.html")
    return render(request,"user/address_form.html")

        
def forget_password_phone(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        try:
            obj = Customer.objects.get(Phone=phone)
        except Customer.DoesNotExist:
            return HttpResponse("User not found.")

        # Prepare values to pass: [first name, last name, email]
        user_info = [obj.email, str(obj.Phone)]
        if user_info:
            otp,old_time=phone_otp(user_info)
            request.session['gotp']=otp
            request.session['phone']=obj.Phone
            request.session['old_time']=str(old_time)
            return redirect('/forget_pass_phone/')
        else:
            return HttpResponse("Phone reset not implemented yet.")

    return render(request, "user/forget_pass_phone.html",{'status':0})


def phone_otp_varify(request):
    temp=[]
    if request.method == "POST":
        phone=request.POST.get('phone')
        cotp=request.POST.get('otp')
        if cotp :
            gotp=request.session.get('gotp')
            old_time=request.session.get('old_time')
            temp.append(gotp)
            temp.append(cotp)
            temp.append(old_time)
            temp=tuple(temp)
            counter=0
            while(1):
              if counter<=3:
                  result=varify_otp(temp)
                  if result:
                      return redirect('/new_pass_password/')
                  else:
                      counter+=1
                      print("Pls Try after 30 miutes ")
                      return redirect('/forget_pass_ph/')         
              else:
                  return HttpResponse("No Attempt")
    return render(request, "user/forget_pass_phone.html",{'status':1})







def forget_password_email(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            obj = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return HttpResponse("User not found.")

        # Prepare values to pass: [first name, last name, email]
        user_info = [obj.fname, obj.lname, obj.email]

        if user_info:
            otp,old_time=email_otp(user_info)    
            global otp_data
            otp_data=(otp,old_time,obj.email)
            print(otp_data)
            return redirect('/email_varify/')
        else:
            return HttpResponse("Phone reset not implemented yet.")

    return render(request, "user/forget_pass_email.html",{'status':0})

    


def email_otp_varify(request):
    temp=[]
    gotp,old_time,email=otp_data
    if request.method=="POST":
        email=request.POST.get('email')
        cotp=request.POST.get('otp')
        temp.append(gotp)
        temp.append(cotp)
        temp.append(str(old_time))
        temp=tuple(temp)
        result=varify_otp(temp)
        counter=0
        while(1):
            if counter<=3:
                result=varify_otp(temp)
                if result:
                    return redirect('/new_pass_password/')
                else:
                    counter+=1
                    return redirect('/forget_pass_ph/')         
            else:
                return HttpResponse("Pls Try after 30 miutes ")
    return render(request,"user/forget_pass_email.html",{'status':1,'email':email})


