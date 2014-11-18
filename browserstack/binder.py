#Bhavesh Sharma
#Date : 17-11-14

"""
Python wrapper for Browserstack API
"""


from browserstack.error import BrowserStackError

class BindAPI(object):
    
    def __init__(self, api,config):
        self.path = '/%s' % config.get('path')
        #self.path = "/worker"
        #print self.path
    	#self.allowed_param = config.get('allowed_param', [])
    	self.method = config.get('method', 'GET')
    	
    	self.require_auth = config.get('require_auth', True)
        self.api = api
		
        if self.require_auth and not api.auth:
            raise BrowserStackError('Authentication required!')
		
        self._data = config.pop('post_data', config.get("default_val"))
        self.headers = config.pop('headers', config.get("defaut_header"))
        
        self.result = self.api.auth.fetch(self).json()
