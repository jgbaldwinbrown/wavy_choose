#!/bin/bash

set -e

cd empdir
ls *.out | while read i; do
    echo ""
done | \
parallel -j 4 {}

#ls "$@" | \
# sed 's/\..*//g' | \
# uniq | \
# sort | \
# uniq | \
# head | \
# while read i ;do 
#    echo $i 
#    cat ${i}.out ${i}.txt 
#    echo "" 
#done


#cd empdir
#ls *.fa | while read i; do
#    echo "../choose_cwt.py -w 30 -m 10 $i | mawk 'NR%2==0{print(length($1))}' | sort | uniq -c > `basename $i .fa`.out"
#done | \
#parallel -j 4 {}
