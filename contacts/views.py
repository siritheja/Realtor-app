from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact
# Create your views here.

def contacts(request):
    if request.method =="POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #check if user has made inquiry already
        if request.user.is_authenticated:
            has_contacted = Contact.objects.filter(user_id=user_id , listing_id = listing_id)
            if has_contacted:
                messages.error(request,'You have already made an inquiry for the property')
            else:
                contact = Contact(listing=listing, listing_id=listing_id,name=name,email=email,phone=phone,message=message, user_id=user_id)
                contact.save()
                messages.success(request,'Your request has been submitted, realtor will get back to you soon')
    return redirect('/listings/'+listing_id)
