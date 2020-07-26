from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User 
from contacts.models import Contact
import logging
logger = logging.getLogger(__name__)
#logger.setLevel(logging.WARNING)
#file_handler_1 = logging.FileHandler('btre/logs/handler_request.log')
#file_handler_2 = logging.FileHandler('btre/logs/filess_2.log')

#file_handler_1.setFormatter(
     #logging.Formatter('1[%(asctime)s] : 2[%(levelname)s] : 3[%(name)s] : 4[%(module)s]: 5[%(process)d]: 6[%(thread)d]: 7[%(message)s]'))
#file_handler_2.setFormatter(
 #    logging.Formatter('%(asctime)s : ******%(levelname)s******* : %(name)s :  %(message)s'))

#logger.addHandler(file_handler_1)
#logger.addHandler(file_handler_2)
#logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')
#logging.info("Just like that!")
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
               messages.success(request, ' you are now logged in')
               logger.info(request)
               return redirect('dashboard')
          else:
               logging.info(messages.error(request, 'Invalid credentials'))
               return redirect('login')
     else:
          
          return render(request, 'accounts\login.html')

     

def logout(request):
     if request.method == 'POST':
          auth.logout(request)
          messages.success(request, 'You are now logged out')
          logger.info(request)
          return redirect('index')
     else:
          return render(request, 'accounts\logout.html')
def dashboard(request):
     contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

     context = {
          'contacts':contacts,
     }
     logger.info(request)
     
     return render(request, 'accounts\dashboard.html', context)