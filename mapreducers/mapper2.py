#!/usr/bin/python

####################
# Sample email

# Message-ID: <22646222.1075857437613.JavaMail.evans@thyme>
# Date: Wed, 13 Dec 2000 04:05:00 -0800 (PST)
# From: fletcher.sturm@enron.com
# To: frank.hayden@enron.com
# Subject: Re: Westpower Web site
# Mime-Version: 1.0
# Content-Type: text/plain; charset=us-ascii
# Content-Transfer-Encoding: 7bit
# X-From: Fletcher J Sturm
# X-To: Frank Hayden
# X-cc: 
# X-bcc: 
# X-Folder: \Fletcher_Sturm_Dec2000\Notes Folders\Sent
# X-Origin: Sturm-F
# X-FileName: fsturm.nsf

# Lloyd will
#####################


import sys
import re

from datetime import datetime
# mapper output is sorted in ascending order by key.

id_count = 1
key = None
sender = None
recievers = []
date = None
subject = None
body = ''

previous_line = 0
previous_line2 = 0

# column headers
# ("sender", 'reciever', 'date', 'subject', 'body')

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip().lower()


	if "message-id: " in line:
		previous_line = 1
		matches =  re.search(r'<(.*)>', line)
		if matches:
			newkey = matches.group()
			newkey = re.sub(r'<|>',"",newkey)

	if "date: " in line and "," in line and previous_line > 0:
		date = re.sub(r"date: ", "", line).strip()
		date = re.search(r"([a-z]{3}, [0-9]{2} [a-z]{3} [0-9]{4}.*:[0-9]{2})", date)
		if date:
			date = datetime.strptime(date.group(), "%a, %d %b %Y %H:%M:%S")
		else:
			date = None

	if "subject: " in line and previous_line > 0:
		subject = re.sub("subject: ", "", line).strip()

	if "x-from:" in line and previous_line > 0:
	    # split the line into sender and reciever list
	    sender = re.split(r'x-from:', line)[1].strip()
	    #sender = re.sub(r'<|>|\"','',sender)

	if "x-to:" in line and previous_line > 0:
		recievers = re.sub("x-to:", "", line).strip()
		recievers = re.split(r',', recievers)
		recievers = [x.strip() for x in recievers]


	if 'x-filename: ' in line:
		previous_line2 = 1

	if previous_line2 > 0 and 'message-id:' not in line and 'x-filename' not in line and previous_line > 0:
		body += " " + re.sub(" ", " ", line).strip()

	
	if not key:
		key = newkey

	# if sender is not None and len(recievers)>0 and date is  not None  and subject is not None and body != '':
	if key != newkey and date is not None and sender is not None and len(recievers)>0:
		# print output
		print '%s\t%s\t%s\t%s\t%s\t%s' % (sender, ",".join(recievers), str(date), subject, body, id_count)
		
		id_count += 1
		key = newkey
		sender = None		
		recievers = []
		date = None
		subject = None
		body = ''

		previous_line = 0
		previous_line2 

if key != None and date is not None and sender is not None and len(recievers)>0:
	print '%s\t%s\t%s\t%s\t%s\t%s' % (sender, ",".join(recievers), str(date), subject, body, id_count)

# Mapper.py output
# sender<TAB>receivers<TAB>date<TAB>subject<TAB>body<TAB>id

# phillip k allen	brenda stone <bs_stone@yahoo.com> @ enron	2000-12-06 04:41:00	re: court ordered notice to customers and registered users of	  brenda,  i checked my records and i mailed check #1178 for the normal amount on...