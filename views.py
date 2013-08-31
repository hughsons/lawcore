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
from google.appengine.api import search
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
            cname = str(request.GET['cname'])
            #cname = " and (Contact_FirstName like '%%"+request.GET['cname']+"%%' or Contact_LastName like '%%"+request.GET['cname']+"%%')"
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
        if 'noof' in request.GET and request.GET['noof'] != "":
            noof = request.GET['noof']
        else:
            noof = 25
        #searchquery="select * from tblcontact where Contact_PK>0 "+cname+" "+ccompany+" "+ctype+""
        searchquery='''SELECT Contact_PK, Contact_FirstName, Contact_MiddleName, Contact_LastName, Contact_Telephone, Contact_Company,
                       Contact_Address1, Contact_Address2, Contact_City, Contact_State, Contact_ZIP, Contact_Fax, Contact_Telephone2,
                       Contact_Email, Contact_AlternateContact, Contact_Type FROM tblcontact WHERE (Contact_LastName LIKE '%%'''+cname+'''%%')
                        OR (Contact_FirstName LIKE '%%'''+cname+'''%%') OR (Contact_Telephone LIKE '%%'''+cname+'''%%')
                        OR (Contact_Telephone2 LIKE '%%'''+cname+'''%%') OR (Contact_Email LIKE '%%'''+cname+'''%%')
                        OR (Contact_AlternateContact LIKE '%%'''+cname+'''%%') OR (Contact_Company LIKE '%%'''+cname+'''%%')
                        ORDER BY Contact_LastName, Contact_FirstName limit '''+str(noof)+''''''
        logging.info('total contacts:: %s',searchquery)
        allcontacts = Tblcontact.objects.raw(searchquery)
        
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
        if 'noof' in request.GET and request.GET['noof'] != "":
            noof = request.GET['noof']
        else:
            noof = 25
        allcalls = Tblcalls.objects.raw("select * from tblcalls where Calls_StaffID = "+str(request.session['Staff'].staff_pk)+" and (Calls_Deleted!=1)  limit "+str(noof)+"")
        calltypes = Tblcalltype.objects.all()
        callactions = Tblcallaction.objects.all()
        callsource = Tblcallsource.objects.all()
        logging.info('total contacts:: %s',request.session['Staff'].staff_pk)
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

class EditCallFormClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        caid = request.GET['caid'] if 'caid' in request.GET else "error"
        if caid != "error" and caid !="":
            callinfo=Tblcalls.objects.get(calls_pk=caid)
            contactinfo=Tblcontact.objects.get(contact_pk=callinfo.calls_contactid)
        else:
            callinfo=""
            cid = "error"
            contactinfo=""
        calltypes = Tblcalltype.objects.all()
        callactions = Tblcallaction.objects.all()
        callsource = Tblcallsource.objects.all()
        callstaff = Tblstaff.objects.all().filter(staff_active=1)
        content = {'page_title': "Add New Call","calltypes":calltypes,"callactions":callactions,
                   "callsource":callsource,"callstaff":callstaff,"caid":caid,"callinfo":callinfo}
        return render_template(request, "editcall.htm", content)

class AddMatterFormClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        cid = request.GET['cid'] if 'cid' in request.GET else "error"
        calltypes = Tblcalltype.objects.all()
        callactions = Tblcallaction.objects.all()
        callsource = Tblcallsource.objects.all()
        callstaff = Tblstaff.objects.all().filter(staff_active=1)
        mattertype = Tblmattertype.objects.all()
        billingtype = Tblbillingtype.objects.all()
        viewmatters = Tblmatters.objects.all().filter(matters_clientid1=cid)
        content = {'page_title': "Add New Matter","calltypes":calltypes,"billingtype":billingtype,"viewmatters":viewmatters,
                   "callsource":callsource,"callstaff":callstaff,"cid":cid,"mattertype":mattertype}
        return render_template(request, "addmatter.htm", content)

class EditMatterFormClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        mid = request.GET['mid'] if 'mid' in request.GET else "error"
        matterinfo = Tblmatters.objects.get(matters_pk=mid)
        callstaff = Tblstaff.objects.all().filter(staff_active=1)
        mattertype = Tblmattertype.objects.all()
        billingtype = Tblbillingtype.objects.all()
        content = {'page_title': "Edit Matter","billingtype":billingtype,"callstaff":callstaff,
                   "mid":mid,"mattertype":mattertype,"matterinfo":matterinfo}
        return render_template(request, "editmatter.htm", content)

class ViewMatterClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        mid = request.GET['mid'] if 'mid' in request.GET else "error"
        matterinfo = Tblmatters.objects.get(matters_pk=mid)
        callstaff = Tblstaff.objects.all().filter(staff_active=1)
        mattertype = Tblmattertype.objects.all()
        billingtype = Tblbillingtype.objects.all()
        viewcases= Tblcasenotes.objects.all().filter(casenotes_matterpk=mid)
        mattertasks = Tblmattertasks.objects.all().filter(mattertasks_matterpk=mid)
        content = {'page_title': "Edit Matter","billingtype":billingtype,"callstaff":callstaff,"viewcases":viewcases,
                   "mid":mid,"mattertype":mattertype,"matterinfo":matterinfo,"mattertasks":mattertasks,}
        return render_template(request, "viewmatter.htm", content)


class ViewFactMemoClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        mid = request.GET['mid'] if 'mid' in request.GET else "error"
        matterinfo = Tblmatters.objects.get(matters_pk=mid)
        callstaff = Tblstaff.objects.all().filter(staff_active=1)
        mattertype = Tblmattertype.objects.all()
        billingtype = Tblbillingtype.objects.all()
        viewcases= Tblcasenotes.objects.all().filter(casenotes_matterpk=mid)
        mattertasks = Tblmattertasks.objects.all().filter(mattertasks_matterpk=mid)
        content = {'page_title': "Edit Matter","billingtype":billingtype,"callstaff":callstaff,"viewcases":viewcases,
                   "mid":mid,"mattertype":mattertype,"matterinfo":matterinfo,"mattertasks":mattertasks,}
        return render_template(request, "factmemo.htm", content)

class ViewContactRecordsClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        mid = request.GET['mid'] if 'mid' in request.GET else "error"
        matterinfo = Tblmatters.objects.get(matters_pk=mid)
        callstaff = Tblstaff.objects.all().filter(staff_active=1)
        mattertype = Tblmattertype.objects.all()
        billingtype = Tblbillingtype.objects.all()
        
        allitems = Tblcalls.objects.raw('''SELECT tblCalls.Calls_PK, tblCalls.Calls_ContactID, tblCalls.Calls_DateTime, tblCalls.Calls_StaffID, tblCalls.Calls_CallSource1, tblCalls.Calls_CallSource2, 
    tblCalls.Calls_CallSource3, tblCalls.Calls_Message, tblCalls.Calls_ReceptionID, tblCalls.Calls_CallActionID, tblCalls.Calls_CallTypeID, tblCalls.Calls_FollowUpMemo 
    FROM tblCalls INNER JOIN tblMatters ON tblCalls.Calls_ContactID = tblMatters.Matters_ClientID1 WHERE (tblMatters.Matters_PK = '''+mid+''') ORDER BY tblCalls.Calls_DateTime DESC''')
        content = {'page_title': "Edit Matter","billingtype":billingtype,"callstaff":callstaff,
                   "mid":mid,"mattertype":mattertype,"matterinfo":matterinfo,"allitems":allitems,}
        return render_template(request, "conrecords.htm", content)


class ViewMattersClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        cid = request.GET['cid'] if 'cid' in request.GET else "error"
        if 'cname' in request.GET and request.GET['cname'] != "":
            cname = " and (tblcontact.contact_firstName like '%%"+request.GET['cname']+"%%' or tblcontact.contact_lastName like '%%"+request.GET['cname']+"%%' or tblcontact.contact_telephone like '%%"+request.GET['cname']+"%%' or tblcontact.contact_company like '%%"+request.GET['cname']+"%%') "
        else:
            cname = ""
        if 'noof' in request.GET and request.GET['noof'] != "":
            noof = request.GET['noof']
        else:
            noof = 25 
        allmatters = Tblmatters.objects.raw(''' SELECT Contact_PK,tblcontact.contact_pk, tblcontact.Contact_FirstName, tblcontact.Contact_LastName,
                                                tblcontact.contact_company,Matters_PK, tblmatters.matters_matterid, tblmatters.matters_pk,
                                                tblcontact.contact_telephone FROM tblcontact INNER JOIN
                                                tblmatters ON tblcontact.contact_pk = tblmatters.matters_clientid1 where tblcontact.contact_pk>0 '''+cname+''' order by matters_mattertype, matters_dateopened limit '''+str(noof)+'''''')
        mattertype = Tblmattertype.objects.all()
        billingtype = Tblbillingtype.objects.all()
         
        content = {'page_title': "View Matter", "allitems":allmatters, "cid":cid,
                   "billingtype":billingtype,"mattertype":mattertype}
        return render_template(request, "viewmatters.htm", content)

class AddPaymentFormClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        mid = request.GET['mid'] if 'mid' in request.GET else "error"
        viewpayments= Tblpayments.objects.all().filter(payments_matterpk=mid)
        matterinfo = Tblmatters.objects.get(matters_pk=mid)
        paymentmethods = Tblpaymentmethods.objects.all()
        content = {'page_title': "Add Payment","viewpayments":viewpayments,
                   "paymentmethods":paymentmethods,"mid":mid,"matterinfo":matterinfo}
        return render_template(request, "addpayment.htm", content)

class ViewPaymentsClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        mid = request.GET['mid'] if 'mid' in request.GET else "error"
        viewpayments= Tblpayments.objects.all().filter(payments_matterpk=mid)
        matterinfo = Tblmatters.objects.get(matters_pk=mid)
        paymentmethods = Tblpaymentmethods.objects.all()
        content = {'page_title': "View Payments","viewpayments":viewpayments,
                   "paymentmethods":paymentmethods,"mid":mid,"matterinfo":matterinfo}
        return render_template(request, "vpays.htm", content)


class EditPaymentFormClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        pid = request.GET['pid'] if 'pid' in request.GET else "error"
        viewpayments= Tblpayments.objects.get(payments_pk=pid)
         
        paymentmethods = Tblpaymentmethods.objects.all()
        content = {'page_title': "Edit Payment","viewpayments":viewpayments,
                   "paymentmethods":paymentmethods,"pid":pid,}
        return render_template(request, "editpayment.htm", content)


class ViewTasksFormClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        mid = request.GET['mid'] if 'mid' in request.GET else "error"
        matterinfo = Tblmatters.objects.get(matters_pk=mid)
        mattertasks = Tblmattertasks.objects.all().filter(mattertasks_matterpk=mid)
        callstaff = Tblstaff.objects.all().filter(staff_active=1)
        content = {'page_title': "Add Payment",
                   "mattertasks":mattertasks,"mid":mid,"callstaff":callstaff}
        return render_template(request, "addtasks.htm", content)

class EditTasksFormClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        tid = request.GET['tid'] if 'tid' in request.GET else "error"
         
        mattertasks = Tblmattertasks.objects.get(mattertasks_pk=tid)
        callstaff = Tblstaff.objects.all().filter(staff_active=1)
        content = {'page_title': "Edit Task",
                   "mattertasks":mattertasks,"tid":tid,"callstaff":callstaff}
        return render_template(request, "edittast.htm", content)

class AddCaseFormClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        mid = request.GET['mid'] if 'mid' in request.GET else "error"
        viewcases= Tblcasenotes.objects.all().filter(casenotes_matterpk=mid)
        
        callstaff = Tblstaff.objects.all().filter(staff_active=1)
        content = {'page_title': "Add Case","viewcases":viewcases,
                   "callstaff":callstaff,"mid":mid}
        return render_template(request, "addcase.htm", content)

class PractiseManagerViewClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        content = {'page_title': "Practice Manager",}
        return render_template(request, "pracman.htm", content)

class ActiveFamilyViewClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        allitems = ViewActivedr.objects.filter(matters_pk__gt=0)
        count = CountActivedr.objects.all()
        logging.info('count::  %s', count)
        content = {'page_title': "Practice Manager","count":count,"allitems":allitems}
        return render_template(request, "actdr.htm", content)

class ActiveBankruptcyViewClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        allitems = ViewActivebcy.objects.filter(matters_pk__gt=0)
        count = CountActivebcy.objects.all()
        logging.info('count::  %s', count)
        content = {'page_title': "Practice Manager","count":count,"allitems":allitems}
        return render_template(request, "actbcy.htm", content)

class ActivePersonalViewClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        allitems = ViewActivecontingency.objects.filter(matters_pk__gt=0)
        count = CountActivecontingency.objects.all()
        logging.info('count::  %s', count)
        content = {'page_title': "Practice Manager","count":count,"allitems":allitems}
        return render_template(request, "actpi.htm", content)

class ActiveEstateViewClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        allitems = ViewActiveep.objects.filter(matters_pk__gt=0)
        count = CountActiveep.objects.all()
        logging.info('count::  %s', count)
        content = {'page_title': "Practice Manager","count":count,"allitems":allitems}
        return render_template(request, "actep.htm", content)

class ActiveProbateViewClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        allitems = ViewActiveprobate.objects.filter(matters_pk__gt=0)
        count = CountActiveprobate.objects.all()
        logging.info('count::  %s', count)
        content = {'page_title': "Practice Manager","count":count,"allitems":allitems}
        return render_template(request, "actprobate.htm", content)

class ActiveTransactionalViewClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        allitems = ViewActivetransactional.objects.filter(matters_pk__gt=0)
        count = CountActivetransactional.objects.all()
        logging.info('count::  %s', count)
        content = {'page_title': "Practice Manager","count":count,"allitems":allitems}
        return render_template(request, "acttransac.htm", content)

class ActiveCivilViewClass(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        allitems = ViewActivecivil.objects.filter(matters_pk__gt=0)
        count = CountActivecivil.objects.all()
        logging.info('count::  %s', count)
        content = {'page_title': "Practice Manager","count":count,"allitems":allitems}
        return render_template(request, "actcivil.htm", content)


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

