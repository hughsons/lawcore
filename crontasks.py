from django.http import *
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User, Group, Permission
from models import Projects, AccessTokens, CronJobs, CronFiles
from django.contrib.auth.models import User;
from google.appengine.api import files
import logging, os
import urllib2
import urllib
import httplib
import xml.dom.minidom
import json
import webapp2
from google.appengine.api import urlfetch
from django.db.models import signals
from views import *
from threading import *
import sys
import time
import subprocess
import re
import sched
import time
from datetime import datetime as dt
import datetime



def now_str():
    """Return hh:mm:ss string representation of the current time."""
    t = dt.now().time()
    return t.strftime("%H:%M:%S")

def CronBucketFiles(bucket_name, pid, cronid, wildcard):
    logging.info('Fetch Started::  %s', now_str())
    file_list = []
    file_path = ""
    PROJECT_NUMBER = pid
    bucket_name = bucket_name
    refreshtokens = refresh_Token("gcs")
    logging.info('Refresh Token:: %s', refreshtokens)
    req = urllib2.Request('http://storage.googleapis.com/%s' %bucket_name)
    req.add_header('Host', 'storage.googleapis.com')
    req.add_header('Date', 'Wed, 26 Mar 2013 01:22:11 GMT')
    req.add_header('Authorization', 'Bearer %s' %refreshtokens)
    req.add_header('Content-Length', '0')
    req.add_header('x-goog-api-version', '2')
    req.add_header('x-goog-project-id', PROJECT_NUMBER)
    socket = urllib2.urlopen(req)
    html = socket.read()
    socket.close()
    dom = xml.dom.minidom.parseString(html)
    
    for node in dom.getElementsByTagName('Key'):
        file_name = node.childNodes[0].data
        #logging.info('File Name:: %s', file_name)
        if file_name.__contains__(wildcard):
            record_exists = CronFiles.objects.filter(filenames=file_name).count()
            if record_exists < 1:
                logging.info('File Name:: %s', file_name)
                file_list.append(file_name)
                t = CronFiles(filenames=file_name,
                              file_addedby="cronfile",
                              file_status='ON',
                              file_processed="NO")
                t.cronjobs_id=cronid
                t.save()
    logging.info('Fetch Ended Started::  %s', now_str())
    return file_list

def updatefilestatus(id, jobid,responsedata):

      t = CronFiles.objects.get(id=id)
      t.file_processed='YES'
      t.file_status='OFF'
      t.file_jobid=jobid
      t.file_responsedata=responsedata
      t.save()
      
    

def ProcessCronJobsClass(object):
    logging.info('Started::  %s', now_str())
    try:
        cronitems = CronJobs.objects.all().filter(cron_status="ON")
        s=dt.now()
        k=s.strftime("%Y:%m:%d %H:%M:%S")
        for fileitems in cronitems:
            buckfiles = CronBucketFiles(fileitems.bucketname, fileitems.projectid, fileitems.id, fileitems.wildcards)
            
            t = CronJobs.objects.get(id=fileitems.id)
            t.lastprocessed_date=k
            t.save()
            
            #logging.info('Project ID::  %s', k)
    except Exception, e:
        cronitems = "not found"
        logging.info('Exception::  %s', e)
        
    logging.info('Completed::  %s', now_str())
    #bucketfiles = CronBucketFiles()
    return HttpResponse(cronitems)

def ProcessFileRecordsClass(object):
    logging.info('Started::  %s', now_str())
    cronitems = ""
    editfilestatus = ""
    processfile = ""
    try:
        fileobjects = CronFiles.objects.filter(file_status="ON", file_processed="NO")
        for fileitems in fileobjects:
            cronobjects = CronJobs.objects.get(id = fileitems.cronjobs_id)
            filepath = "gs://"+cronobjects.bucketname+'/'+fileitems.filenames
            processfile = assignjobstofiles(cronobjects.projectid,cronobjects.datasetid,cronobjects.tablename,filepath,cronobjects.formats,cronobjects.fieldDelimiter)
            logging.info(processfile['jobReference']['jobId'])
            editfilestatus = updatefilestatus(fileitems.id, processfile['jobReference']['jobId'],processfile)
    except Exception, e:
        cronitems = "not found"
        processfile = "no file processd"
        logging.info('Exception::  %s', e)
    logging.info('Completed::  %s', now_str())
    return HttpResponse(processfile)

