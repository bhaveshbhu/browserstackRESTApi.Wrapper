#Bhavesh Sharma
#Date : 17-11-14

"""
Python wrapper for Browserstack API
"""

import os
from browserstack.binder import BindAPI
from browserstack.error import BrowserStackError

class API(object):
    def __init__(self, auth_handler=None,
            host='api.browserstack.com',
            cache=None, api_root='/3'
            ):
        self.auth = auth_handler
        if auth_handler:
            auth_handler.api = self
                
        self.host = host
        self.api_root = api_root
        self.result = None

        
    def _get_browsers(self,**kwargs):
    #default config
    	_config = {}
       	for k in kwargs:
       		_config[k] = kwargs[k]

    	headers = {'content-type': 'application/json', 'Accept': 'application/json'}
        default = {'path' :'browsers',
        			'require_auth': 'True',
        			"default_val":_config,
        			"defaut_header" : headers
        			}
       	self.result = BindAPI(self,default).result


    def _get_workers(self,**kwargs):
    #default config
    	_config = {}

    	headers = {'content-type': 'application/json', 'Accept': 'application/json'}
        default = {'path' :'workers',
        			'require_auth': 'True',
        			"default_val":_config,
        			"defaut_header" : headers
        			}
       	self.result = BindAPI(self,default).result
        

    def _api_status(self,**kwargs):
    #default config
    	_config = {}
#       	for k in kwargs:
#       		default[k] = kwargs[k]

    	headers = {'content-type': 'application/json', 'Accept': 'application/json'}
        default = {'path' :'status',
        			'require_auth': 'True',
        			"default_val":_config,
        			"defaut_header" : headers
        			}
       	self.result = BindAPI(self,default).result



    def _get_worker_byId(self,**kwargs):
    #default config
    	_config = {}

    	if kwargs.get("id")==None:
    		raise InvalidRequestError("No id passed")
    	headers = {'content-type': 'application/json', 'Accept': 'application/json'}
        default = {'path' :'worker/%s' % kwargs['id'],
        			'require_auth': 'True',
        			"default_val":_config,
        			"defaut_header" : headers
        			}
       	self.result = BindAPI(self,default).result

        
    def _create_browser_worker(self,**kwargs):
    	_config = {
            "os":"Windows",
            "os_version":"7",
            "browser_version":"8.0",
            "browser":"ie",
        	"url":"http://google.com"}
        	
    	headers = {'content-type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}
       	for k in kwargs:
       		_config[k] = kwargs[k]

    	default = {'path' :'worker',
        			'require_auth': 'True',
        			"default_val":_config,
        			"defaut_header" : headers,
        			"method":"POST"
        			}
        			

       	self.result = BindAPI(self,default).result



    def _delete_worker(self,**kwargs):
    	_config = {}
    	
    	if kwargs.get("id")==None:
    		raise InvalidRequestError("No id passed")
		
				
    	headers = {'content-type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}
    	default = {'path' :'worker/%s'% kwargs["id"],
        			'require_auth': 'True',
        			"default_val":_config,
        			"defaut_header" : headers,
        			"method":"DELETE"
        			}
       	self.result = BindAPI(self,default).result
