#!/bin/bash
# arg $1 is the folder containing all employes
# arg $2 is the email folder (sent, inbox)


for f in `find $1/* -name $2`
do
   printf $f; printf " "; find $f -type f | wc -l 
done


