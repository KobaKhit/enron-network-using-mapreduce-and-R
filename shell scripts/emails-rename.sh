#!/bin/bash

# $1 enron-emails folder
# $2 sent, inbox or any other folder thats present in everyone's account
# $2 destination folder where to save uniquely named email files



for f in `find $1/*/$2 -name '*'`
do
   filename=`echo $f|awk -F'/' '{SL = NF-1; TL = NF-2; print $TL "_" $SL  "_" $NF}'`
   cp $f $3/$filename
done
