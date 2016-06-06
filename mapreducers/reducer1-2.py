#!/usr/bin/env python

########################################
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

import sys
import re

def replace_sqbr(x):
	# erases square brackets from string
	return(re.sub(r'\[|\]',"",x))

key = None
total_rec = 0
all_recievers = []

# input comes from STDIN
for line in sys.stdin:
	parts = line.split("\t")
	# newkey = re.sub(ur'[^(]*(\<.*\>)[^)]*$','',parts[0])
	newkey = parts[0]
	recievers = replace_sqbr(parts[1])
	recievers = recievers.split(',')
	# remove brackets and content inside, ex.g. name <name@email.com> -> name
	recievers = [re.sub(ur'[^(]*(\<.*\>)[^)]*$','',x).strip() for x in recievers]
	all_recievers += recievers
	
	if not key:
		key = newkey

	if key != newkey:
		conns = [x for x in set(all_recievers) if x != ""]
		print key + '\t' + replace_sqbr(str(conns))
		key = newkey
		all_recievers = []

if key != None:
	print key + "\t" + replace_sqbr(str([x for x in set(all_recievers) if x != ""]))
