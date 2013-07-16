from django import template
from models import *
from django.db import models
from django.db.models import Count, Min, Sum, Max, Avg
from django.db import connection, transaction
import logging, datetime
register = template.Library()


from datetime import date, timedelta
@register.filter(name='fromunix')
def fromunix(value):
    return datetime.datetime.fromtimestamp(int(value)/1000)

@register.filter("contacttypes")
def contacttypes(objid,field=""):
    result = ""
    #logging.info('Call Type Id:: %s',objid)
    try:
        if objid =="all":
            result = Tblcontacttype.objects.all()
        else:
            resultq = Tblcontacttype.objects.all().filter(contact_typepk = objid)
            for crms in resultq:
                result = crms.contact_typedesc
    except Exception as e:
        result = ""
        logging.info('LoginfoMessage:: %s',e)
    return result

@register.filter("contactsvalue")
def contactsvalue(cid,field=""):
    result = ""
    try:
        crm_obj = Tblcontact.objects.all().filter(contact_pk = cid)
        for crms in crm_obj:
            if field == "contact_email":
                result = crms.contact_email
            elif field == "contact_telephone":
                result = crms.contact_telephone
            else:
                result = str(crms.contact_firstname)+' '+str(crms.contact_lastname)
    except Exception as e:
        crm_id = e
        logging.info('LoginfoMessage Contact Value Error:: %s',e)
    logging.info('LoginfoMessage Contact Result:: %s',result)
    return result

@register.filter("callactions")
def callactions(objid,field=""):
    result = ""
    try:
        crm_obj = Tblcallaction.objects.all().filter(callaction_pk = objid)
        for crms in crm_obj:
            if field == "contact_email":
                result = crms.contact_email
            else:
                result = str(crms.callaction_description)
    except Exception as e:
        crm_id = e
        logging.info('LoginfoMessage Contact Value Error:: %s',e)
    logging.info('LoginfoMessage Contact Result:: %s',result)
    return result

@register.filter("calltypes")
def calltypes(objid,field=""):
    result = ""
    try:
        crm_obj = Tblcalltype.objects.all().filter(calltype_pk = objid)
        for crms in crm_obj:
            if field == "contact_email":
                result = crms.calltype_pk
            else:
                result = str(crms.calltype_description)
    except Exception as e:
        crm_id = e
        logging.info('LoginfoMessage Contact Value Error:: %s',e)
    logging.info('LoginfoMessage Contact Result:: %s',result)
    return result

@register.filter("staffvalues")
def staffvalues(objid,field=""):
    result = ""
    try:
        crm_obj = Tblstaff.objects.all().filter(staff_pk = objid)
        for crms in crm_obj:
            if field == "staff_email":
                result = crms.staff_email
            else:
                result = str(crms.staff_stafffullname)
    except Exception as e:
        crm_id = e
        logging.info('LoginfoMessage Contact Value Error:: %s',e)
    logging.info('LoginfoMessage Contact Result:: %s',result)
    return result

@register.filter("callsources")
def callsources(objid,field=""):
    result = ""
    try:
        crm_obj = Tblcallsource.objects.all().filter(callsource_pk = objid)
        for crms in crm_obj:
            if field == "contact_email":
                result = crms.calltype_pk
            else:
                result = str(crms.callsource_description)
    except Exception as e:
        crm_id = e
        logging.info('LoginfoMessage Contact Value Error:: %s',e)
    logging.info('LoginfoMessage Contact Result:: %s',result)
    return result

@register.filter("matterttpeval")
def matterttpeval(objid,field=""):
    result = ""
    try:
        crm_obj = Tblmattertype.objects.all().filter(mattertype_pk = objid)
        for crms in crm_obj:
            if field == "mattertype_shortdesc":
                result = crms.mattertype_shortdesc
            else:
                result = str(crms.mattertype_desc)
    except Exception as e:
        crm_id = e
        logging.info('LoginfoMessage Contact Value Error:: %s',e)
    logging.info('LoginfoMessage Contact Result:: %s',result)
    return result
