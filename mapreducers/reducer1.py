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

key = None
all_recievers = []

# input comes from STDIN
for line in sys.stdin:
	parts = line.split("\t")
	newkey = parts[0]
	recievers = re.sub(r'\[|\]',"",parts[1])
	recievers = recievers.split(',')
	all_recievers += recievers
	
	if not key:
		key = newkey

	if key != newkey:
		print key + '\t' + str(len(set(all_recievers)))
		key = newkey
		all_recievers = []

if key != None:
	print key + "\t" + str(len(set(all_recievers)))
