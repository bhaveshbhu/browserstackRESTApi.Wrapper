#Name: Bhavesh Sharma

from browserstack import auth,api
import config

auth = auth.AuthHandler(config.USERNAME,config.ACCESS_KEY,proxy_data=config.PROXY_URL)

apiO = api.API(auth, api_root='/3')

#apiO._create_browser_worker()
#print apiO.result

apiO._get_browsers(flat="true")
print apiO.result

apiO._api_status()
print apiO.result

#apiO._get_workers()
#print apiO.result

#apiO._get_worker_byId(id= "20220444")
#print apiO.result

#apiO._delete_worker(id= "20220444")
#print apiO.result





