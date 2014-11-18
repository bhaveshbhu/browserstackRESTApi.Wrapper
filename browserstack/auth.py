#Bhavesh Sharma
#Date : 17-11-14

"""
Python wrapper for Browserstack API
"""

from browserstack.error import BrowserStackError
from browserstack.api import API
import base64
import os
import requests

try:
    import simplejson as json
except ImportError:
    import json

class AuthHandler(object):
    A_HOST = 'api.browserstack.com/3'
    def __init__(self,USERNAME,ACCESS_KEY,**kwargs):
        self._username = USERNAME
        self.access_key = ACCESS_KEY
        self.api = None
        self.proxy = None
        if kwargs.get('proxy_data'):
        	self.proxy = kwargs.get('proxy_data')
        
        self.session = requests.Session()	
       	self.proxy_url = None
       	self.myheader = None
       	url = self._get_auth_url('')
       	if not self.proxy==None:
       		self.proxy_url = {'http': self.proxy.get('url')}
       		token = base64.encodestring('%s:%s' %(self.proxy.get('proxyUsername'), self.proxy.get('proxyPassword'))).strip()
       		self.myheader = {'Proxy-Authorization': 'Basic %s' %token}
			
		#self.fetch()
		
		
		
		self.result = "{}"
		
		
    def _get_auth_url(self,extra):
        prefix = 'http://'
        return prefix + self.A_HOST+extra

    def _checkResponse(self,ret):
        if ret.status_code == 200:
            return ret
    	elif ret.status_code == 407:
    		raise BrowserStackError("Proxy Authentication unsuccessfull")
        elif ret.status_code == 401:
            raise BrowserStackError("Authentication Failure")
        elif ret.status_code == 422:
            raise BrowserStackError("InvalidRequestError")
        else:
        	raise BrowserStackError(ret.status_code)
        
    def fetch(self,binder):
        try:
        	url = self._get_auth_url(binder.path)
        	print binder._data
        	datatoSend = None
        	if not len(binder._data)==0:
        		datatoSend = json.dumps(binder._data)
        	if not self.myheader==None:
        		binder.headers.update(self.myheader)
        	
        	if binder.method == 'POST':
        		r = self.session.post(url, data=binder._data, proxies = self.proxy_url, headers = binder.headers,auth=(self._username,self.access_key))
        	elif binder.method == 'GET':
        		r = requests.get(url, params=binder._data, proxies = self.proxy_url, headers =binder.headers,auth=(self._username,self.access_key))
        	else:
        		r = requests.delete(url, proxies = self.proxy_url, headers = binder.headers,auth=(self._username,self.access_key))	
        	#print r.status_code
        	process = self._checkResponse(r)
        	return r
        except Exception, e:
        	raise BrowserStackError(e)
            

