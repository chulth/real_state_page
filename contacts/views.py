from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact 
# Create your views here.

def contact(request):
    if request.method == 'POST':
        listing_id     = request.POST['listing_id']
        listing        = request.POST['listing']
        name           = request.POST['name']
        email          = request.POST['email']
        phone          = request.POST['phone']
        message        = request.POST['message']
        user_id        = request.POST['user_id']
        realtor_email  = request.POST['realtor_email']

        #check if user has meda inquiry alredy
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have alredy made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing,listing_id= listing_id, 
        name=name, email=email, phone=phone, message=message, user_id=user_id )
        contact.save()

        #send_mail
        send_mail(
            'Propertu listing inquiry',
            'There has been an inquiery for ' + listing + '. Sing into the admin panel for more information',
            'chulth@gmail.com',
            [realtor_email, 'techguy@info.com'],
            fail_silenty=False
        )

        messages.success(request, 'You request gas beeb submited, a realtor will get back to you soon')
    
        return redirect('/listings/'+listings_id) 