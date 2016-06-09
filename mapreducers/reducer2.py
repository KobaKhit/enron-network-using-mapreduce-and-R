import sys
import re

# input comes from STDIN

# Mapper.py output
# date<TAB>sender<TAB>receivers<TAB>subject<TAB>id

# 2000-12-06 04:41:00	brenda stone <bs_stone@yahoo.com> @ enron	2000-12-06 04:41:00	re: court ordered notice to customers and registered users of	1

# Reducer.py output
# if identity function is used
# date<TAB>sender<TAB>eceivers<TAB>subject<TAB>id

# Long format
# date<TAB>sender<TAB>reciever<TAB>id


for line in sys.stdin:
	# Identity function. Uncomment line below
	# print line

	# Long format. Uncomment lines below
	parts = line.split("\t")
	iid = parts[4]
	recievers = parts[1].split(',')

	for r in recievers:
		print '%s\t%s\t%s\t%s' % (parts[2], parts[0], r, iid)
