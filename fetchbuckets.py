import urllib
import urllib2
import httplib
import json
import xml.dom.minidom
import time

# From Installed Applications
CLIENT_ID = '507190119457.apps.googleusercontent.com'
CLIENT_SECRET = 'zxHDv4m8Yw0ZnJPR8tVLBNvM'

class GoogleCloudStorage1(object):

  access_token = ""
  token_expiry_seconds = 0 

  def __init__(self):

    if GoogleCloudStorage1.token_expiry_seconds > time.time():
      # No need to refresh
      return

    self.access_token = ""
    f = open("oauth2.dat")
    text = f.read()
    f.close()
    json_data = json.loads(text)
    token_expiry_seconds = time.mktime(time.strptime(json_data['token_expiry'], "%Y-%m-%dT%H:%M:%SZ"))
    refresh_token = json_data['token_response']['refresh_token']
    
    if time.time() >= token_expiry_seconds:
      refresh_json = json.loads(self.RefreshToken(refresh_token))
      json_data['access_token'] = refresh_json['access_token']
      json_data['token_expiry'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.localtime(time.time() + 3000))
      f = open("oauth2.dat", 'w')
      json.dump(json_data, f)
      f.close()

    GoogleCloudStorage.access_token = json_data['access_token']
    GoogleCloudStorage.token_expiry = time.mktime(time.strptime(json_data['token_expiry'], "%Y-%m-%dT%H:%M:%SZ"))

  def RefreshToken(self, pRefresh_Token):
    print "Refreshing Token"
    data = {}
    data['refresh_token'] = pRefresh_Token
    data['client_id'] = CLIENT_ID
    data['client_secret'] = CLIENT_SECRET
    data['grant_type'] = 'refresh_token'
    req = urllib2.Request('https://accounts.google.com/o/oauth2/token', urllib.urlencode(data))
    socket = urllib2.urlopen(req)
    html = socket.read()
    return html


  def GetBucketList(self, project_id):
    bucket_list = []
    req = urllib2.Request('http://storage.googleapis.com')
    req.add_header('Host', 'storage.googleapis.com')
    req.add_header('Date', 'Wed, 26 Mar 2013 01:22:11 GMT')
    req.add_header('Authorization', 'Bearer %s' %GoogleCloudStorage.access_token)
    req.add_header('Content-Length', '0')
    req.add_header('x-goog-api-version', '2')
    req.add_header('x-goog-project-id', project_id)
    socket = urllib2.urlopen(req)
    html = socket.read()
    socket.close()
    dom = xml.dom.minidom.parseString(html)
    for node in dom.getElementsByTagName('Name'):
      bucket_list.append(node.childNodes[0].data)

    return bucket_list

  def GetFileList(self, project_id, file_path):
    file_list = []
    bucket_name = file_path.split("/")[0]
    # Removing bucket from the file path

    if file_path.__contains__("/"):
      file_path = file_path[file_path.index("/")+1:]
    else:
      bucket_name = file_path
      file_path = ""
      
    req = urllib2.Request('http://storage.googleapis.com/%s' %bucket_name)
    req.add_header('Host', 'storage.googleapis.com')
    req.add_header('Date', 'Wed, 26 Mar 2013 01:22:11 GMT')
    req.add_header('Authorization', 'Bearer %s' %GoogleCloudStorage.access_token)
    req.add_header('Content-Length', '0')
    req.add_header('x-goog-api-version', '2')
    req.add_header('x-goog-project-id', project_id)
    socket = urllib2.urlopen(req)
    html = socket.read()
    socket.close()
    dom = xml.dom.minidom.parseString(html)
    for node in dom.getElementsByTagName('Key'):
      file_name = node.childNodes[0].data
      if file_name.__contains__(file_path) or file_path == "":
        file_list.append(node.childNodes[0].data)

    return file_list
    
gcs = GoogleCloudStorage1()
# Must be Project ID
buckets = gcs.GetBucketList('507190119457')

print "Buckets in the Project"
print "-" * 60
for bucket in buckets:
  print bucket
print "-" * 60
print "\n"

# Must be Project ID and File Path preceeded by Bucket Name
files =  gcs.GetFileList('507190119457', 'testingsimon/')

print "Files in the Bucket 'TestingSimon'"
print "-" * 60
for file_name in files:
  print file_name

print "-" * 60

