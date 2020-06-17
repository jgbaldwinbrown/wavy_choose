#!/bin/bash

set -e

ls "$@" | \
 sed 's/\..*//g' | \
 uniq | \
 sort | \
 uniq | \
 head | \
 while read i ;do 
    echo $i 
    cat ${i}.out ${i}.txt 
    echo "" 
done
