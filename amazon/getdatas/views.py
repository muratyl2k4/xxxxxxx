from django.shortcuts import render
from django.contrib.auth.decorators import login_required  
from imap_tools import MailBox , AND , OR
from django.contrib.auth.models import User
from .models import *
import re
import locale

from datetime import datetime

@login_required(login_url="login")
def home(request):
    ###EMAIL PARSE
    username ="mybusinnes.21@gmail.com"
    app_password = "vjtmyjezyhhxpsry"
    mb = MailBox('imap.gmail.com').login(username, app_password)
    user_email = request.user.email
    messages = mb.fetch(criteria=OR(from_=user_email))
    liste = []
    
    for msg in messages:
        print("----------------------------------------------------------")
        ##FROM 
        print(msg.from_)
        #ORDER İD 
        order_id_text=re.findall("Order ID:.*$",msg.text,re.MULTILINE)
        for x in order_id_text:
            print(x)
            order_id = re.findall('(?<=: )(.*)', x)
            for oi in order_id:
                print(oi)
        #ORDER DATE
        order_date_text=re.findall("Order date: .*$",msg.text,re.MULTILINE)
        locale.setlocale(locale.LC_ALL, 'en_US')

        for x in order_date_text:
            order_date = re.findall('(?<=: )(.*)', x)
            for od in order_date:
                #string to datetime object
                datetime_object = datetime.strptime(od[0:len(od)-1], "%d-%b-%Y")
                print(datetime_object)
        #PRICE
        price_text=re.findall("Price: CDN .*$",msg.text,re.MULTILINE)
        for x in price_text:
            price = re.findall('(?<=: )(.*)', x)
            for prc in price:
                print("Price:" , prc)
        #SHIPPING
        shipping_text=re.findall("Shipping: CDN .*$",msg.text,re.MULTILINE)
        for x in shipping_text:
            shipping = re.findall('(?<=: )(.*)', x)
            for shp in shipping:
                print("shipping:" , shp)
        #AMAZON FEES
        fee_text=re.findall("Amazon fees: .*$",msg.text,re.MULTILINE)
        for x in fee_text:
            fee = re.findall('(?<=: )(.*)', x)
            for afee in fee:
                print("fee:" , afee)
        #YOUR EARNING
        earning_text=re.findall("Your earnings: CDN .*$",msg.text,re.MULTILINE)
        for x in earning_text:
            earning = re.findall('(?<=: )(.*)', x)
            for ern in earning:
                print("earning:" , ern)
                print("----------------------------------------------------------")

        

            b = Data.objects.filter(SATICI_SIPARIS_NUMARASI = oi[0:len(oi)-1])
            print(b)
        if len(b) == 0:
            b = Data(
                KULLANICI = request.user , 
                SATICI_SIPARIS_NUMARASI = oi[0:len(oi)-1],
                SATIS_FIYATI  = float(prc.replace("CDN $" , "")[0:len(prc)-1]),
                AMAZON_FEE  = float(afee.replace("(","").replace(")","").replace("CDN $","")[0:len(afee)-1]),


            )
            b.save()
    return render(request , "index.html")
