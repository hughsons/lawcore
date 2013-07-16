from django.contrib.auth import *
from django.http import *
from forms import *
from django.template.loader import get_template
from django.template import Context
from django.utils.decorators import method_decorator
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView, View
from django.views.decorators.csrf import csrf_exempt
import logging, random, hashlib, datetime
from google.appengine.api import users
import webapp2
from models import *
class MyHandler(TemplateView):
    def get(self, request, *args, **kwargs):
        user = users.get_current_user()
        logging.info('Fetch Started::  %s', request.session['Staff'].staff_email)
        logging.info('Fetch Ended::  %s', user.nickname())
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                        (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))

        return HttpResponse('<html><body>%s</body></html>' % greeting)

@csrf_exempt
def LoginView(request):
    if request.method == 'POST':
        if 'target' in request.POST:
            target_page = request.POST['target']
        else:
            target_page = users.create_login_url('/')
        #logout(request)
        customer_list=""
        form = LoginForm(request.POST)
        if form.is_valid():
            logging.info('Form Is clean')
            email = form.cleaned_data['email']
            #password = form.cleaned_data['password']
            logging.info('LoginfoMessage:: %s',email)
            customer_list = Tblstaff.objects.filter(staff_email = email, staff_active=1)
            if customer_list:
                #t = Tblstaff.objects.get(staff_email = email, staff_active=1)
                #t.lastlogindate = datetime.datetime.now()
                #t.save()
                request.session['IsLogin'] = True
                request.session['Staff'] = customer_list[0]
                success = True
                logging.info('LoginfoMessage:: %s',customer_list[0])
                return HttpResponseRedirect(target_page)
            else:
                request.session['ErrorMessage'] = "Invalid Username or Password."
                return HttpResponseRedirect('/login')
            
        else:
            request.session['ErrorMessage'] = "Invalid Form data."
            return HttpResponseRedirect('/login')
    else:
        request.session['ErrorMessage'] = "Form submission is not as expected."
        return HttpResponseRedirect('/login')

@csrf_exempt
def loginpage(request):
    state = "Please log in below..."
    default_message = ""
    error_message1, error_message2 = "", ""
    #logging.info('Fetch Started::  %s', request.session["ErrorMessage"])

    if 'message' in request.GET:
      default_message = request.GET['message']

    #if 'error' in request.GET:
    #  error_message = request.GET['error']
    error_message = ""
    if "ErrorMessage" in request.session:
      error_message1 = request.session["ErrorMessage"]
      del request.session["ErrorMessage"]
      
    if "ErrorMessage2" in request.session:
      error_message2 = request.session["ErrorMessage2"]
      del request.session["ErrorMessage2"]
    t = get_template('login.htm')
    c = Context({
        'page_title': "User Area",
        'form': LoginForm(),
        'message2': default_message,
        'error_message1': error_message1,
        'error_message2': error_message2
    })
    logout(request)
    return HttpResponse(t.render(c))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')
