from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User 
from contacts.models import Contact
import logging
log = logging.getLogger(__name__)
# Create your views here.

def register(request):
     if request.method == 'POST':
          #GET forms values
          first_name     = request.POST['first_name']
          last_name      = request.POST['last_name']
          username       = request.POST['username']
          email          = request.POST['email']
          password       = request.POST['password']
          password2      = request.POST['password2']
          
          # check if passwords match.
          if password == password2:
               #check user nanme
               if User.objects.filter(username=username).exists():
                    messages.error(request,'username exists, please change')
                    return redirect('register')
          
               else:
                    if User.objects.filter(email=email).exists():
                         logging.info(messages.error(request,'email is being used'))
                         return redirect('register')
                    else:
                         user = User.objects.create_user(username=username, password=password,
                         email=email, first_name=first_name, last_name=last_name)
                         #loging after resgister
                         #auth.login(request, user)
                         #messages.success(request, 'You are logged in')
                         user.save()
                         messages.success(request, 'You are logged in')
                         return redirect('login')

          else:
               messages.error(request,'password do not match')
               return redirect('register')
     else:
          return render(request, 'accounts/register.html')
     



def login(request):
     if request.method == 'POST':
          username       = request.POST['username']
          password       = request.POST['password']

          user = auth.authenticate(username=username, password=password)

          if user is not None:
               auth.login(request ,user)
               logging.info (messages.success(request, ' you are now logged in'))
               return redirect('dashboard')
          else:
               logging.info(messages.error(request, 'Invalid credentials'))
               return redirect('login')
     else:
          return render(request, 'accounts\login.html')
     

def logout(request):
     if request.method == 'POST':
          auth.logout(request)
          logging.info(messages.success(request, 'You are now logged out'))
          return redirect('index')
     else:
          return render(request, 'accounts\logout.html')
def dashboard(request):
     contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

     context = {
          'contacts':contacts,
     }
     
     return render(request, 'accounts\dashboard.html', context)