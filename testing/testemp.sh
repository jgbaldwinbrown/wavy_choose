#!/bin/bash
set -e

cd empirical_tests/full

ls *.gz | while read i; do
    echo "../../../wavy_choose.py -w 500 -m 200 -t 1 <(gunzip -c $i) | \
    pigz -p 7 > test_results/`basename $i _clustered.fa.gz`_chosen.fa.gz"
done | \
parallel -j 4 {}
