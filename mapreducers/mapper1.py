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
# mapper output is sorted in ascending order by key.
# make reciever count a key.
# substract the reciever count from a constant thats greater 
# then total number of emails to obtain results in descending 
# order by reciever count. (total emails = 60k)
constant = 100000 

sender = None
recievers = []

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip().lower()
	if "x-from:" in line:
	    # split the line into sender and reciever list
	    sender = re.split(r'x-from:', line)[1].strip()
	    sender = re.sub(r'<|>','',sender)

	if "x-to:" in line:
		recievers = re.sub("x-to:", "", line).strip()
		recievers = re.split(r',', recievers)
		recievers = [x.strip() for x in recievers]


	if sender is not None and len(recievers)>0:
		# print '%s\t%s' % (constant - len(recievers),sender)
		print '%s\t%s' % (sender, recievers)
		# print '%s\t%s' % (sender, len(recievers))
		sender = None
		recievers = []


# Mapper.py output

# ina rangel      ['amanda huble']
# ina rangel      ['arsystem@mailman.enron.com @ enron']
# ina rangel      ['information risk management']
# ina rangel      ['john j lavorato']
# phillip k allen ['8774820206@pagenetmessage.net']
# phillip k allen ['alan comnes']
# phillip k allen ['al pollard']
# phillip k allen ['al pollard']
# phillip k allen ['al pollard']
# phillip k allen ['al pollard']
# phillip k allen ['al pollard']
# phillip k allen ['andrea richards']
# phillip k allen ['andrea richards']
# phillip k allen ['andrea richards']
#########################################
