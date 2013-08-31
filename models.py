from django.db import models
from django.contrib.auth.models import User

def validate_not_spaces(value):
    if value.strip() == '':
        
        raise ValidationError(u"You must provide more than just whitespace.")

class CountActivebcy(models.Model):
    count = models.IntegerField(primary_key=True, db_column='COUNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_activebcy'
        app_label = ''

class CountActivecivil(models.Model):
    count = models.IntegerField(primary_key=True, blank=True)
    class Meta:
        db_table = u'count_activecivil'
        app_label = ''

class CountActivecontingency(models.Model):
    count = models.IntegerField(primary_key=True, db_column='COUNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_activecontingency'
        app_label = ''

class CountActivedr(models.Model):
    count = models.IntegerField(primary_key=True, db_column='COUNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_activedr'
        app_label = ''

class CountActiveep(models.Model):
    count = models.IntegerField(primary_key=True, db_column='COUNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_activeep'
        app_label = ''

class CountActiveprobate(models.Model):
    count = models.IntegerField(primary_key=True, db_column='COUNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_activeprobate'
        app_label = ''

class CountActivetransactional(models.Model):
    count = models.IntegerField(primary_key=True, db_column='COUNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_activetransactional'
        app_label = ''

class CountApptsTodayBcy(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_appts_today_bcy'
        app_label = ''

class CountApptsTodayDom(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_appts_today_dom'
        app_label = ''

class CountApptsTodayDr(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_appts_today_dr'
        app_label = ''

class CountApptsTodayEp(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_appts_today_ep'
        app_label = ''

class CountApptsTodayPi(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_appts_today_pi'
        app_label = ''

class CountCallsToday(models.Model):
    todaycalls = models.IntegerField(null=True, db_column='TodayCalls', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_calls_today'
        app_label = ''

class CountCallsTodayBcy(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_calls_today_bcy'
        app_label = ''

class CountCallsTodayDom(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_calls_today_dom'
        app_label = ''

class CountCallsTodayDr(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_calls_today_dr'
        app_label = ''

class CountCallsTodayEp(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_calls_today_ep'
        app_label = ''

class CountCallsTodayPi(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_calls_today_pi'
        app_label = ''

class CountNewmattersbymonthBcy(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    bcymatters = models.IntegerField(null=True, db_column='BCYMatters', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_newmattersbymonth_bcy'
        app_label = ''

class CountNewmattersbymonthDr(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    drmatters = models.IntegerField(null=True, db_column='DRMatters', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_newmattersbymonth_dr'
        app_label = ''

class CountNewmattersbymonthEp(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    drmatters = models.IntegerField(null=True, db_column='DRMatters', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_newmattersbymonth_ep'
        app_label = ''

class CountNewmattersbymonthPi(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    bcymatters = models.IntegerField(null=True, db_column='BCYMatters', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_newmattersbymonth_pi'
        app_label = ''

class CountNewmattersbymonthProbate(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    probatematters = models.IntegerField(null=True, db_column='ProbateMatters', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_newmattersbymonth_probate'
        app_label = ''

class Countcalls12Monthstrailingdr(models.Model):
    callyear = models.IntegerField(null=True, db_column='CallYear', blank=True) # Field name made lowercase.
    callmonth = models.IntegerField(null=True, db_column='CallMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls12monthstrailingdr'
        app_label = ''

class Countcalls12Monthstrailingep(models.Model):
    callyear = models.IntegerField(null=True, db_column='CallYear', blank=True) # Field name made lowercase.
    callmonth = models.IntegerField(null=True, db_column='CallMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls12monthstrailingep'
        app_label = ''

class Countcalls12Monthstrailingnewcontacts(models.Model):
    callyear = models.IntegerField(null=True, db_column='CallYear', blank=True) # Field name made lowercase.
    callmonth = models.IntegerField(null=True, db_column='CallMonth', blank=True) # Field name made lowercase.
    callsource = models.CharField(max_length=150, db_column='CallSource', blank=True) # Field name made lowercase.
    calltype = models.CharField(max_length=150, db_column='CallType', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls12monthstrailingnewcontacts'
        app_label = ''

class Countcalls12Monthstrailingpi(models.Model):
    callyear = models.IntegerField(null=True, db_column='CallYear', blank=True) # Field name made lowercase.
    callmonth = models.IntegerField(null=True, db_column='CallMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls12monthstrailingpi'
        app_label = ''

class Countcalls12Monthstrailingprobate(models.Model):
    callyear = models.IntegerField(null=True, db_column='CallYear', blank=True) # Field name made lowercase.
    callmonth = models.IntegerField(null=True, db_column='CallMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls12monthstrailingprobate'
        app_label = ''

class Countcalls12Monthstrailybcy(models.Model):
    callyear = models.IntegerField(null=True, db_column='CallYear', blank=True) # Field name made lowercase.
    callmonth = models.IntegerField(null=True, db_column='CallMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls12monthstrailybcy'
        app_label = ''

class Countcalls30Daystrailingbcy(models.Model):
    calldate = models.IntegerField(null=True, db_column='CallDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls30daystrailingbcy'
        app_label = ''

class Countcalls30Daystrailingdr(models.Model):
    calldate = models.IntegerField(null=True, db_column='CallDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls30daystrailingdr'
        app_label = ''

class Countcalls30Daystrailingep(models.Model):
    calldate = models.IntegerField(null=True, db_column='CallDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls30daystrailingep'
        app_label = ''

class Countcalls30Daystrailingpi(models.Model):
    calldate = models.IntegerField(null=True, db_column='CallDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls30daystrailingpi'
        app_label = ''

class Countcalls30Daystrailingprobate(models.Model):
    calldate = models.IntegerField(null=True, db_column='CallDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls30daystrailingprobate'
        app_label = ''

class Countnewmatters2Yearstrailingdr(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters2yearstrailingdr'
        app_label = ''

class Countnewmatters2Yearstrailingep(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters2yearstrailingep'
        app_label = ''

class Countnewmatters2Yearstrailingprobate(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters2yearstrailingprobate'
        app_label = ''

class Countnewmatters2Yrstrailingbcy(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters2yrstrailingbcy'
        app_label = ''

class Countnewmatters2Yrstrailingpi(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters2yrstrailingpi'
        app_label = ''

class Countnewmatters30Daystrailingbcy(models.Model):
    matterdate = models.IntegerField(null=True, db_column='MatterDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters30daystrailingbcy'
        app_label = ''

class Countnewmatters30Daystrailingdr(models.Model):
    matterdate = models.IntegerField(null=True, db_column='MatterDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters30daystrailingdr'
        app_label = ''

class Countnewmatters30Daystrailingep(models.Model):
    matterdate = models.IntegerField(null=True, db_column='MatterDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters30daystrailingep'
        app_label = ''

class Countnewmatters30Daystrailingpi(models.Model):
    matterdate = models.IntegerField(null=True, db_column='MatterDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters30daystrailingpi'
        app_label = ''

class Countnewmatters30Daystrailingprobate(models.Model):
    matterdate = models.IntegerField(null=True, db_column='MatterDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters30daystrailingprobate'
        app_label = ''

class Tblbillingtype(models.Model):
    billingtype_pk = models.IntegerField(primary_key=True, db_column='BillingType_PK') # Field name made lowercase.
    billingtype_desc = models.CharField(max_length=150, db_column='BillingType_Desc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblbillingtype'
        app_label = ''
        
class Tblcallaction(models.Model):
    callaction_pk = models.IntegerField(primary_key=True, db_column='CallAction_PK') # Field name made lowercase.
    callaction_description = models.CharField(max_length=150, db_column='CallAction_Description', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblcallaction'
        app_label = ''

class Tblcalls(models.Model):
    calls_pk = models.IntegerField(primary_key=True, db_column='Calls_PK') # Field name made lowercase.
    calls_contactid = models.IntegerField(null=True, db_column='Calls_ContactID', blank=True) # Field name made lowercase.
    calls_datetime = models.DateTimeField(null=True, db_column='Calls_DateTime', blank=True) # Field name made lowercase.
    calls_opencall = models.TextField(db_column='Calls_OpenCall', blank=True) # Field name made lowercase. This field type is a guess.
    calls_staffid = models.IntegerField(db_column='Calls_StaffID') # Field name made lowercase.
    calls_callsource1 = models.IntegerField(db_column='Calls_CallSource1') # Field name made lowercase.
    calls_callsource2 = models.IntegerField(db_column='Calls_CallSource2') # Field name made lowercase.
    calls_callsource3 = models.IntegerField(db_column='Calls_CallSource3') # Field name made lowercase.
    calls_message = models.TextField(db_column='Calls_Message', blank=True) # Field name made lowercase.
    calls_receptionid = models.IntegerField(db_column='Calls_ReceptionID') # Field name made lowercase.
    calls_callactionid = models.IntegerField(db_column='Calls_CallActionID') # Field name made lowercase.
    calls_calltypeid = models.IntegerField(db_column='Calls_CallTypeID') # Field name made lowercase.
    calls_callactive = models.TextField(db_column='Calls_CallActive') # Field name made lowercase. This field type is a guess.
    calls_matterid = models.IntegerField(null=True, db_column='Calls_MatterID', blank=True) # Field name made lowercase.
    calls_followupmemo = models.TextField(db_column='Calls_FollowUpMemo', blank=True) # Field name made lowercase.
    calls_deleted = models.CharField(max_length=150, db_column='Calls_Deleted', blank=True) # Field name made lowercase.
    addedby = models.IntegerField(null=True, db_column='addedby', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblcalls'
        app_label = ''

class Tblcallsource(models.Model):
    callsource_pk = models.IntegerField(primary_key=True, db_column='CallSource_PK') # Field name made lowercase.
    callsource_description = models.CharField(max_length=150, db_column='CallSource_Description', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblcallsource'
        app_label = ''

class Tblcalltype(models.Model):
    calltype_pk = models.IntegerField(primary_key=True, db_column='CallType_PK') # Field name made lowercase.
    calltype_description = models.CharField(max_length=150, db_column='CallType_Description', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblcalltype'
        app_label = ''

class Tblstaff(models.Model):
    staff_pk = models.IntegerField(primary_key=True, db_column='Staff_PK') # Field name made lowercase.
    staff_staffinitials = models.CharField(max_length=150, db_column='Staff_StaffInitials', blank=True) # Field name made lowercase.
    staff_stafffullname = models.CharField(max_length=150, db_column='Staff_StaffFullName', blank=True) # Field name made lowercase.
    staff_accesslevel = models.IntegerField(null=True, db_column='Staff_AccessLevel', blank=True) # Field name made lowercase.
    staff_password = models.CharField(max_length=150, db_column='Staff_Password', blank=True) # Field name made lowercase.
    staff_active = models.TextField(db_column='Staff_Active', blank=True) # Field name made lowercase. This field type is a guess.
    staff_level = models.CharField(max_length=150, db_column='Staff_Level', blank=True) # Field name made lowercase.
    staff_lastname = models.CharField(max_length=150, db_column='Staff_LastName', blank=True) # Field name made lowercase.
    staff_firstname = models.CharField(max_length=150, db_column='Staff_FirstName', blank=True) # Field name made lowercase.
    staff_extension = models.CharField(max_length=150, db_column='Staff_Extension', blank=True) # Field name made lowercase.
    staff_mobile = models.CharField(max_length=150, db_column='Staff_Mobile', blank=True) # Field name made lowercase.
    staff_email = models.CharField(max_length=150, db_column='Staff_Email', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblstaff'
        app_label = ''

class Tblcasecontacts(models.Model):
    casecontacts_pk = models.IntegerField(primary_key=True, db_column='CaseContacts_PK') # Field name made lowercase.
    casecontacts_matterpk = models.IntegerField(db_column='CaseContacts_MatterPK') # Field name made lowercase.
    casecontacts_oc1 = models.IntegerField(null=True, db_column='CaseContacts_OC1', blank=True) # Field name made lowercase.
    casecontacts_oc2 = models.IntegerField(null=True, db_column='CaseContacts_OC2', blank=True) # Field name made lowercase.
    casecontacts_oc3 = models.IntegerField(null=True, db_column='CaseContacts_OC3', blank=True) # Field name made lowercase.
    casecontacts_judge = models.IntegerField(null=True, db_column='CaseContacts_Judge', blank=True) # Field name made lowercase.
    casecontacts_ja = models.IntegerField(null=True, db_column='CaseContacts_JA', blank=True) # Field name made lowercase.
    casecontacts_cocounsel1 = models.IntegerField(null=True, db_column='CaseContacts_CoCounsel1', blank=True) # Field name made lowercase.
    casecontacts_cocounsel2 = models.IntegerField(null=True, db_column='CaseContacts_CoCounsel2', blank=True) # Field name made lowercase.
    casecontacts_adjuster1 = models.IntegerField(null=True, db_column='CaseContacts_Adjuster1', blank=True) # Field name made lowercase.
    casecontacts_adjuster2 = models.IntegerField(null=True, db_column='CaseContacts_Adjuster2', blank=True) # Field name made lowercase.
    casecontacts_med1 = models.IntegerField(null=True, db_column='CaseContacts_Med1', blank=True) # Field name made lowercase.
    casecontacts_med2 = models.IntegerField(null=True, db_column='CaseContacts_Med2', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblcasecontacts'
        app_label = ''

class Tblcasenotes(models.Model):
    casenotes_pk = models.IntegerField(primary_key=True, db_column='CaseNotes_PK') # Field name made lowercase.
    casenotes_matterpk = models.IntegerField(null=True, db_column='CaseNotes_MatterPK', blank=True) # Field name made lowercase.
    casenotes_notedate = models.DateField(null=True, db_column='CaseNotes_NoteDate', blank=True) # Field name made lowercase.
    casenotes_notetext = models.TextField(db_column='CaseNotes_NoteText', blank=True) # Field name made lowercase.
    casenotes_notesubject = models.TextField(db_column='CaseNotes_NoteSubject', blank=True) # Field name made lowercase.
    casenotes_staffpk = models.IntegerField(null=True, db_column='CaseNotes_StaffPK', blank=True) # Field name made lowercase.
    casenotes_billabletime = models.DecimalField(decimal_places=2, null=True, max_digits=6, db_column='CaseNotes_BillableTime', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblcasenotes'
        app_label = ''

class Tblcontact(models.Model):
    contact_pk = models.IntegerField(primary_key=True, db_column='Contact_PK') # Field name made lowercase.
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_middlename = models.CharField(max_length=360, db_column='Contact_MiddleName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    contact_company = models.CharField(max_length=360, db_column='Contact_Company', blank=True) # Field name made lowercase.
    contact_address1 = models.CharField(max_length=360, db_column='Contact_Address1', blank=True) # Field name made lowercase.
    contact_address2 = models.CharField(max_length=360, db_column='Contact_Address2', blank=True) # Field name made lowercase.
    contact_city = models.CharField(max_length=360, db_column='Contact_City', blank=True) # Field name made lowercase.
    contact_state = models.CharField(max_length=360, db_column='Contact_State', blank=True) # Field name made lowercase.
    contact_zip = models.CharField(max_length=30, db_column='Contact_ZIP', blank=True) # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    contact_telephone2 = models.CharField(max_length=135, db_column='Contact_Telephone2', blank=True) # Field name made lowercase.
    contact_fax = models.CharField(max_length=135, db_column='Contact_Fax', blank=True) # Field name made lowercase.
    contact_email = models.CharField(max_length=360, db_column='Contact_Email', blank=True) # Field name made lowercase.
    contact_alternatecontact = models.CharField(max_length=135, db_column='Contact_AlternateContact', blank=True) # Field name made lowercase.
    contact_accountnumber = models.IntegerField(null=True, db_column='Contact_AccountNumber', blank=True) # Field name made lowercase.
    contact_client = models.TextField(db_column='Contact_Client', blank=True) # Field name made lowercase. This field type is a guess.
    contact_memo = models.TextField(db_column='Contact_Memo', blank=True) # Field name made lowercase.
    contact_datecreated = models.DateTimeField(null=True, db_column='Contact_DateCreated', blank=True) # Field name made lowercase.
    contact_type = models.IntegerField(null=True, db_column='Contact_Type', blank=True) # Field name made lowercase.
    contact_addedby = models.IntegerField(null=True, db_column='Contact_AddedBy', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblcontact'
        app_label = ''

class Tblcontacttype(models.Model):
    contact_typepk = models.IntegerField(primary_key=True, db_column='Contact_TypePK') # Field name made lowercase.
    contact_typedesc = models.CharField(max_length=150, db_column='Contact_TypeDesc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblcontacttype'
        app_label = ''

class Tblmatters(models.Model):
    matters_pk = models.IntegerField('self', primary_key=True, db_column='Matters_PK') # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    matters_clientid1 = models.IntegerField(null=True, db_column='Matters_ClientID1', blank=True) # Field name made lowercase.
    matters_clientid2 = models.IntegerField(null=True, db_column='Matters_ClientID2', blank=True) # Field name made lowercase.
    matters_primaryattorney = models.IntegerField(null=True, db_column='Matters_PrimaryAttorney', blank=True) # Field name made lowercase.
    matters_supportattorney1 = models.IntegerField(null=True, db_column='Matters_SupportAttorney1', blank=True) # Field name made lowercase.
    matters_supportattorney2 = models.IntegerField(null=True, db_column='Matters_SupportAttorney2', blank=True) # Field name made lowercase.
    matters_dateopened = models.DateField(null=True, db_column='Matters_DateOpened', blank=True) # Field name made lowercase.
    matters_dateclosed = models.DateField(null=True, db_column='Matters_DateClosed', blank=True) # Field name made lowercase.
    matters_caseclosed = models.DateField(null=True, db_column='Matters_CaseClosed', blank=True) # Field name made lowercase.
    matters_mattertype = models.IntegerField(null=True, db_column='Matters_MatterType', blank=True) # Field name made lowercase.
    matters_billingtype = models.IntegerField(null=True, db_column='Matters_BillingType', blank=True) # Field name made lowercase.
    matters_adverseparty1 = models.IntegerField(null=True, db_column='Matters_AdverseParty1', blank=True) # Field name made lowercase.
    matters_adverseparty2 = models.IntegerField(null=True, db_column='Matters_AdverseParty2', blank=True) # Field name made lowercase.
    matters_adverseparty3 = models.IntegerField(null=True, db_column='Matters_AdverseParty3', blank=True) # Field name made lowercase.
    matters_active = models.TextField(db_column='Matters_Active', blank=True) # Field name made lowercase. This field type is a guess.
    matters_intakememo = models.TextField(db_column='Matters_IntakeMemo', blank=True) # Field name made lowercase.
    matters_datecreated = models.DateTimeField(null=True, db_column='Matters_datecreated', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblmatters'
        app_label = ''

class Tblmattertasks(models.Model):
    mattertasks_pk = models.IntegerField(primary_key=True, db_column='MatterTasks_PK') # Field name made lowercase.
    mattertasks_matterpk = models.IntegerField(null=True, db_column='MatterTasks_MatterPK', blank=True) # Field name made lowercase.
    mattertasks_text = models.TextField(db_column='MatterTasks_Text', blank=True) # Field name made lowercase.
    mattertasks_subject = models.TextField(db_column='MatterTasks_Subject', blank=True) # Field name made lowercase.
    mattertasks_datecreated = models.DateField(null=True, db_column='MatterTasks_DateCreated', blank=True) # Field name made lowercase.
    mattertasks_duedate = models.DateField(null=True, db_column='MatterTasks_DueDate', blank=True) # Field name made lowercase.
    mattertasks_priority = models.IntegerField(null=True, db_column='MatterTasks_Priority', blank=True) # Field name made lowercase.
    mattertasks_staffcreatorpk = models.IntegerField(null=True, db_column='MatterTasks_StaffCreatorPK', blank=True) # Field name made lowercase.
    mattertasks_assignedstaff1pk = models.IntegerField(null=True, db_column='MatterTasks_AssignedStaff1PK', blank=True) # Field name made lowercase.
    mattertasks_assignedstaff2pk = models.IntegerField(null=True, db_column='MatterTasks_AssignedStaff2PK', blank=True) # Field name made lowercase.
    mattertasks_billabletimevalue = models.DecimalField(decimal_places=2, null=True, max_digits=5, db_column='MatterTasks_BillableTimeValue', blank=True) # Field name made lowercase.
    mattertasks_taskcomplete = models.TextField(db_column='MatterTasks_TaskComplete', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'tblmattertasks'
        app_label = ''

class Tblmattertype(models.Model):
    mattertype_pk = models.IntegerField(primary_key=True, db_column='MatterType_PK') # Field name made lowercase.
    mattertype_desc = models.CharField(max_length=150, db_column='MatterType_Desc', blank=True) # Field name made lowercase.
    mattertype_shortdesc = models.CharField(max_length=150, db_column='MatterType_ShortDesc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblmattertype'
        app_label = ''

class Tblpaymentmethods(models.Model):
    paymentmethods_pk = models.IntegerField(primary_key=True, db_column='PaymentMethods_PK') # Field name made lowercase.
    paymentmethods_desc = models.CharField(max_length=150, db_column='PaymentMethods_Desc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblpaymentmethods'
        app_label = ''

class Tblpayments(models.Model):
    payments_pk = models.IntegerField(primary_key=True, db_column='Payments_PK') # Field name made lowercase.
    payments_clientpk = models.IntegerField(null=True, db_column='Payments_ClientPK', blank=True) # Field name made lowercase.
    payments_staffpk = models.IntegerField(null=True, db_column='Payments_StaffPK', blank=True) # Field name made lowercase.
    payments_receiveddate = models.DateField(null=True, db_column='Payments_ReceivedDate', blank=True) # Field name made lowercase.
    payments_amount = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='Payments_Amount', blank=True) # Field name made lowercase.
    payments_methodpk = models.IntegerField(null=True, db_column='Payments_MethodPK', blank=True) # Field name made lowercase.
    payments_matterpk = models.IntegerField(null=True, db_column='Payments_MatterPK', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblpayments'
        app_label = ''

class ViewActivedr(models.Model):
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    matters_active = models.TextField(db_column='Matters_Active', blank=True) # Field name made lowercase. This field type is a guess.
    matters_mattertype = models.IntegerField(null=True, db_column='Matters_MatterType', blank=True) # Field name made lowercase.
    matters_pk = models.IntegerField(primary_key=True, db_column='Matters_PK') # Field name made lowercase.
    matters_clientid1 = models.IntegerField(null=True, db_column='Matters_ClientID1', blank=True) # Field name made lowercase.
    matters_clientid2 = models.IntegerField(null=True, db_column='Matters_ClientID2', blank=True) # Field name made lowercase.
    contact_pk = models.IntegerField(db_column='Contact_PK') # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_activedr'
        app_label = ''

class ViewActivebcy(models.Model):
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    matters_active = models.TextField(db_column='Matters_Active', blank=True) # Field name made lowercase. This field type is a guess.
    matters_mattertype = models.IntegerField(null=True, db_column='Matters_MatterType', blank=True) # Field name made lowercase.
    matters_pk = models.IntegerField(primary_key=True, db_column='Matters_PK') # Field name made lowercase.
    matters_clientid1 = models.IntegerField(null=True, db_column='Matters_ClientID1', blank=True) # Field name made lowercase.
    matters_clientid2 = models.IntegerField(null=True, db_column='Matters_ClientID2', blank=True) # Field name made lowercase.
    contact_pk = models.IntegerField(db_column='Contact_PK') # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_activebcy'
        app_label = ''

class ViewActivecontingency(models.Model):
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    matters_active = models.TextField(db_column='Matters_Active', blank=True) # Field name made lowercase. This field type is a guess.
    matters_mattertype = models.IntegerField(null=True, db_column='Matters_MatterType', blank=True) # Field name made lowercase.
    matters_pk = models.IntegerField(primary_key=True, db_column='Matters_PK') # Field name made lowercase.
    matters_clientid1 = models.IntegerField(null=True, db_column='Matters_ClientID1', blank=True) # Field name made lowercase.
    matters_clientid2 = models.IntegerField(null=True, db_column='Matters_ClientID2', blank=True) # Field name made lowercase.
    contact_pk = models.IntegerField(db_column='Contact_PK') # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_activecontingency'
        app_label = ''

class ViewActiveep(models.Model):
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    matters_active = models.TextField(db_column='Matters_Active', blank=True) # Field name made lowercase. This field type is a guess.
    matters_mattertype = models.IntegerField(null=True, db_column='Matters_MatterType', blank=True) # Field name made lowercase.
    matters_pk = models.IntegerField(primary_key=True, db_column='Matters_PK') # Field name made lowercase.
    matters_clientid1 = models.IntegerField(null=True, db_column='Matters_ClientID1', blank=True) # Field name made lowercase.
    matters_clientid2 = models.IntegerField(null=True, db_column='Matters_ClientID2', blank=True) # Field name made lowercase.
    contact_pk = models.IntegerField(db_column='Contact_PK') # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_activeep'
        app_label = ''

class ViewActiveprobate(models.Model):
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    matters_active = models.TextField(db_column='Matters_Active', blank=True) # Field name made lowercase. This field type is a guess.
    matters_mattertype = models.IntegerField(null=True, db_column='Matters_MatterType', blank=True) # Field name made lowercase.
    matters_pk = models.IntegerField(primary_key=True, db_column='Matters_PK') # Field name made lowercase.
    matters_clientid1 = models.IntegerField(null=True, db_column='Matters_ClientID1', blank=True) # Field name made lowercase.
    matters_clientid2 = models.IntegerField(null=True, db_column='Matters_ClientID2', blank=True) # Field name made lowercase.
    contact_pk = models.IntegerField(db_column='Contact_PK') # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_activeprobate'
        app_label = ''

class ViewActivetransactional(models.Model):
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    matters_active = models.TextField(db_column='Matters_Active', blank=True) # Field name made lowercase. This field type is a guess.
    matters_mattertype = models.IntegerField(null=True, db_column='Matters_MatterType', blank=True) # Field name made lowercase.
    matters_pk = models.IntegerField(primary_key=True, db_column='Matters_PK') # Field name made lowercase.
    matters_clientid1 = models.IntegerField(null=True, db_column='Matters_ClientID1', blank=True) # Field name made lowercase.
    matters_clientid2 = models.IntegerField(null=True, db_column='Matters_ClientID2', blank=True) # Field name made lowercase.
    contact_pk = models.IntegerField(db_column='Contact_PK') # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_activetransactional'
        app_label = ''

class ViewActivecivil(models.Model):
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    matters_active = models.TextField(db_column='Matters_Active', blank=True) # Field name made lowercase. This field type is a guess.
    matters_mattertype = models.IntegerField(null=True, db_column='Matters_MatterType', blank=True) # Field name made lowercase.
    matters_pk = models.IntegerField(primary_key=True, db_column='Matters_PK') # Field name made lowercase.
    matters_clientid1 = models.IntegerField(null=True, db_column='Matters_ClientID1', blank=True) # Field name made lowercase.
    matters_clientid2 = models.IntegerField(null=True, db_column='Matters_ClientID2', blank=True) # Field name made lowercase.
    contact_pk = models.IntegerField(db_column='Contact_PK') # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_activecivil'
        app_label = ''

