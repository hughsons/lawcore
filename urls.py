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
    url(r'^addcontact$', AddContactFormClass.as_view(), name='deluser'),
	url(r'^editcontact$', EditContactFormClass.as_view(), name='editcontact'),
	url(r'^vcontactinfo$', ViewContactClass.as_view(), name='editcontact'),
	url(r'^vcallinfo$', ViewCallClass.as_view(), name='vcallinfo'),
	url(r'^callactions$', CallsActionClass.as_view(), name='addcontact'),
	url(r'^matteractions$', MatterActionClass.as_view(), name='matteractions'),
	url(r'^matteradd$', AddMatterFormClass.as_view(), name='addmatter'),
	url(r'^viewmatters$', ViewMattersClass.as_view(), name='viewmatters'),
)
