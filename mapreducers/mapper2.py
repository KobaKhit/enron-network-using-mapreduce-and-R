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

regex1 = r'(\b(?=\w*[@\.])[\w\-\.@]+\b)' # get email adressess (contain one @ and one .)
regex2 = r'(<.*>)' # get everything between the brackets
regex3 = r'\"(.*)\"'


def get_first_match(pattern,x):
	match = re.search(pattern,x)
	if match:
		return match.group(0)
	else: return re.sub(r'\"','',x)

def func(x):
	# ["allen, phillip"] -> ["phillip allen"]
	g = lambda x: x.split(',')
	namelastname = g(x)[1].strip() + " " + g(x)[0].strip() if ',' in x else x
	return re.sub(r"\"|\'",'', namelastname)

# mapper output is sorted in ascending order by key.

id_count = 1
key = None
sender1 = None 
sender2 = None
origin = None
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

	if "x-from:" in line:
	    sender = re.split(r'x-from:', line)[1].strip()
	    sender2 = get_first_match(regex1,  sender)
	    sender2 = re.sub(regex2,'', sender2)
	    if len(sender2) == 1: sender2 = None
	    
	    sender = re.sub(regex1 + '|'+ regex2,'',sender)
	    sender1 = get_first_match(regex3 ,  sender)
	    if '@' not in sender1: sender1 = re.sub(r'\.|\"','',sender1)
	    
	# Origin if the email, i.e. Enron's employee name to whom belongs an email account
	if "x-origin:" in line:
	    origin = re.split(r'x-origin:', line)[1].strip()

	if "x-to:" in line:
		recievers = re.sub("x-to:", "", line).strip()
		recievers = [x.strip().split('<')[0] for x in re.split(r'>,', recievers)]
		if len(recievers) > 15: continue
		else: recievers = list(map(func, recievers))



	if 'x-filename: ' in line:
		previous_line2 = 1

	# if previous_line2 > 0 and 'message-id:' not in line and 'x-filename' not in line and previous_line > 0:
	# 	body += " " + re.sub(" ", " ", line).strip()

	if not key:
		key = newkey

	# if sender is not None and len(recievers)>0 and date is  not None  and subject is not None and body != '':
	if key != newkey and date is not None and sender1 is not None and len(recievers)>0:
		# print output
		print '%s\t%s\t%s\t%s\t%s' % (str(date), sender1, ",".join(recievers), subject, id_count)
		
		id_count += 1
		key = newkey
		sender = None		
		recievers = []
		date = None
		subject = None
		body = ''

		previous_line = 0
		previous_line2 

if key != None and date is not None and sender1 is not None and len(recievers)>0:
	print '%s\t%s\t%s\t%s\t%s' % (str(date), sender1, ",".join(recievers), subject, id_count)

# Mapper.py output
# sender<TAB>receivers<TAB>date<TAB>subject<TAB>id

# phillip k allen	brenda stone <bs_stone@yahoo.com> @ enron	2000-12-06 04:41:00	re: court ordered notice to customers and registered users of	1