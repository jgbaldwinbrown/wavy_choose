#!/bin/bash
set -e

#python3 make_bigtest.py

find simulated_tests/test_results/big/ -name '*.fa' | while read i; do
    echo "../wavy_choose.py -w 30 -m 10 $i | mawk 'NR%2==0{print(length($1))}' | sort | uniq -c > `dirname $i`/`basename $i .fa`.out"
done | \
parallel -j 4 {}

find simulated_tests/test_results/big/ -name '*clustered.fa.gz'
