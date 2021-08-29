#pip install request (to install requests)

import requests
import json
total_user=0
for x in range(2, 13):
        #To traverse each page
	r = requests.get("https://reqres.in/api/users?page="+str(x))
	#retrieving object
	r_obj=r.json()
	#print(r_obj)
	print("Page : %2d, User : %2d" % (r_obj['page'], len(r_obj['data'])))
	total_user+=len(r_obj['data'])
	#print("Page : %2d, User : %2d" % (r_obj['page'], r_obj['total']))
print("Total User=",total_user)	
