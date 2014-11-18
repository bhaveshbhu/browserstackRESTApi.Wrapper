browserstackRESTApi.Wrapper
===========================

Installation
------------

### From source

```bash
$ git clone https://github.com/bhaveshbhu/browserstackRESTApi.Wrapper.git
$ Extract and cd browserstackRESTApi.Wrapper/
$ python setup.py install --user  # to install in the user directory (~/.local)
$ sudo python setup.py install    # to install globally
```

Tutorial
------------
   *Edit config.py file for Proxy Settings if using proxy.
   *Edit username and browserStack Access Key [Link](https://www.browserstack.com/accounts/automate).
   Create AuthHandler Object using 
'''bash
  $ auth = auth.AuthHandler(config.USERNAME,config.ACCESS_KEY,proxy_data=config.PROXY_URL)
'''
```bash
$ auth = auth.AuthHandler(config.USERNAME,config.ACCESS_KEY,proxy_data=config.PROXY_URL) (if using proxy)
$ auth = auth.AuthHandler(config.USERNAME,config.ACCESS_KEY,proxy_data=None)            (if not using proxy)   
$ apiO = api.API(auth, api_root='/3')
```

Examples
------------
```bash
$ apiO._create_browser_worker()
$ print apiO.result

$ apiO._get_browsers(flat="true")
$ print apiO.result

$ apiO._api_status()
$ print apiO.result

$ apiO._get_workers()
$ print apiO.result

$ apiO._get_worker_byId(id= "20220444")
$ print apiO.result
```




