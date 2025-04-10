from django.core.mail import send_mail
from django.conf import settings
import requests
import datetime as dt
import random as rm
# Create your views here.

#--------------------------------------------------------------------------------------------------------------
time=dt.datetime


def email_otp(*a):   
    fname, lname, email = a[0]
    otp,old_time=genrate_otp()
    subject = 'Hello Brother'
    message = f"""Hi [ {fname} {lname} ],

requested a password reset. Use the code below to proceed:

🔐 OTP: {otp}

This code is valid for 10 minutes. If you didn’t request this, just ignore this email.

Thanks,  The [ TrollyMate ] Team
                """
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,from_email,recipient_list)
    return otp,old_time

    
def check_time(time):
        time = dt.datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
        new_time=time+dt.timedelta(minutes=5)
        return new_time
    
    

def genrate_otp():
    otp=rm.randint(100000,999999)
    old_time=time.now()
    return otp,old_time

def varify_otp(*a):
        gotp,cotp,old_time=a[0]
        new_time=check_time(old_time)
        if time.now()<=new_time:
           if str(gotp)==str(cotp):
              return True
           else:
              return False
        else:
           print(" Otp Expired")
           return False
        




# ---------------------------------------------------------------------------
def phone_otp(*a):
    api_root="https://2factor.in/API/V1/"
    api_key="a0780a7e-aa8b-11ef-8b17-0200cd936042/"
    type_otp="SMS/"
    cuntry_code="+91"
    email, phone = a[0]
    number=phone+"/"
    otp,old_time=genrate_otp()
    otp=str(otp)
    url=api_root+api_key+type_otp+cuntry_code+number+otp
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    return otp,old_time

#

def otp_genrate():
    pass