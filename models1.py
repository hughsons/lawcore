# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class CountActivebcy(models.Model):
    count = models.IntegerField(null=True, db_column='COUNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_activebcy'

class CountActivecivil(models.Model):
    count = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'count_activecivil'

class CountActivecontingency(models.Model):
    count = models.IntegerField(null=True, db_column='COUNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_activecontingency'

class CountActivedr(models.Model):
    count = models.IntegerField(null=True, db_column='COUNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_activedr'

class CountActiveep(models.Model):
    count = models.IntegerField(null=True, db_column='COUNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_activeep'

class CountActiveprobate(models.Model):
    count = models.IntegerField(null=True, db_column='COUNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_activeprobate'

class CountActivetransactional(models.Model):
    count = models.IntegerField(null=True, db_column='COUNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_activetransactional'

class CountApptsTodayBcy(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_appts_today_bcy'

class CountApptsTodayDom(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_appts_today_dom'

class CountApptsTodayDr(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_appts_today_dr'

class CountApptsTodayEp(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_appts_today_ep'

class CountApptsTodayPi(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_appts_today_pi'

class CountCallsToday(models.Model):
    todaycalls = models.IntegerField(null=True, db_column='TodayCalls', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_calls_today'

class CountCallsTodayBcy(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_calls_today_bcy'

class CountCallsTodayDom(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_calls_today_dom'

class CountCallsTodayDr(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_calls_today_dr'

class CountCallsTodayEp(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_calls_today_ep'

class CountCallsTodayPi(models.Model):
    currentappts = models.IntegerField(null=True, db_column='CurrentAppts', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_calls_today_pi'

class CountNewmattersbymonthBcy(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    bcymatters = models.IntegerField(null=True, db_column='BCYMatters', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_newmattersbymonth_bcy'

class CountNewmattersbymonthDr(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    drmatters = models.IntegerField(null=True, db_column='DRMatters', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_newmattersbymonth_dr'

class CountNewmattersbymonthEp(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    drmatters = models.IntegerField(null=True, db_column='DRMatters', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_newmattersbymonth_ep'

class CountNewmattersbymonthPi(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    bcymatters = models.IntegerField(null=True, db_column='BCYMatters', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_newmattersbymonth_pi'

class CountNewmattersbymonthProbate(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    probatematters = models.IntegerField(null=True, db_column='ProbateMatters', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'count_newmattersbymonth_probate'

class Countcalls12Monthstrailingdr(models.Model):
    callyear = models.IntegerField(null=True, db_column='CallYear', blank=True) # Field name made lowercase.
    callmonth = models.IntegerField(null=True, db_column='CallMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls12monthstrailingdr'

class Countcalls12Monthstrailingep(models.Model):
    callyear = models.IntegerField(null=True, db_column='CallYear', blank=True) # Field name made lowercase.
    callmonth = models.IntegerField(null=True, db_column='CallMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls12monthstrailingep'

class Countcalls12Monthstrailingnewcontacts(models.Model):
    callyear = models.IntegerField(null=True, db_column='CallYear', blank=True) # Field name made lowercase.
    callmonth = models.IntegerField(null=True, db_column='CallMonth', blank=True) # Field name made lowercase.
    callsource = models.CharField(max_length=150, db_column='CallSource', blank=True) # Field name made lowercase.
    calltype = models.CharField(max_length=150, db_column='CallType', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls12monthstrailingnewcontacts'

class Countcalls12Monthstrailingpi(models.Model):
    callyear = models.IntegerField(null=True, db_column='CallYear', blank=True) # Field name made lowercase.
    callmonth = models.IntegerField(null=True, db_column='CallMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls12monthstrailingpi'

class Countcalls12Monthstrailingprobate(models.Model):
    callyear = models.IntegerField(null=True, db_column='CallYear', blank=True) # Field name made lowercase.
    callmonth = models.IntegerField(null=True, db_column='CallMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls12monthstrailingprobate'

class Countcalls12Monthstrailybcy(models.Model):
    callyear = models.IntegerField(null=True, db_column='CallYear', blank=True) # Field name made lowercase.
    callmonth = models.IntegerField(null=True, db_column='CallMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls12monthstrailybcy'

class Countcalls30Daystrailingbcy(models.Model):
    calldate = models.IntegerField(null=True, db_column='CallDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls30daystrailingbcy'

class Countcalls30Daystrailingdr(models.Model):
    calldate = models.IntegerField(null=True, db_column='CallDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls30daystrailingdr'

class Countcalls30Daystrailingep(models.Model):
    calldate = models.IntegerField(null=True, db_column='CallDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls30daystrailingep'

class Countcalls30Daystrailingpi(models.Model):
    calldate = models.IntegerField(null=True, db_column='CallDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls30daystrailingpi'

class Countcalls30Daystrailingprobate(models.Model):
    calldate = models.IntegerField(null=True, db_column='CallDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countcalls30daystrailingprobate'

class Countnewmatters2Yearstrailingdr(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters2yearstrailingdr'

class Countnewmatters2Yearstrailingep(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters2yearstrailingep'

class Countnewmatters2Yearstrailingprobate(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters2yearstrailingprobate'

class Countnewmatters2Yrstrailingbcy(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters2yrstrailingbcy'

class Countnewmatters2Yrstrailingpi(models.Model):
    matteryear = models.IntegerField(null=True, db_column='MatterYear', blank=True) # Field name made lowercase.
    mattermonth = models.IntegerField(null=True, db_column='MatterMonth', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters2yrstrailingpi'

class Countnewmatters30Daystrailingbcy(models.Model):
    matterdate = models.IntegerField(null=True, db_column='MatterDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters30daystrailingbcy'

class Countnewmatters30Daystrailingdr(models.Model):
    matterdate = models.IntegerField(null=True, db_column='MatterDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters30daystrailingdr'

class Countnewmatters30Daystrailingep(models.Model):
    matterdate = models.IntegerField(null=True, db_column='MatterDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters30daystrailingep'

class Countnewmatters30Daystrailingpi(models.Model):
    matterdate = models.IntegerField(null=True, db_column='MatterDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters30daystrailingpi'

class Countnewmatters30Daystrailingprobate(models.Model):
    matterdate = models.IntegerField(null=True, db_column='MatterDate', blank=True) # Field name made lowercase.
    count = models.IntegerField(null=True, db_column='Count', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countnewmatters30daystrailingprobate'

class ReportNewmattersToday(models.Model):
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    contact_firstname = models.CharField(max_length=150, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=150, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    mattertype_desc = models.CharField(max_length=150, db_column='MatterType_Desc', blank=True) # Field name made lowercase.
    staff_stafffullname = models.CharField(max_length=150, db_column='Staff_StaffFullName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'report_newmatters_today'

class ReportPaymentsreceivedToday(models.Model):
    payments_amount = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='Payments_Amount', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=150, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    contact_firstname = models.CharField(max_length=150, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'report_paymentsreceived_today'

class SumPaymentsreceivedToday(models.Model):
    paymentsreceived = models.DecimalField(decimal_places=2, null=True, max_digits=40, db_column='PaymentsReceived', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'sum_paymentsreceived_today'

class Tblbillingtype(models.Model):
    billingtype_pk = models.IntegerField(unique=True, db_column='BillingType_PK') # Field name made lowercase.
    billingtype_desc = models.CharField(max_length=150, db_column='BillingType_Desc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblbillingtype'

class Tblcallaction(models.Model):
    callaction_pk = models.IntegerField(unique=True, db_column='CallAction_PK') # Field name made lowercase.
    callaction_description = models.CharField(max_length=150, db_column='CallAction_Description', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblcallaction'

class Tblcalls(models.Model):
    calls_pk = models.IntegerField(unique=True, db_column='Calls_PK') # Field name made lowercase.
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
    class Meta:
        db_table = u'tblcalls'

class Tblcallsource(models.Model):
    callsource_pk = models.IntegerField(unique=True, db_column='CallSource_PK') # Field name made lowercase.
    callsource_description = models.CharField(max_length=150, db_column='CallSource_Description', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblcallsource'

class Tblcalltype(models.Model):
    calltype_pk = models.IntegerField(unique=True, db_column='CallType_PK') # Field name made lowercase.
    calltype_description = models.CharField(max_length=150, db_column='CallType_Description', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblcalltype'

class Tblcasecontacts(models.Model):
    casecontacts_pk = models.IntegerField(unique=True, db_column='CaseContacts_PK') # Field name made lowercase.
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

class Tblcasenotes(models.Model):
    casenotes_pk = models.IntegerField(unique=True, db_column='CaseNotes_PK') # Field name made lowercase.
    casenotes_matterpk = models.IntegerField(null=True, db_column='CaseNotes_MatterPK', blank=True) # Field name made lowercase.
    casenotes_notedate = models.DateField(null=True, db_column='CaseNotes_NoteDate', blank=True) # Field name made lowercase.
    casenotes_notetext = models.TextField(db_column='CaseNotes_NoteText', blank=True) # Field name made lowercase.
    casenotes_notesubject = models.TextField(db_column='CaseNotes_NoteSubject', blank=True) # Field name made lowercase.
    casenotes_staffpk = models.IntegerField(null=True, db_column='CaseNotes_StaffPK', blank=True) # Field name made lowercase.
    casenotes_billabletime = models.DecimalField(decimal_places=2, null=True, max_digits=6, db_column='CaseNotes_BillableTime', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblcasenotes'

class TblchecklistDomcontested(models.Model):
    domcontchk_pk = models.IntegerField(unique=True, db_column='DOMContChk_PK') # Field name made lowercase.
    domcontchk_initialconsultation = models.DateField(null=True, db_column='DOMContChk_InitialConsultation', blank=True) # Field name made lowercase.
    domcontchk_dateclientretained = models.DateField(null=True, db_column='DOMContChk_DateClientRetained', blank=True) # Field name made lowercase.
    domcontchk_casefiledyesno = models.CharField(max_length=45, db_column='DOMContChk_CaseFiledYESNO', blank=True) # Field name made lowercase.
    domcontchk_initialmemotofile = models.DateField(null=True, db_column='DOMContChk_InitialMemotoFile', blank=True) # Field name made lowercase.
    domcontchk_matterpk = models.IntegerField(null=True, db_column='DOMContChk_MatterPK', blank=True) # Field name made lowercase.
    domcontchk_memooflaw = models.DateField(null=True, db_column='DOMContChk_MemoofLaw', blank=True) # Field name made lowercase.
    domcontchk_intakesheet = models.CharField(max_length=45, db_column='DOMContChk_IntakeSheet', blank=True) # Field name made lowercase.
    domcontchk_vitalstatistics = models.CharField(max_length=45, db_column='DOMContChk_VitalStatistics', blank=True) # Field name made lowercase.
    domcontchk_summons = models.CharField(max_length=45, db_column='DOMContChk_Summons', blank=True) # Field name made lowercase.
    domcontchk_petitionanswer = models.CharField(max_length=45, db_column='DOMContChk_PetitionAnswer', blank=True) # Field name made lowercase.
    domcontchk_uccjea = models.CharField(max_length=45, db_column='DOMContChk_UCCJEA', blank=True) # Field name made lowercase.
    domcontchk_noticessn = models.CharField(max_length=45, db_column='DOMContChk_NoticeSSN', blank=True) # Field name made lowercase.
    domcontchk_affmilitaryservice = models.CharField(max_length=45, db_column='DOMContChk_AffMilitaryService', blank=True) # Field name made lowercase.
    domcontchk_noticeresidency = models.CharField(max_length=45, db_column='DOMContChk_NoticeResidency', blank=True) # Field name made lowercase.
    domcontchk_financialaffidavit = models.CharField(max_length=45, db_column='DOMContChk_FinancialAffidavit', blank=True) # Field name made lowercase.
    domcontchk_filingfee = models.CharField(max_length=45, db_column='DOMContChk_FilingFee', blank=True) # Field name made lowercase.
    domcontchk_datepleadingsfiled = models.DateField(null=True, db_column='DOMContChk_DatePleadingsFiled', blank=True) # Field name made lowercase.
    domcontchk_motiontempsupport = models.DateField(null=True, db_column='DOMContChk_MotionTempSupport', blank=True) # Field name made lowercase.
    domcontchk_receivedmandisclosureclient = models.DateField(null=True, db_column='DOMContChk_ReceivedManDisclosureClient', blank=True) # Field name made lowercase.
    domcontchk_mandisclosuretooc = models.DateField(null=True, db_column='DOMContChk_ManDisclosuretoOC', blank=True) # Field name made lowercase.
    domcontchk_interrogstooc = models.CharField(max_length=45, db_column='DOMContChk_InterrogstoOC', blank=True) # Field name made lowercase.
    domcontchk_requestforadmissiontooc = models.CharField(max_length=45, db_column='DOMContChk_RequestforAdmissiontoOC', blank=True) # Field name made lowercase.
    domcontchk_preliminaryreqprod = models.CharField(max_length=45, db_column='DOMContChk_PreliminaryReqProd', blank=True) # Field name made lowercase.
    domcontchk_mediationdate = models.DateField(null=True, db_column='DOMContChk_MediationDate', blank=True) # Field name made lowercase.
    domcontchk_pretrialmemolaw = models.DateField(null=True, db_column='DOMContChk_PreTrialMemoLaw', blank=True) # Field name made lowercase.
    domcontchk_depooppparty = models.DateField(null=True, db_column='DOMContChk_DepoOppParty', blank=True) # Field name made lowercase.
    domcontchk_depokeywitnesses = models.DateField(null=True, db_column='DOMContChk_DepoKeyWitnesses', blank=True) # Field name made lowercase.
    domcontchk_requestforproduction = models.DateField(null=True, db_column='DOMContChk_RequestforProduction', blank=True) # Field name made lowercase.
    domcontchk_trialbindercomplete = models.DateField(null=True, db_column='DOMContChk_TrialBinderComplete', blank=True) # Field name made lowercase.
    domcontchk_resolvedoutstandingdiscovery = models.DateField(null=True, db_column='DOMContChk_ResolvedOutstandingDiscovery', blank=True) # Field name made lowercase.
    domcontchk_trialwitnesssubpoena = models.DateField(null=True, db_column='DOMContChk_TrialWitnessSubpoena', blank=True) # Field name made lowercase.
    domcontchk_expertwitnesssubpoena = models.DateField(null=True, db_column='DOMContChk_ExpertWitnessSubpoena', blank=True) # Field name made lowercase.
    domcontchk_courtroomvisualaids = models.DateField(null=True, db_column='DOMContChk_CourtroomVisualAids', blank=True) # Field name made lowercase.
    domcontchk_trialdate = models.DateField(null=True, db_column='DOMContChk_TrialDate', blank=True) # Field name made lowercase.
    domcontchk_judgmentdate = models.DateField(null=True, db_column='DOMContChk_JudgmentDate', blank=True) # Field name made lowercase.
    domcontchk_mediationscheduled = models.DateField(null=True, db_column='DOMContChk_MediationScheduled', blank=True) # Field name made lowercase.
    domcontchk_civilcoversheet = models.CharField(max_length=45, db_column='DOMContChk_CivilCoverSheet', blank=True) # Field name made lowercase.
    domcontchk_stageonecomp = models.TextField(db_column='DOMContChk_StageOneComp', blank=True) # Field name made lowercase. This field type is a guess.
    domcontchk_stagetwocomp = models.TextField(db_column='DOMContChk_StageTwoComp', blank=True) # Field name made lowercase. This field type is a guess.
    domcontchk_stagethreecomp = models.TextField(db_column='DOMContChk_StageThreeComp', blank=True) # Field name made lowercase. This field type is a guess.
    domcontchk_stagefourcomp = models.TextField(db_column='DOMContChk_StageFourComp', blank=True) # Field name made lowercase. This field type is a guess.
    domcontchk_noticefortrial = models.DateField(null=True, db_column='DOMContChk_NoticeForTrial', blank=True) # Field name made lowercase.
    domcontchk_trialdatescheduled = models.DateField(null=True, db_column='DOMContChk_TrialDateScheduled', blank=True) # Field name made lowercase.
    domcontchk_childsupportguidelines = models.CharField(max_length=45, db_column='DOMContChk_ChildSupportGuidelines', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblchecklist_domcontested'

class TblchecklistPi(models.Model):
    pichk_pk = models.IntegerField(unique=True, db_column='PIChk_PK') # Field name made lowercase.
    pichk_matterpk = models.IntegerField(null=True, db_column='PIChk_MatterPK', blank=True) # Field name made lowercase.
    pichk_initialstage = models.TextField(db_column='PIChk_InitialStage', blank=True) # Field name made lowercase. This field type is a guess.
    pichk_predemandstage = models.TextField(db_column='PIChk_PreDemandStage', blank=True) # Field name made lowercase. This field type is a guess.
    pichk_demandstage = models.TextField(db_column='PIChk_DemandStage', blank=True) # Field name made lowercase. This field type is a guess.
    pichk_litigation = models.TextField(db_column='PIChk_Litigation', blank=True) # Field name made lowercase. This field type is a guess.
    pichk_initialdemand = models.IntegerField(null=True, db_column='PIChk_InitialDemand', blank=True) # Field name made lowercase.
    pichk_currentdemand = models.IntegerField(null=True, db_column='PIChk_CurrentDemand', blank=True) # Field name made lowercase.
    pichk_initialconsultation = models.DateField(null=True, db_column='PIChk_InitialConsultation', blank=True) # Field name made lowercase.
    pichk_engagementdocuments = models.DateField(null=True, db_column='PIChk_EngagementDocuments', blank=True) # Field name made lowercase.
    pichk_accidentreportreceived = models.DateField(null=True, db_column='PIChk_AccidentReportReceived', blank=True) # Field name made lowercase.
    pichk_lorclientins = models.DateField(null=True, db_column='PIChk_LORClientIns', blank=True) # Field name made lowercase.
    pichk_loratfaultins = models.DateField(null=True, db_column='PIChk_LORAtFaultIns', blank=True) # Field name made lowercase.
    pichk_lorhospital = models.DateField(null=True, db_column='PIChk_LORHospital', blank=True) # Field name made lowercase.
    pichk_lorems = models.DateField(null=True, db_column='PIChk_LOREMS', blank=True) # Field name made lowercase.
    pichk_lorphysicianprimary = models.DateField(null=True, db_column='PIChk_LORPhysicianPrimary', blank=True) # Field name made lowercase.
    pichk_lorphysicianalt2 = models.DateField(null=True, db_column='PIChk_LORPhysicianAlt2', blank=True) # Field name made lowercase.
    pichk_lorphysicianalt3 = models.DateField(null=True, db_column='PIChk_LORPhysicianAlt3', blank=True) # Field name made lowercase.
    pichk_clientinsdec = models.DateField(null=True, db_column='PIChk_ClientInsDec', blank=True) # Field name made lowercase.
    pichk_atfaultinsdec = models.DateField(null=True, db_column='PIChk_AtFaultInsDec', blank=True) # Field name made lowercase.
    pichk_mmi = models.DateField(null=True, db_column='PIChk_MMI', blank=True) # Field name made lowercase.
    pichk_mmipercentage = models.CharField(max_length=360, db_column='PIChk_MMIPercentage', blank=True) # Field name made lowercase.
    pichk_demandatfault = models.TextField(db_column='PIChk_DemandAtFault', blank=True) # Field name made lowercase. This field type is a guess.
    pichk_demandatfaultcounteroffer = models.TextField(db_column='PIChk_DemandAtFaultCounterOffer', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'tblchecklist_pi'

class TblchecklistProbate(models.Model):
    probatechk_pk = models.IntegerField(unique=True, db_column='ProbateChk_PK') # Field name made lowercase.
    probatechk_matterpk = models.IntegerField(null=True, db_column='ProbateChk_MatterPK', blank=True) # Field name made lowercase.
    probatechk_initialstage = models.TextField(db_column='ProbateChk_InitialStage', blank=True) # Field name made lowercase. This field type is a guess.
    probatechk_filingstage = models.TextField(db_column='ProbateChk_FilingStage', blank=True) # Field name made lowercase. This field type is a guess.
    probatechk_postletters = models.TextField(db_column='ProbateChk_PostLetters', blank=True) # Field name made lowercase. This field type is a guess.
    probatechk_inventory = models.TextField(db_column='ProbateChk_Inventory', blank=True) # Field name made lowercase. This field type is a guess.
    probatechk_postdistribution = models.TextField(db_column='ProbateChk_PostDistribution', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'tblchecklist_probate'

class Tblcontact(models.Model):
    contact_pk = models.IntegerField(unique=True, db_column='Contact_PK') # Field name made lowercase.
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
    class Meta:
        db_table = u'tblcontact'

class Tblcontacttype(models.Model):
    contact_typepk = models.IntegerField(unique=True, db_column='Contact_TypePK') # Field name made lowercase.
    contact_typedesc = models.CharField(max_length=150, db_column='Contact_TypeDesc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblcontacttype'

class Tblmatters(models.Model):
    matters_pk = models.ForeignKey('self', unique=True, db_column='Matters_PK') # Field name made lowercase.
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
    class Meta:
        db_table = u'tblmatters'

class Tblmattertasks(models.Model):
    mattertasks_pk = models.IntegerField(unique=True, db_column='MatterTasks_PK') # Field name made lowercase.
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

class Tblmattertype(models.Model):
    mattertype_pk = models.IntegerField(unique=True, db_column='MatterType_PK') # Field name made lowercase.
    mattertype_desc = models.CharField(max_length=150, db_column='MatterType_Desc', blank=True) # Field name made lowercase.
    mattertype_shortdesc = models.CharField(max_length=150, db_column='MatterType_ShortDesc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblmattertype'

class Tblpaymentmethods(models.Model):
    paymentmethods_pk = models.IntegerField(unique=True, db_column='PaymentMethods_PK') # Field name made lowercase.
    paymentmethods_desc = models.CharField(max_length=150, db_column='PaymentMethods_Desc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblpaymentmethods'

class Tblpayments(models.Model):
    payments_pk = models.IntegerField(unique=True, db_column='Payments_PK') # Field name made lowercase.
    payments_clientpk = models.IntegerField(null=True, db_column='Payments_ClientPK', blank=True) # Field name made lowercase.
    payments_staffpk = models.IntegerField(null=True, db_column='Payments_StaffPK', blank=True) # Field name made lowercase.
    payments_receiveddate = models.DateField(null=True, db_column='Payments_ReceivedDate', blank=True) # Field name made lowercase.
    payments_amount = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='Payments_Amount', blank=True) # Field name made lowercase.
    payments_methodpk = models.IntegerField(null=True, db_column='Payments_MethodPK', blank=True) # Field name made lowercase.
    payments_matterpk = models.IntegerField(null=True, db_column='Payments_MatterPK', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblpayments'

class Tblpiclaims(models.Model):
    piclaim_pk = models.IntegerField(unique=True, db_column='PIClaim_PK') # Field name made lowercase.
    piclaim_matterpk = models.IntegerField(null=True, db_column='PIClaim_MatterPK', blank=True) # Field name made lowercase.
    piclaim_claimamount = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='PIClaim_ClaimAmount', blank=True) # Field name made lowercase.
    piclaim_claimdesc = models.TextField(db_column='PIClaim_ClaimDesc', blank=True) # Field name made lowercase.
    piclaim_provider = models.CharField(max_length=360, db_column='PIClaim_Provider', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblpiclaims'

class Tblpidemand(models.Model):
    pidemand_pk = models.IntegerField(unique=True, db_column='PIDemand_PK') # Field name made lowercase.
    pidemand_date = models.DateField(null=True, db_column='PIDemand_Date', blank=True) # Field name made lowercase.
    pidemand_amount = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='PIDemand_Amount', blank=True) # Field name made lowercase.
    pidemand_status = models.CharField(max_length=150, db_column='PIDemand_Status', blank=True) # Field name made lowercase.
    pidemand_staff = models.IntegerField(null=True, db_column='PIDemand_Staff', blank=True) # Field name made lowercase.
    pidemand_matterpk = models.IntegerField(db_column='PIDemand_MatterPK') # Field name made lowercase.
    class Meta:
        db_table = u'tblpidemand'

class Tblpilop(models.Model):
    pilop_pk = models.IntegerField(unique=True, db_column='PILOP_PK') # Field name made lowercase.
    pilop_date = models.DateField(null=True, db_column='PILOP_Date', blank=True) # Field name made lowercase.
    pilop_provider = models.CharField(max_length=360, db_column='PILOP_Provider', blank=True) # Field name made lowercase.
    pilop_matterpk = models.IntegerField(null=True, db_column='PILOP_MatterPK', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblpilop'

class Tblpimatters(models.Model):
    pimatters_pk = models.IntegerField(unique=True, db_column='PIMatters_PK') # Field name made lowercase.
    pimatters_matterpk = models.IntegerField(null=True, db_column='PIMatters_MatterPK', blank=True) # Field name made lowercase.
    pimatters_clientins1 = models.IntegerField(null=True, db_column='PIMatters_ClientIns1', blank=True) # Field name made lowercase.
    pimatters_clientins2 = models.IntegerField(null=True, db_column='PIMatters_ClientIns2', blank=True) # Field name made lowercase.
    pimatters_clientins3 = models.IntegerField(null=True, db_column='PIMatters_ClientIns3', blank=True) # Field name made lowercase.
    pimatters_def1 = models.IntegerField(null=True, db_column='PIMatters_Def1', blank=True) # Field name made lowercase.
    pimatters_def2 = models.IntegerField(null=True, db_column='PIMatters_Def2', blank=True) # Field name made lowercase.
    pimatters_def3 = models.IntegerField(null=True, db_column='PIMatters_Def3', blank=True) # Field name made lowercase.
    pimatters_defins1 = models.IntegerField(null=True, db_column='PIMatters_DefIns1', blank=True) # Field name made lowercase.
    pimatters_defins2 = models.IntegerField(null=True, db_column='PIMatters_DefIns2', blank=True) # Field name made lowercase.
    pimatters_defins3 = models.IntegerField(null=True, db_column='PIMatters_DefIns3', blank=True) # Field name made lowercase.
    pimatters_claimnumber_clientins = models.CharField(max_length=300, db_column='PIMatters_ClaimNumber_ClientIns', blank=True) # Field name made lowercase.
    pimatters_claimnumber_defins = models.CharField(max_length=300, db_column='PIMatters_ClaimNumber_DefIns', blank=True) # Field name made lowercase.
    pimatters_stage = models.IntegerField(null=True, db_column='PIMatters_Stage', blank=True) # Field name made lowercase.
    pimatters_clientins1_bi = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='PIMatters_ClientIns1_BI', blank=True) # Field name made lowercase.
    pimatters_clientins2_bi = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='PIMatters_ClientIns2_BI', blank=True) # Field name made lowercase.
    pimatters_clientins3_bi = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='PIMatters_ClientIns3_BI', blank=True) # Field name made lowercase.
    pimatters_clientins1_um = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='PIMatters_ClientIns1_UM', blank=True) # Field name made lowercase.
    pimatters_clientins2_um = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='PIMatters_ClientIns2_UM', blank=True) # Field name made lowercase.
    pimatters_clientins3_um = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='PIMatters_ClientIns3_UM', blank=True) # Field name made lowercase.
    pimatters_defins1_bi = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='PIMatters_DefIns1_BI', blank=True) # Field name made lowercase.
    pimatters_defins2_bi = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='PIMatters_DefIns2_BI', blank=True) # Field name made lowercase.
    pimatters_defins3_bi = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='PIMatters_DefIns3_BI', blank=True) # Field name made lowercase.
    pimatters_doa = models.DateField(null=True, db_column='PIMatters_DOA', blank=True) # Field name made lowercase.
    pimatters_sol = models.DateField(null=True, db_column='PIMatters_SOL', blank=True) # Field name made lowercase.
    pimatters_casevalue = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='PIMatters_CaseValue', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblpimatters'

class Tblpimatterstage(models.Model):
    pimatterstage_pk = models.IntegerField(unique=True, db_column='PIMatterStage_PK') # Field name made lowercase.
    pimatterstage_desc = models.CharField(max_length=150, db_column='PIMatterStage_Desc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblpimatterstage'

class Tblpimedical(models.Model):
    pimedical_pk = models.IntegerField(unique=True, db_column='PIMedical_PK') # Field name made lowercase.
    pimedical_matterpk = models.IntegerField(null=True, db_column='PIMedical_MatterPK', blank=True) # Field name made lowercase.
    pimedical_amount = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='PIMedical_Amount', blank=True) # Field name made lowercase.
    pimedical_desc = models.TextField(db_column='PIMedical_Desc', blank=True) # Field name made lowercase.
    pimedical_provider = models.CharField(max_length=360, db_column='PIMedical_Provider', blank=True) # Field name made lowercase.
    pimedical_servicedate = models.DateField(null=True, db_column='PIMedical_ServiceDate', blank=True) # Field name made lowercase.
    pimedical_type = models.CharField(max_length=150, db_column='PIMedical_Type', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblpimedical'

class Tblpolicyinfo(models.Model):
    policyinfo_pk = models.IntegerField(unique=True, db_column='PolicyInfo_PK') # Field name made lowercase.
    policyinfo_insco = models.CharField(max_length=360, db_column='PolicyInfo_InsCo', blank=True) # Field name made lowercase.
    policyinfo_bi = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='PolicyInfo_BI', blank=True) # Field name made lowercase.
    policyinfo_pi = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='PolicyInfo_PI', blank=True) # Field name made lowercase.
    policyinfo_um = models.DecimalField(decimal_places=2, null=True, max_digits=12, db_column='PolicyInfo_UM', blank=True) # Field name made lowercase.
    policyinfo_insured = models.CharField(max_length=150, db_column='PolicyInfo_Insured', blank=True) # Field name made lowercase.
    policyinfo_matterpk = models.IntegerField(null=True, db_column='PolicyInfo_MatterPK', blank=True) # Field name made lowercase.
    policyinfo_adjuster = models.CharField(max_length=360, db_column='PolicyInfo_Adjuster', blank=True) # Field name made lowercase.
    policyinfo_number = models.CharField(max_length=360, db_column='PolicyInfo_Number', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblpolicyinfo'

class Tblstaff(models.Model):
    staff_pk = models.IntegerField(unique=True, db_column='Staff_PK') # Field name made lowercase.
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

class Tblstate(models.Model):
    state_pk = models.CharField(max_length=9, unique=True, db_column='State_PK') # Field name made lowercase.
    state_name = models.CharField(max_length=150, db_column='State_Name', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblstate'

class ViewActivebcy(models.Model):
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    matters_active = models.TextField(db_column='Matters_Active', blank=True) # Field name made lowercase. This field type is a guess.
    matters_mattertype = models.IntegerField(null=True, db_column='Matters_MatterType', blank=True) # Field name made lowercase.
    matters_pk = models.IntegerField(db_column='Matters_PK') # Field name made lowercase.
    matters_clientid1 = models.IntegerField(null=True, db_column='Matters_ClientID1', blank=True) # Field name made lowercase.
    matters_clientid2 = models.IntegerField(null=True, db_column='Matters_ClientID2', blank=True) # Field name made lowercase.
    contact_pk = models.IntegerField(db_column='Contact_PK') # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_activebcy'

class ViewActivecivil(models.Model):
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    matters_active = models.TextField(db_column='Matters_Active', blank=True) # Field name made lowercase. This field type is a guess.
    matters_mattertype = models.IntegerField(null=True, db_column='Matters_MatterType', blank=True) # Field name made lowercase.
    matters_pk = models.IntegerField(db_column='Matters_PK') # Field name made lowercase.
    matters_clientid1 = models.IntegerField(null=True, db_column='Matters_ClientID1', blank=True) # Field name made lowercase.
    matters_clientid2 = models.IntegerField(null=True, db_column='Matters_ClientID2', blank=True) # Field name made lowercase.
    contact_pk = models.IntegerField(db_column='Contact_PK') # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_activecivil'

class ViewActivecontingency(models.Model):
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    matters_active = models.TextField(db_column='Matters_Active', blank=True) # Field name made lowercase. This field type is a guess.
    matters_mattertype = models.IntegerField(null=True, db_column='Matters_MatterType', blank=True) # Field name made lowercase.
    matters_pk = models.IntegerField(db_column='Matters_PK') # Field name made lowercase.
    matters_clientid1 = models.IntegerField(null=True, db_column='Matters_ClientID1', blank=True) # Field name made lowercase.
    matters_clientid2 = models.IntegerField(null=True, db_column='Matters_ClientID2', blank=True) # Field name made lowercase.
    contact_pk = models.IntegerField(db_column='Contact_PK') # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_activecontingency'

class ViewActivedr(models.Model):
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    matters_active = models.TextField(db_column='Matters_Active', blank=True) # Field name made lowercase. This field type is a guess.
    matters_mattertype = models.IntegerField(null=True, db_column='Matters_MatterType', blank=True) # Field name made lowercase.
    matters_pk = models.IntegerField(db_column='Matters_PK') # Field name made lowercase.
    matters_clientid1 = models.IntegerField(null=True, db_column='Matters_ClientID1', blank=True) # Field name made lowercase.
    matters_clientid2 = models.IntegerField(null=True, db_column='Matters_ClientID2', blank=True) # Field name made lowercase.
    contact_pk = models.IntegerField(db_column='Contact_PK') # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_activedr'

class ViewActiveep(models.Model):
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    matters_active = models.TextField(db_column='Matters_Active', blank=True) # Field name made lowercase. This field type is a guess.
    matters_mattertype = models.IntegerField(null=True, db_column='Matters_MatterType', blank=True) # Field name made lowercase.
    matters_pk = models.IntegerField(db_column='Matters_PK') # Field name made lowercase.
    matters_clientid1 = models.IntegerField(null=True, db_column='Matters_ClientID1', blank=True) # Field name made lowercase.
    matters_clientid2 = models.IntegerField(null=True, db_column='Matters_ClientID2', blank=True) # Field name made lowercase.
    contact_pk = models.IntegerField(db_column='Contact_PK') # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_activeep'

class ViewActiveprobate(models.Model):
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    matters_active = models.TextField(db_column='Matters_Active', blank=True) # Field name made lowercase. This field type is a guess.
    matters_mattertype = models.IntegerField(null=True, db_column='Matters_MatterType', blank=True) # Field name made lowercase.
    matters_pk = models.IntegerField(db_column='Matters_PK') # Field name made lowercase.
    matters_clientid1 = models.IntegerField(null=True, db_column='Matters_ClientID1', blank=True) # Field name made lowercase.
    matters_clientid2 = models.IntegerField(null=True, db_column='Matters_ClientID2', blank=True) # Field name made lowercase.
    contact_pk = models.IntegerField(db_column='Contact_PK') # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_activeprobate'

class ViewActivetransactional(models.Model):
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    matters_active = models.TextField(db_column='Matters_Active', blank=True) # Field name made lowercase. This field type is a guess.
    matters_mattertype = models.IntegerField(null=True, db_column='Matters_MatterType', blank=True) # Field name made lowercase.
    matters_pk = models.IntegerField(db_column='Matters_PK') # Field name made lowercase.
    matters_clientid1 = models.IntegerField(null=True, db_column='Matters_ClientID1', blank=True) # Field name made lowercase.
    matters_clientid2 = models.IntegerField(null=True, db_column='Matters_ClientID2', blank=True) # Field name made lowercase.
    contact_pk = models.IntegerField(db_column='Contact_PK') # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_activetransactional'

class ViewAdjusters(models.Model):
    contact_pk = models.IntegerField(unique=True, db_column='Contact_PK') # Field name made lowercase.
    contact_middlename = models.CharField(max_length=360, db_column='Contact_MiddleName', blank=True) # Field name made lowercase.
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    contact_company = models.CharField(max_length=360, db_column='Contact_Company', blank=True) # Field name made lowercase.
    contact_address1 = models.CharField(max_length=360, db_column='Contact_Address1', blank=True) # Field name made lowercase.
    contact_address2 = models.CharField(max_length=360, db_column='Contact_Address2', blank=True) # Field name made lowercase.
    contact_city = models.CharField(max_length=360, db_column='Contact_City', blank=True) # Field name made lowercase.
    contact_state = models.CharField(max_length=360, db_column='Contact_State', blank=True) # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    contact_zip = models.CharField(max_length=30, db_column='Contact_ZIP', blank=True) # Field name made lowercase.
    contact_telephone2 = models.CharField(max_length=135, db_column='Contact_Telephone2', blank=True) # Field name made lowercase.
    contact_fax = models.CharField(max_length=135, db_column='Contact_Fax', blank=True) # Field name made lowercase.
    contact_email = models.CharField(max_length=360, db_column='Contact_Email', blank=True) # Field name made lowercase.
    contact_alternatecontact = models.CharField(max_length=135, db_column='Contact_AlternateContact', blank=True) # Field name made lowercase.
    contact_type = models.IntegerField(null=True, db_column='Contact_Type', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_adjusters'

class ViewCallsbysourcealltimeDirectory(models.Model):
    callyear = models.IntegerField(null=True, db_column='CallYear', blank=True) # Field name made lowercase.
    callmonth = models.IntegerField(null=True, db_column='CallMonth', blank=True) # Field name made lowercase.
    directorycalls = models.IntegerField(null=True, db_column='DirectoryCalls', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_callsbysourcealltime_directory'

class ViewCallsourcealltimeBillboard(models.Model):
    callyear = models.IntegerField(null=True, db_column='CallYear', blank=True) # Field name made lowercase.
    callmonth = models.IntegerField(null=True, db_column='CallMonth', blank=True) # Field name made lowercase.
    calltype = models.CharField(max_length=150, db_column='CallType', blank=True) # Field name made lowercase.
    tvcalls = models.IntegerField(null=True, db_column='TVCalls', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_callsourcealltime_billboard'

class ViewCallsourcealltimeInternet(models.Model):
    callyear = models.IntegerField(null=True, db_column='CallYear', blank=True) # Field name made lowercase.
    callmonth = models.IntegerField(null=True, db_column='CallMonth', blank=True) # Field name made lowercase.
    internetcalls = models.IntegerField(null=True, db_column='InternetCalls', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_callsourcealltime_internet'

class ViewCallsourcealltimeNewspaper(models.Model):
    callyear = models.IntegerField(null=True, db_column='CallYear', blank=True) # Field name made lowercase.
    callmonth = models.IntegerField(null=True, db_column='CallMonth', blank=True) # Field name made lowercase.
    newspapercalls = models.IntegerField(null=True, db_column='NewspaperCalls', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_callsourcealltime_newspaper'

class ViewCallsourcealltimeTv(models.Model):
    callyear = models.IntegerField(null=True, db_column='CallYear', blank=True) # Field name made lowercase.
    callmonth = models.IntegerField(null=True, db_column='CallMonth', blank=True) # Field name made lowercase.
    calltype = models.CharField(max_length=150, db_column='CallType', blank=True) # Field name made lowercase.
    tvcalls = models.IntegerField(null=True, db_column='TVCalls', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_callsourcealltime_tv'

class ViewCallstatistics(models.Model):
    call_year = models.IntegerField(null=True, db_column='Call Year', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    call_month = models.IntegerField(null=True, db_column='Call Month', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    call_type = models.CharField(max_length=150, db_column='Call Type', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    primary_call_source = models.CharField(max_length=150, db_column='Primary Call Source', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    call_count = models.IntegerField(null=True, db_column='Call Count', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    callsource_description = models.CharField(max_length=150, db_column='CallSource_Description', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_callstatistics'

class ViewCasenotes(models.Model):
    casenotes_notedate = models.DateField(null=True, db_column='CaseNotes_NoteDate', blank=True) # Field name made lowercase.
    casenotes_notetext = models.TextField(db_column='CaseNotes_NoteText', blank=True) # Field name made lowercase.
    casenotes_notesubject = models.TextField(db_column='CaseNotes_NoteSubject', blank=True) # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    staff_stafffullname = models.CharField(max_length=150, db_column='Staff_StaffFullName', blank=True) # Field name made lowercase.
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    contact_company = models.CharField(max_length=360, db_column='Contact_Company', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_casenotes'

class ViewCasenotesCount(models.Model):
    staff_stafffullname = models.CharField(max_length=150, db_column='Staff_StaffFullName', blank=True) # Field name made lowercase.
    case_note_count = models.IntegerField(null=True, db_column='Case Note Count', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    casenotes_notedate = models.DateField(null=True, db_column='CaseNotes_NoteDate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_casenotes_count'

class ViewCasenotesCountToday(models.Model):
    staff_stafffullname = models.CharField(max_length=150, db_column='Staff_StaffFullName', blank=True) # Field name made lowercase.
    case_note_count = models.IntegerField(null=True, db_column='Case Note Count', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    class Meta:
        db_table = u'view_casenotes_count_today'

class ViewCasenotesToday(models.Model):
    casenotes_notedate = models.DateField(null=True, db_column='CaseNotes_NoteDate', blank=True) # Field name made lowercase.
    casenotes_notetext = models.TextField(db_column='CaseNotes_NoteText', blank=True) # Field name made lowercase.
    casenotes_notesubject = models.TextField(db_column='CaseNotes_NoteSubject', blank=True) # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    staff_stafffullname = models.CharField(max_length=150, db_column='Staff_StaffFullName', blank=True) # Field name made lowercase.
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    contact_company = models.CharField(max_length=360, db_column='Contact_Company', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_casenotes_today'

class ViewClientcontacts(models.Model):
    contact_pk = models.IntegerField(unique=True, db_column='Contact_PK') # Field name made lowercase.
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_middlename = models.CharField(max_length=360, db_column='Contact_MiddleName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    contact_company = models.CharField(max_length=360, db_column='Contact_Company', blank=True) # Field name made lowercase.
    contact_address1 = models.CharField(max_length=360, db_column='Contact_Address1', blank=True) # Field name made lowercase.
    contact_address2 = models.CharField(max_length=360, db_column='Contact_Address2', blank=True) # Field name made lowercase.
    contact_city = models.CharField(max_length=360, db_column='Contact_City', blank=True) # Field name made lowercase.
    contact_zip = models.CharField(max_length=30, db_column='Contact_ZIP', blank=True) # Field name made lowercase.
    contact_state = models.CharField(max_length=360, db_column='Contact_State', blank=True) # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    contact_telephone2 = models.CharField(max_length=135, db_column='Contact_Telephone2', blank=True) # Field name made lowercase.
    contact_fax = models.CharField(max_length=135, db_column='Contact_Fax', blank=True) # Field name made lowercase.
    contact_email = models.CharField(max_length=360, db_column='Contact_Email', blank=True) # Field name made lowercase.
    contact_alternatecontact = models.CharField(max_length=135, db_column='Contact_AlternateContact', blank=True) # Field name made lowercase.
    contact_accountnumber = models.IntegerField(null=True, db_column='Contact_AccountNumber', blank=True) # Field name made lowercase.
    contact_datecreated = models.DateTimeField(null=True, db_column='Contact_DateCreated', blank=True) # Field name made lowercase.
    contact_type = models.IntegerField(null=True, db_column='Contact_Type', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_clientcontacts'

class ViewContactdefendants(models.Model):
    contact_pk = models.IntegerField(unique=True, db_column='Contact_PK') # Field name made lowercase.
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
    contact_type = models.IntegerField(null=True, db_column='Contact_Type', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_contactdefendants'

class ViewInsurancecompanies(models.Model):
    contact_pk = models.IntegerField(unique=True, db_column='Contact_PK') # Field name made lowercase.
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_middlename = models.CharField(max_length=360, db_column='Contact_MiddleName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    contact_company = models.CharField(max_length=360, db_column='Contact_Company', blank=True) # Field name made lowercase.
    contact_address1 = models.CharField(max_length=360, db_column='Contact_Address1', blank=True) # Field name made lowercase.
    contact_city = models.CharField(max_length=360, db_column='Contact_City', blank=True) # Field name made lowercase.
    contact_address2 = models.CharField(max_length=360, db_column='Contact_Address2', blank=True) # Field name made lowercase.
    contact_state = models.CharField(max_length=360, db_column='Contact_State', blank=True) # Field name made lowercase.
    contact_zip = models.CharField(max_length=30, db_column='Contact_ZIP', blank=True) # Field name made lowercase.
    contact_telephone = models.CharField(max_length=135, db_column='Contact_Telephone', blank=True) # Field name made lowercase.
    contact_telephone2 = models.CharField(max_length=135, db_column='Contact_Telephone2', blank=True) # Field name made lowercase.
    contact_fax = models.CharField(max_length=135, db_column='Contact_Fax', blank=True) # Field name made lowercase.
    contact_email = models.CharField(max_length=360, db_column='Contact_Email', blank=True) # Field name made lowercase.
    contact_alternatecontact = models.CharField(max_length=135, db_column='Contact_AlternateContact', blank=True) # Field name made lowercase.
    contact_type = models.IntegerField(null=True, db_column='Contact_Type', blank=True) # Field name made lowercase.
    contact_datecreated = models.DateTimeField(null=True, db_column='Contact_DateCreated', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_insurancecompanies'

class ViewNochecklistreportPi(models.Model):
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    matters_pk = models.IntegerField(db_column='Matters_PK') # Field name made lowercase.
    matters_mattertype = models.IntegerField(null=True, db_column='Matters_MatterType', blank=True) # Field name made lowercase.
    matters_active = models.TextField(db_column='Matters_Active', blank=True) # Field name made lowercase. This field type is a guess.
    pichk_pk = models.IntegerField(db_column='PIChk_PK') # Field name made lowercase.
    class Meta:
        db_table = u'view_nochecklistreport_pi'

class ViewSumpicaseinventory(models.Model):
    year = models.IntegerField(null=True, db_column='Year', blank=True) # Field name made lowercase.
    month = models.IntegerField(null=True, db_column='Month', blank=True) # Field name made lowercase.
    firm_est_fee = models.DecimalField(decimal_places=6, null=True, max_digits=40, db_column='Firm Est Fee', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    expr1 = models.IntegerField(null=True, db_column='Expr1', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'view_sumpicaseinventory'

class ViewcasenotesCount(models.Model):
    staff_stafffullname = models.CharField(max_length=150, db_column='Staff_StaffFullName', blank=True) # Field name made lowercase.
    case_note_count = models.IntegerField(null=True, db_column='Case Note Count', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    casenotes_notedate = models.DateField(null=True, db_column='CaseNotes_NoteDate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'viewcasenotes_count'

class Viewspecialclaims(models.Model):
    matters_pk = models.IntegerField(db_column='Matters_PK') # Field name made lowercase.
    matters_matterid = models.CharField(max_length=297, db_column='Matters_MatterID', blank=True) # Field name made lowercase.
    contact_lastname = models.CharField(max_length=360, db_column='Contact_LastName', blank=True) # Field name made lowercase.
    contact_firstname = models.CharField(max_length=360, db_column='Contact_FirstName', blank=True) # Field name made lowercase.
    diagnostic = models.DecimalField(decimal_places=2, null=True, max_digits=40, db_column='Diagnostic', blank=True) # Field name made lowercase.
    treatment = models.DecimalField(decimal_places=2, null=True, max_digits=40, db_column='Treatment', blank=True) # Field name made lowercase.
    total_claims = models.DecimalField(decimal_places=2, null=True, max_digits=40, db_column='Total Claims', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    low_factor = models.DecimalField(decimal_places=2, null=True, max_digits=40, db_column='Low Factor', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    mid_factor = models.DecimalField(decimal_places=2, null=True, max_digits=40, db_column='Mid Factor', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    high_factor = models.DecimalField(decimal_places=2, null=True, max_digits=40, db_column='High Factor', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    class Meta:
        db_table = u'viewspecialclaims'