def assignjobstofiles(pid,did,tid,filepath,formats,delimiter):
    PROJECT_NUMBER = pid
    did=did
    tid = tid
    sourceuri= filepath
    refreshtokens = refresh_Token("BQ")
    headers = {}
    newresource = ('{"configuration":{"load":{"sourceFormat": "'+formats+'","fieldDelimiter": "'+delimiter+'","destinationTable":{"projectId": "'+PROJECT_NUMBER+'","datasetId":"'+did+'","tableId":"'+tid+'"},"sourceUris":["'+sourceuri+'"]}}}')
    #logging.info(newresource)
    try:
        headers = {"Authorization": "Bearer "+refreshtokens,
                   "X-JavaScript-User-Agent": "Google APIs Explorer",
                   "Content-Type":  "application/json; charset=UTF-8"}
        conn = httplib.HTTPConnection('https://www.googleapis.com/auth/bigquery')
        conn.request("POST", "https://www.googleapis.com/bigquery/v2/projects/"+PROJECT_NUMBER+"/jobs",
                     newresource, headers)
        res = conn.getresponse()
    except Exception, e:            
            logging.info('Error value-------------------')
            logging.info('Reason:: %s',e)
            logging.info('Error value-------------------')
    data = res.read()
    jasondata = json.loads(data)
    #logging.info(jasondata)
    #logging.info(jasondata['jobReference']['jobId'])
    return jasondata

def Movefilestohistory(object):
    logging.info('Started::  %s', now_str())
    refreshtokens = refresh_Token("gcs")
    filename = "sonnypot/newfiles/1343325279_stock.txt"
    destination = "sonnypot/oldfiles/1343325279_stock.txt"
    try:
        fileobjects = CronFiles.objects.filter(file_status="OFF", file_processed="YES")
        
        for fileitems in fileobjects:
            cronobjects = CronJobs.objects.get(id = fileitems.cronjobs_id)
            sourcepath = cronobjects.bucketname+'/'+fileitems.filenames
            req=urlfetch.fetch('http://'+cronobjects.historyfiles+'.storage.googleapis.com/'+fileitems.filenames,
                               method='PUT',
                               headers={'Date':'Sat, 4 May 2013 22:22:11 GMT',
                                        'Authorization':'Bearer %s' %refreshtokens,
                                        'Host': 'bucket.storage.googleapis.com',
                                        'Content-Length':'0',
                                        'x-goog-api-version':'2',
                                        'x-goog-copy-source':sourcepath,
                                        'x-goog-project-id':cronobjects.projectid,
                                        'x-goog-metadata-directive':'REPLACE'},
                                allow_truncated=False,
                                follow_redirects=True,
                                deadline=10,
                                validate_certificate=False)
            if req.status_code == 200:
                deletefile = deleteprocessedfile(cronobjects.bucketname, fileitems.filenames, cronobjects.projectid, refreshtokens)
            logging.info(req.content+'<br>==<br>'+str(req.status_code))
    except Exception as e:
        logging.info('error value-------------------')
        logging.info(e)
        logging.info('error value-------------------')
    #data = res.read()
    #jasondata = json.loads(data)
    logging.info('Completed::  %s', now_str())
    return HttpResponse('Total Files'+ str(fileobjects.count()))

def deleteprocessedfile(bucket,filename,projectid, refreshtokens):
    try:
        req=urlfetch.fetch('http://'+bucket+'.storage.googleapis.com/'+filename,
                           method='DELETE',
                           headers={'Date':'Sat, 30 Mar 2013 22:22:11 GMT',
                                    'Authorization':'Bearer %s' %refreshtokens,
                                    'Host': 'bucket.storage.googleapis.com',
                                    'x-goog-project-id':projectid,
                                    'x-goog-api-version':'2',
                                    },
                           allow_truncated=False,
                           follow_redirects=True,
                           deadline=10,
                           validate_certificate=False)
    except Exception as e:
        logging.info('error value-------------------')
        logging.info(e)
        logging.info('error value-------------------')
        #return HttpResponse(req.content)        
    if req.status_code == 204:
        logging.info('File Deleted success %s', filename)
    else:
        logging.info('Failed to delete file %s', filename)
