#!/usr/bin/env python
# coding=utf-8
# code by 92ez.com

import requests
from Crypto.Hash import SHA
import random
import time
import json
import sys
import re

def tryLoginMi():

	host = sys.argv[1]

	homeRequest = requests.get('http://'+ host +'/cgi-bin/luci/web/home')
	key = re.findall(r'key: \'(.*)\',',homeRequest.text)[0]

	
	aimurl = "http://"+host+"/cgi-bin/luci/api/xqsystem/login"

	nonce = "0_00:88:65:3d:bd:22_"+ str(int(time.time())) +"_"+str(random.randint(1000,10000))

	pwdtext = sys.argv[2]

	pwd = SHA.new()
	pwd.update(pwdtext+key)
	hexpwd1 = pwd.hexdigest()

	pwd2 = SHA.new()
	pwd2.update(nonce+hexpwd1)
	hexpwd2 = pwd2.hexdigest()


	data = {
		"logtype":2,
		"nonce":nonce,
		"password":hexpwd2,
		"username":"admin"
		}


	response = requests.post(url=aimurl,data=data,timeout = 5)
	resjson = json.loads(response.content)
	
	if resjson['code'] == 0:
		print 'Login Success! Token is '+resjson['token']
	else:
		print 'Login Failed! Code is '+str(resjson['code'])

if __name__ == '__main__':
	print '\n########### Login Mi Router Test Py ############'
	print '		Author 92ez.com'
	print '################################################\n'

	tryLoginMi()