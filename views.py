from django.http import *
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.utils.decorators import method_decorator
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView, View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.db.models import Q
from models import *
 
from django.contrib.auth import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import unittest
from google.appengine.api import files
import logging
import urllib2
import urllib
import httplib
import xml.dom.minidom
import json
from google.appengine.api import urlfetch
from django.db.models import signals
from google.appengine.api import users as cusers
import webapp2

PERPAGE=50
users = ""
class CsrfExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CsrfExemptMixin, self).dispatch(request, *args, **kwargs)

def checkuserlogin_dispatch(f):
    def wrap(request, *args, **kwargs):
        if 'IsLogin' in request.session and request.session['IsLogin'] and request.session['Staff'].staff_email !="":
            user = cusers.get_current_user()
            logging.info('Gmail User::  %s', user.email())
            logging.info('Appengine User::  %s', request.session['Staff'].staff_email)
            if user.email() != request.session['Staff'].staff_email:
                logging.info('Error Gmail User::  %s', user.email())
                logging.info('Error Appengine User::  %s', request.session['Staff'].staff_email)
                request.session['ErrorMessage'] = "You are logged in as "+str(user.email())+" gmail account. Clean Gmail cookies and relogin."
                return HttpResponseRedirect('/login')
            customer_list = Tblstaff.objects.filter(staff_email = request.session['Staff'].staff_email, staff_active=1)
            #customer_list = customers.objects.filter(email = request.session['Customer'].email,
            #                                         pass_field = request.session['Customer'].pass_field,custenabled=1)
            if customer_list:
                request.session['IsLogin'] = True
                request.session['Staff'] = customer_list[0]
                success = True
            else:
                request.session['ErrorMessage'] = "Local Session Doesnot match with gmail session. Clean Gmail cookies and relogin."
                logging.info('Error Gmail User::  %s', user.email())
                logging.info('Error Appengine User::  %s', request.session['Staff'].staff_email)
                return HttpResponseRedirect('/login')
            logging.info('Staff List::  %s', customer_list[0])
        else:
            #logging.info('Error Gmail User::  %s', user.email())
            #logging.info('Error Appengine User::  %s', request.session['Staff'].staff_email)
            request.session['ErrorMessage'] = "Your session has been expired. Please retry."
            return HttpResponseRedirect('/login')
        return f(request, *args, **kwargs)
    return wrap

class LoginRequiredMixin(object):
    @method_decorator(checkuserlogin_dispatch)
    def dispatch(self,request, *args, **kwargs):
        #logging.info('Fetch Started::  %s', request.session['Customer'].email)
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

@csrf_exempt
def render_template(request, template, data=None):
    errs =""
    if request.method == 'GET' and 'err' in request.GET:
        data.update({'errs':request.GET['err']})
    
    response = render_to_response(template, data,
                              context_instance=RequestContext(request))
    return response


class ContactsViewClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        if 'cname' in request.GET and request.GET['cname'] != "":
            #cname = request.GET['cname']
            cname = " and (Contact_FirstName like '%%"+request.GET['cname']+"%%' or Contact_LastName like '%%"+request.GET['cname']+"%%')"
        else:
            cname = ""

        #if 'cemail' in request.GET and request.GET['cemail'] != "":
        #    cemail = " and Contact_Email like '%%"+request.GET['cemail']+"%%'"
        #else:
        #    cemail = ""
        if 'ccompany' in request.GET and request.GET['ccompany'] != "":
            ccompany = " and Contact_Company like '%%"+request.GET['ccompany']+"%%'"
        else:
            ccompany = ""
        
        if 'ctype' in request.GET and request.GET['ctype'] != "" and request.GET['ctype'] != "Contact Type":
            ctype = " and Contact_Type like '%%"+request.GET['ctype']+"%%'"
        else:
            ctype = ""

        searchquery="select * from tblcontact where Contact_PK>0 "+cname+" "+ccompany+" "+ctype+""
        allcontacts = Tblcontact.objects.raw(searchquery)
        #logging.info('total contacts:: %s',allcontacts.count())
        content = {'page_title': "View Contacts",
                   'allitems':allcontacts,}
        return render_template(request, "viewcontacts.htm", content)

class CallsViewClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        if 'cname' in request.GET and request.GET['cname'] != "":
            #cname = request.GET['cname']
            cname = " and (Contact_FirstName like '%%"+request.GET['cname']+"%%' or Contact_LastName like '%%"+request.GET['cname']+"%%')"
        else:
            cname = ""

        if 'ccompany' in request.GET and request.GET['ccompany'] != "":
            ccompany = " and Contact_Company like '%%"+request.GET['ccompany']+"%%'"
        else:
            ccompany = ""
        
        if 'ctype' in request.GET and request.GET['ctype'] != "" and request.GET['ctype'] != "Contact Type":
            ctype = " and Contact_Type like '%%"+request.GET['ctype']+"%%'"
        else:
            ctype = ""
        #allcontacts = Tblcontact.objects.raw("select * from tblcontact where Contact_PK>0 "+cname+" "+cemail+" "+ctype+"")
        allcalls = Tblcalls.objects.raw("select * from tblcalls where calls_pk>0")
        calltypes = Tblcalltype.objects.all()
        callactions = Tblcallaction.objects.all()
        callsource = Tblcallsource.objects.all()
        #logging.info('total contacts:: %s',allcontacts.count())
        content = {'page_title': "View Calls",
                   'allitems':allcalls,"calltypes":calltypes,"callactions":callactions,
                   "callsource":callsource,}
        return render_template(request, "viewcalls.htm", content)

class AddContactFormClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        content = {'page_title': "Add Contact",}
        return render_template(request, "addcontact.htm", content)

class EditContactFormClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        cid = request.GET['cid'] if 'cid' in request.GET else "error"
        if cid != "error" and cid !="":
            contactinfo=Tblcontact.objects.get(contact_pk=cid)
        else:
            contactinfo=""
            cid = "error"
        content = {'page_title': "Edit Contact","info":contactinfo,"cid":cid}
        return render_template(request, "editcontact.htm", content)

class ViewContactClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        cid = request.GET['cid'] if 'cid' in request.GET else "error"
        if cid != "error" and cid !="":
            contactinfo=Tblcontact.objects.get(contact_pk=cid)
        else:
            contactinfo=""
            cid = "error"
        content = {'page_title': "Edit Contact","info":contactinfo,"cid":cid}
        return render_template(request, "viewcontact.htm", content)

class ViewCallClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        cid = request.GET['cid'] if 'cid' in request.GET else "error"
        if cid != "error" and cid !="":
            callinfo=Tblcalls.objects.get(calls_pk=cid)
            contactinfo=Tblcontact.objects.get(contact_pk=callinfo.calls_contactid)
        else:
            callinfo=""
            cid = "error"
            contactinfo=""
        calltypes = Tblcalltype.objects.all()
        callactions = Tblcallaction.objects.all()
        callsource = Tblcallsource.objects.all()
        
        content = {'page_title': "View Call","info":callinfo,"cinfo":contactinfo,"cid":cid,
                   "calltypes":calltypes,"callactions":callactions,
                   "callsource":callsource,}
        return render_template(request, "viewcall.htm", content)

class AddCallFormClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        cid = request.GET['cid'] if 'cid' in request.GET else "error"
        calltypes = Tblcalltype.objects.all()
        callactions = Tblcallaction.objects.all()
        callsource = Tblcallsource.objects.all()
        callstaff = Tblstaff.objects.all().filter(staff_active=1)
        content = {'page_title': "Add New Call","calltypes":calltypes,"callactions":callactions,
                   "callsource":callsource,"callstaff":callstaff,"cid":cid}
        return render_template(request, "addcall.htm", content)

class AddMatterFormClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        cid = request.GET['cid'] if 'cid' in request.GET else "error"
        calltypes = Tblcalltype.objects.all()
        callactions = Tblcallaction.objects.all()
        callsource = Tblcallsource.objects.all()
        callstaff = Tblstaff.objects.all().filter(staff_active=1)
        mattertype = Tblmattertype.objects.all()
        billingtype = Tblbillingtype.objects.all()
        content = {'page_title': "Add New Matter","calltypes":calltypes,"billingtype":billingtype,
                   "callsource":callsource,"callstaff":callstaff,"cid":cid,"mattertype":mattertype}
        return render_template(request, "addmatter.htm", content)

class ViewMattersClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        cid = request.GET['cid'] if 'cid' in request.GET else "error"
        allmatters = Tblmatters.objects.all()
        mattertype = Tblmattertype.objects.all()
        billingtype = Tblbillingtype.objects.all()
        content = {'page_title': "View Matter", "allitems":allmatters, "cid":cid,
                   "billingtype":billingtype,"mattertype":mattertype}
        return render_template(request, "viewmatters.htm", content)

class SummaryClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        #user = cusers.get_current_user()
        #logging.info('Fetch Started::  %s', request.session['Staff'].staff_email)
        #logging.info('Fetch Ended::  %s', user.nickname())
        content = {'page_title': "Profile",}
        return render_template(request, "index.html", content)

class UsersViewClass(LoginRequiredMixin,TemplateView):
    def get(self, request, *args, **kwargs):
        content = {'page_title': "Users",
                   'users':User.objects.filter(is_active = True).all(),}
        return render_template(request, "users.html", content)

