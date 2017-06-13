#!/usr/bin/env python

import tailer
#open file and watch for new lines
import re
#import regex
import time
#import time
openfile = open('/private/var/log/system.log')
userprocessregex = re.compile('sshd: .*USER_PROCESS')
# successful login
startedregex = re.compile(' no path for address ')
#started login
oncloseregex = re.compile('Service exited with abnormal code: 255')
#three lines show up in system log file 
wasLastAttemptSuccessful = False

def onLine(line):
    global wasLastAttemptSuccessful
    #print '[D] new line:', line
    if userprocessregex.search(line):
    	# onSuccess
        print '[+] ssh login successful %s' % time.strftime("%m/%d/%y %H:%M:%S")
        wasLastAttemptSuccessful = True
    elif startedregex.search(line):
    	# onStart event
        print '[+] ssh connection started %s' % time.strftime("%m/%d/%y %H:%M:%S")
    if oncloseregex.search(line):
    	# onClose event
        if wasLastAttemptSuccessful:
        	wasLastAttemptSuccessful = False
        else:
            print '[+] ssh login attempt failed  %s' % time.strftime("%m/%d/%y %H:%M:%S")

    
for line in tailer.follow(openfile):
    onLine(line)    
