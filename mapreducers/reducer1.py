#!/usr/bin/env python

########################################
# Mapper.py output

# Mapper.py output
# rank<TAB>sender1<TAB>sender2<TAB>origin<TAB>recievers

# 9999999	john arnold	john arnold	arnold-j	slafontaine@globalp.com @ enron


#########################################

import sys
import re


key = None
total_rec = 0
all_recievers = []

# input comes from STDIN
for line in sys.stdin:
	parts = line.split("\t")
	newkey = parts[1]
	recievers = parts[-1]
	recievers = recievers.split(',')
	recievers = [re.sub(ur'\"|\'','',x).strip() for x in recievers]
	all_recievers += recievers
	
	if not key:
		key = newkey

	if key != newkey:
		conns = [x for x in set(all_recievers) if x != ""]
		nconns = len(conns)
		print(key + '\t' + ','.join(conns))
		# print(key + '\t' + str(nconns))
		key = newkey
		all_recievers = []

if key != None:
	print (key + "\t" + ','.join([x for x in set(all_recievers) if x != ""]))
	# print(key + "\t" + str(len([x for x in set(all_recievers) if x != ""])))

# Reducer output
# sender1<TAB>recievers
# or
# sender1<TAB>number of recievers
#
# community  	1077
# gorte, david 	795
# clyatt, julie 	795
# dl-technology 	795
# dottie kerr 	795
# energy insight editor @enron	795
