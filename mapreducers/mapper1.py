#!/usr/bin/python

import sys
import re

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

# Mapper output is sorted in ascending order by key.
# Make reciever count a key.
# Substract the reciever count from a constant thats greater 
# than total number of emails to obtain results in descending 
# order by reciever count. (total emails = 600k+)

constant = 10000000

sender1 = None 
sender2 = None
origin = None
recievers = []

#TO DO: Figure the right regex for recievers
# input comes from STDIN (standard input)
for line in sys.stdin:

	# remove leading and trailing whitespace
	line = line.strip().lower()

	# Get sender ids
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
		# print(line,"\n")
		recievers = re.sub("x-to:", "", line).strip()
		recievers = [x.strip().split('<')[0] for x in re.split(r'>,', recievers)]
		recievers = list(map(func, recievers))

	# print line
	if sender1 is not None and sender2 is not None and len(recievers)>0 and origin is not None:
		rank = constant-len(recievers)
		recievers = ",".join(recievers)

		print('%s\t%s\t%s\t%s\t%s' % (rank, sender1, sender2, origin, recievers))

		sender1 = None 
		sender2 = None
		origin = None
		recievers = []

# Mapper.py output
# rank<TAB>sender1<TAB>sender2<TAB>origin<TAB>recievers



# Sample email
####################

# Message-ID: <8579795.1075855681604.JavaMail.evans@thyme>
# Date: Tue, 19 Sep 2000 09:35:00 -0700 (PDT)
# From: phillip.allen@enron.com
# To: pallen70@hotmail.com
# Subject: Westgate Proforma-Phillip Allen.xls
# Mime-Version: 1.0
# Content-Type: text/plain; charset=us-ascii
# Content-Transfer-Encoding: 7bit
# X-From: Phillip K Allen
# X-To: pallen70@hotmail.com
# X-cc: 
# X-bcc: 
# X-Folder: \Phillip_Allen_Dec2000\Notes Folders\Sent
# X-Origin: Allen-P
# X-FileName: pallen.nsf

# ---------------------- Forwarded by Phillip K Allen/HOU/ECT on 09/19/2000 
# 04:35 PM ---------------------------


# "George Richards" <cbpres@austin.rr.com> on 09/08/2000 05:21:49 AM
# Please respond to <cbpres@austin.rr.com>
# To: "Phillip Allen" <pallen@enron.com>
# cc: "Larry Lewter" <retwell@mail.sanmarcos.net> 
# Subject: Westgate Proforma-Phillip Allen.xls


# Enclosed is the preliminary proforma for the Westgate property is Austin
# that we told you about.  As you can tell from the proforma this project
# should produce a truly exceptional return of over 40% per year over 3 years.

#####################
