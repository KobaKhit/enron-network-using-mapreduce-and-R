#!/bin/bash
# $1 search folders
# $2 destination
SOURCE=../data/enron-emails/*/inbox/  # Enron emails folder source. sent is an alternative
DEST_FOLDER=../data/enron-emails-inbox

for f in `find $SOURCE -name '*'`
do
   filename=`echo $f|awk -F'/' '{SL = NF-1; TL = NF-2; print $TL "_" $SL  "_" $NF}'`
   cp $f $DEST_FOLDER/$filename
done
