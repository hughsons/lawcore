from django.conf.urls.defaults import *
from django.contrib import admin
from views import *
from user_actions import *
from auth_views import *


handler500 = 'djangotoolbox.errorviews.server_error'
admin.autodiscover()
urlpatterns = patterns('',
    #('^$', 'django.views.generic.simple.direct_to_template',{'template': 'home.html'}),
    url(r'^$', SummaryClass.as_view(), name='upload'),
    url(r'^accounts/login/$','auth_views.loginpage',name='login'),
	url(r'^custlogin', 'auth_views.LoginView', name='stafflogin'),
    url(r'^users', MyHandler.as_view(), name='vprofile'),
    url(r'^admin/', include(admin.site.urls)),
	(r'^login$', 'auth_views.loginpage'),
    (r'^logout$', 'auth_views.logout_view'),
	url(r'^viewcontacts$', ContactsViewClass.as_view(), name='viewcontacts'),
    url(r'^viewcalls$', CallsViewClass.as_view(), name='edituser'),
    url(r'^newcall$', AddCallFormClass.as_view(), name='modifyuser'),
	url(r'^edtcall$', EditCallFormClass.as_view(), name='modifyuser'),
    url(r'^addcontact$', AddContactFormClass.as_view(), name='deluser'),
	url(r'^editcontact$', EditContactFormClass.as_view(), name='editcontact'),
	url(r'^vcontactinfo$', ViewContactClass.as_view(), name='editcontact'),
	url(r'^vcallinfo$', ViewCallClass.as_view(), name='vcallinfo'),
	url(r'^callactions$', CallsActionClass.as_view(), name='addcontact'),
	url(r'^matteractions$', MatterActionClass.as_view(), name='matteractions'),
	url(r'^matteradd$', AddMatterFormClass.as_view(), name='addmatter'),
	url(r'^viewmatters$', ViewMattersClass.as_view(), name='viewmatters'),
	url(r'^addpayment$', AddPaymentFormClass.as_view(), name='addpayment'),
	url(r'^edipayform$', EditPaymentFormClass.as_view(), name='EditPaymentFormClass'),
	url(r'^editmatter$', EditMatterFormClass.as_view(), name='EditMatterFormClass'),
	url(r'^vmatid$', ViewMatterClass.as_view(), name='ViewMatterFormClass'),
	url(r'^viewtasks$', ViewTasksFormClass.as_view(), name='viewtasks'),
	url(r'^editaskform$', EditTasksFormClass.as_view(), name='editaskform'),
	url(r'^addcase$', AddCaseFormClass.as_view(), name='addcase'),
	url(r'^pracman$', PractiseManagerViewClass.as_view(), name='addcase'),

	url(r'^actdr$', ActiveFamilyViewClass.as_view(), name='actdr'),
	url(r'^actbcy$', ActiveBankruptcyViewClass.as_view(), name='actdr'),
	url(r'^actpi$', ActivePersonalViewClass.as_view(), name='actdr'),
	url(r'^actep$', ActiveEstateViewClass.as_view(), name='actdr'),
	url(r'^actprobate$', ActiveProbateViewClass.as_view(), name='actdr'),
	url(r'^acttransac$', ActiveTransactionalViewClass.as_view(), name='actdr'),
	url(r'^actcivil$', ActiveCivilViewClass.as_view(), name='actdr'),
	url(r'^wordomc$', PractiseManagerViewClass.as_view(), name='actdr'),
	url(r'^worpi$', PractiseManagerViewClass.as_view(), name='actdr'),
	url(r'^worprobate$', PractiseManagerViewClass.as_view(), name='actdr'),
	url(r'^opendemands$', PractiseManagerViewClass.as_view(), name='actdr'),
	url(r'^specdamages$', PractiseManagerViewClass.as_view(), name='actdr'),
	url(r'^dailycasenotes$', PractiseManagerViewClass.as_view(), name='actdr'),
	url(r'^datecasenotes$', PractiseManagerViewClass.as_view(), name='actdr'),

	url(r'^fmemo$', ViewFactMemoClass.as_view(), name='ViewFactMemoClass'),
	url(r'^fpays$', ViewPaymentsClass.as_view(), name='ViewPaymentsClass'),
	url(r'^fconrs$', ViewContactRecordsClass.as_view(), name='ViewPaymentsClass'),
	url(r'^fconrs$', ViewContactRecordsClass.as_view(), name='ViewPaymentsClass'),

)
