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
from django.contrib.auth.models import User, Group, Permission
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import unittest
from django.core.context_processors import csrf
from forms import *
from views import *
from models import *
from google.appengine.api import mail
import logging, random, hashlib, datetime, settings

#from django.db import connection, transaction
PERPAGE=50
class CsrfExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CsrfExemptMixin, self).dispatch(request, *args, **kwargs)

@csrf_exempt
def render_template(request, template, data=None):
    errs =""
    if request.method == 'GET' and 'err' in request.GET:
        data.update({'errs':request.GET['err']})
    
    response = render_to_response(template, data,
                              context_instance=RequestContext(request))
    return response

class CallsActionClass(LoginRequiredMixin,TemplateView):
    def get(self, request, *args, **kwargs):
        if "action" in request.GET and request.GET['action'] == "delcid":
            #logging.info('status type:: %s',request.POST['status'])
            try:
                Tblcontact.objects.filter(contact_pk=request.GET['cid']).delete()
                
                return HttpResponseRedirect('/viewcontacts?msg=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponseRedirect('/viewcontacts?err=Form Field Errors')

        elif "action" in request.GET and request.GET['action'] == "delcallid":
            #logging.info('status type:: %s',request.POST['status'])
            try:
                t = Tblcalls.objects.get(calls_pk=request.GET['cid'])
                t.calls_deleted = 1
                t.save()
                #Tblcalls.objects.filter(calls_pk=request.GET['cid']).delete()
                return HttpResponseRedirect('/viewcalls?msg=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponseRedirect('/viewcalls?err=Form Field Errors')
        else:
            return HttpResponseRedirect('/?err=Form Field Errors')
    def post(self, request, *args, **kwargs):
        if "action" in request.POST and request.POST['action'] == "addcontactsss":
            #logging.info('status type:: %s',request.POST['status'])
            try:
                s = Tblcontact(contact_addedby = request.session['Staff'].staff_pk, sendername = "",
                                sender = 1, message = request.POST['message'],
                                datentime = datetime.datetime.now())
                s.save()
                return HttpResponseRedirect('/editrequestform?crmid='+crmid+'&err=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponseRedirect('/acrm?page=1&err=Form Field Errors')
        elif "action" in request.POST and request.POST['action'] == "addnewcall":
            logging.info('LoginfoMessage:: %s',request.POST['calls_callactive']) 
            try:
                s = Tblcalls(addedby = request.session['Staff'].staff_pk,calls_opencall = 1,
                             calls_contactid = request.POST['calls_contactid'], calls_staffid = request.POST['calls_staffid'],
                             calls_callsource1 = request.POST['calls_callsource1'], calls_callsource2 = request.POST['calls_callsource2'],
                             calls_callsource3 = request.POST['calls_callsource3'], calls_message = request.POST['calls_message'],
                             calls_receptionid = request.POST['calls_receptionid'], calls_callactionid = request.POST['calls_callactionid'],
                             calls_calltypeid = request.POST['calls_calltypeid'], calls_callactive = 1,Calls_Deleted=0,
                             calls_datetime = datetime.datetime.now())
                s.save()
                return HttpResponseRedirect('/viewcalls?msg=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponseRedirect('/viewcalls?err=Form Field Errors')
        elif "action" in request.POST and request.POST['action'] == "edtcall":
            try:
                t = Tblcalls.objects.get(calls_pk=request.POST['calls_pk'])
                #t.calls_contactid = request.POST['calls_contactid']
                t.calls_staffid = request.POST['calls_staffid']
                t.calls_callsource1 = request.POST['calls_callsource1']
                t.calls_callsource2 = request.POST['calls_callsource2']
                t.calls_callsource3 = request.POST['calls_callsource3']
                t.calls_message = request.POST['calls_message']
                t.calls_receptionid = request.POST['calls_receptionid']
                t.calls_callactionid = request.POST['calls_callactionid']
                t.calls_calltypeid = request.POST['calls_calltypeid']
                t.calls_callactive = request.POST['calls_callactive']
                
                t.save()
                return HttpResponseRedirect('/viewcalls?msg=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponseRedirect('/viewcalls?err=Form Field Errors')
        elif "action" in request.POST and request.POST['action'] == "addcontact":
            
            try:
                s = Tblcontact(contact_addedby = request.session['Staff'].staff_pk, contact_lastname = request.POST['contact_lastname'],
                               contact_company = request.POST['contact_company'], contact_email = request.POST['contact_email'],
                               contact_address1 = request.POST['contact_address1'], contact_address2 = request.POST['contact_address2'],
                               contact_city = request.POST['contact_city'], contact_state = request.POST['contact_state'],
                               contact_zip = request.POST['contact_zip'], contact_telephone = request.POST['contact_telephone'],
                               contact_type = request.POST['contact_type'], contact_firstname = request.POST['contact_firstname'],
                               contact_datecreated = datetime.datetime.now())
                s.save()
                return HttpResponseRedirect('/viewcontacts?msg=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponseRedirect('/viewcontacts?err=Form Field Errors')
        elif "action" in request.POST and request.POST['action'] == "editcontact":
            try:
                t = Tblcontact.objects.get(contact_pk=request.POST['contact_pk'])
                t.contact_firstname = request.POST['contact_firstname']
                t.contact_lastname = request.POST['contact_lastname']
                t.contact_company = request.POST['contact_company']
                t.contact_email = request.POST['contact_email']
                t.contact_address1 = request.POST['contact_address1']
                t.contact_address2 = request.POST['contact_address2']
                t.contact_city = request.POST['contact_city']
                t.contact_state = request.POST['contact_state']
                t.contact_zip = request.POST['contact_zip']
                t.contact_telephone = request.POST['contact_telephone']
                t.contact_type = request.POST['contact_type']
                logging.info('Contact Type:: %s',request.POST['contact_type'])
                t.save()
                return HttpResponseRedirect('/viewcontacts?msg=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponseRedirect('/viewcontacts?err=Form Field Errors')
        else:
            return HttpResponseRedirect('/myaccount?err=Form Field Errors')

class MatterActionClass(LoginRequiredMixin,TemplateView):
    def get(self, request, *args, **kwargs):
        if "action" in request.GET and request.GET['action'] == "delcid":
            #logging.info('status type:: %s',request.POST['status'])
            try:
                Tblcontact.objects.filter(contact_pk=request.GET['cid']).delete()
                
                return HttpResponseRedirect('/viewcontacts?msg=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponseRedirect('/viewcontacts?err=Form Field Errors')

        elif "action" in request.GET and request.GET['action'] == "delcallid":
            #logging.info('status type:: %s',request.POST['status'])
            try:
                t = Tblcalls.objects.get(calls_pk=request.GET['cid'])
                t.calls_deleted = 1
                t.save()
                #Tblcalls.objects.filter(calls_pk=request.GET['cid']).delete()
                return HttpResponseRedirect('/viewcalls?msg=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponseRedirect('/viewcalls?err=Form Field Errors')
        elif "action" in request.GET and request.GET['action'] == "delpayid":
            #logging.info('status type:: %s',request.POST['status'])
            try:
                Tblpayments.objects.filter(payments_pk=request.GET['pid']).delete()
                return HttpResponseRedirect('/viewmatters?msg=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponseRedirect('/viewmatters?err=Form Field Errors')
        elif "action" in request.GET and request.GET['action'] == "deltaskid":
            #logging.info('status type:: %s',request.POST['status'])
            try:
                Tblmattertasks.objects.filter(mattertasks_pk=request.GET['tid']).delete()
                return HttpResponseRedirect('/viewmatters?msg=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponseRedirect('/viewmatters?err=Form Field Errors')
        else:
            return HttpResponseRedirect('/?err=Form Field Errors')
    def post(self, request, *args, **kwargs):
        if "action" in request.POST and request.POST['action'] == "addmatter":
            #logging.info('status type:: %s',request.POST['status'])
            try:
                s = Tblmatters(matters_matterid = request.POST['matters_matterid'],
                               matters_clientid1 = request.POST['matters_clientid1'], matters_primaryattorney = request.POST['matters_primaryattorney'],
                               matters_supportattorney1 = request.POST['matters_supportattorney1'], matters_dateopened = request.POST['matters_dateopened'],
                               matters_supportattorney2 = request.POST['matters_supportattorney2'], matters_mattertype = request.POST['matters_mattertype'],
                               matters_billingtype = request.POST['matters_billingtype'], matters_active = 1, matters_intakememo = "",
                               matters_datecreated = datetime.datetime.now())
                s.save()
                return HttpResponseRedirect('/viewmatters?msg=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponseRedirect('/viewmatters?page=1&err=Form Field Errors')
        elif "action" in request.POST and request.POST['action'] == "maddpayments":
            try:
                s = Tblpayments(payments_matterpk = request.POST['payments_matterpk'], payments_methodpk = request.POST['payments_methodpk'],
                                payments_amount = request.POST['payments_amount'], payments_receiveddate = request.POST['payments_receiveddate'],
                                payments_clientpk = request.POST['payments_clientpk'], payments_staffpk = request.POST['payments_staffpk'])
                s.save()
                return HttpResponseRedirect('/viewmatters?msg=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponseRedirect('/viewmatters?page=1&err=Form Field Errors')
        elif "action" in request.POST and request.POST['action'] == "edipayment":
            try:
                s = Tblpayments.objects.get(payments_pk=request.POST['payments_pk'])
                s.payments_methodpk = request.POST['payments_methodpk']
                s.payments_amount = request.POST['payments_amount']
                s.payments_receiveddate = request.POST['payments_receiveddate']
                s.save()
                return HttpResponseRedirect('/viewmatters?msg=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponseRedirect('/viewmatters?page=1&err=Form Field Errors')
        elif "action" in request.POST and request.POST['action'] == "matteredit":
            try:
                t = Tblmatters.objects.get(matters_pk=request.POST['mid'])
                t.matters_primaryattorney = request.POST['matters_primaryattorney']
                t.matters_supportattorney1 = request.POST['matters_supportattorney1']
                t.matters_supportattorney2 = request.POST['matters_supportattorney2']
                t.matters_dateopened = request.POST['matters_dateopened']
                t.matters_dateclosed = request.POST['matters_dateclosed']
                t.matters_caseclosed = request.POST['matters_caseclosed']
                t.matters_mattertype = request.POST['matters_mattertype']
                t.matters_billingtype = request.POST['matters_billingtype']
                t.matters_matterid = request.POST['matters_matterid']
                t.save()
                logging.info('Matter ID:: %s',request.POST['matters_matterid'])
                return HttpResponseRedirect('/viewmatters?msg=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponse('/viewmatters?err=Form Field Errors')
        elif "action" in request.POST and request.POST['action'] == "factedit":
            try:
                mid=request.POST['mid']
                t = Tblmatters.objects.get(matters_pk=mid)
                t.matters_intakememo = request.POST['matters_intakememo']
                t.save()
                return HttpResponseRedirect('/fmemo?mid='+mid+'&msg=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponse('/viewmatters?err=Form Field Errors')
        elif "action" in request.POST and request.POST['action'] == "maddtask":
            try:
                
                s = Tblmattertasks(mattertasks_matterpk = request.POST['mattertasks_matterpk'],
                               mattertasks_text = request.POST['mattertasks_text'], mattertasks_subject = request.POST['mattertasks_subject'],
                               mattertasks_datecreated = request.POST['mattertasks_datecreated'], mattertasks_duedate = request.POST['mattertasks_duedate'],
                               mattertasks_assignedstaff1pk = request.POST['mattertasks_assignedstaff1pk'], mattertasks_assignedstaff2pk = request.POST['mattertasks_assignedstaff2pk'],
                               mattertasks_staffcreatorpk = request.session['Staff'].staff_pk, mattertasks_taskcomplete = 0)
                s.save()
                return HttpResponseRedirect('/viewmatters?msg=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponseRedirect('/viewmatters?err=Form Field Errors')
        elif "action" in request.POST and request.POST['action'] == "maddcase":
            try:
                
                s = Tblcasenotes(casenotes_matterpk = request.POST['casenotes_matterpk'],
                               casenotes_notedate = request.POST['casenotes_notedate'], casenotes_staffpk = request.POST['casenotes_staffpk'],
                               casenotes_notesubject = request.POST['casenotes_notesubject'], casenotes_notetext = request.POST['casenotes_notetext'])
                s.save()
                return HttpResponseRedirect('/viewmatters?msg=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponseRedirect('/viewmatters?err=Form Field Errors')
        elif "action" in request.POST and request.POST['action'] == "addrmarequest":
            try:
                oid=request.POST['oid']
                rmaid = oid
                s = Rma(orderid = oid,idrmamethod = 1, idrmareason=1, idrmastatus=1,comments = request.POST['message'],
                                rmadate = datetime.datetime.now(), idrmaaction="0",qty_received=0,qty_restock=0)
                s.save()
                return HttpResponseRedirect('/rmaservice?crmid='+oid+'&err=Successfully Updated the Record')
            except Exception, e:
                logging.info('LoginfoMessage:: %s',e)
                return HttpResponseRedirect('/rmaservice?crmid='+rmaid+'&err=Form Field Errors')
        else:
            return HttpResponseRedirect('/?err=Form Field Errors')

