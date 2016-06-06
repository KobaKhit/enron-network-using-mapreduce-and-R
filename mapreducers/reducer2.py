import sys
import re

# input comes from STDIN

# Mapper.py output
# sender<TAB>receivers<TAB>date<TAB>subject<TAB>body<TAB>id


# Reducer.py output
# if identity function is used
# sender<TAB>receivers<TAB>date<TAB>subject<TAB>body<TAB>id

# Long format
# date<TAB>sender<TAB>reciever<TAB>id


for line in sys.stdin:
	# Identity functuion
	print line
	#

	# Long format
	# parts = line.split("\t")
	# key = parts[5]
	# recievers = parts[1].split(',')

	# for r in recievers:
	# 	print '%s\t%s\t%s\t%s' % (parts[2], parts[0], re.sub(r'<|>',"",r), parts[5])
