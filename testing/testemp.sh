#!/bin/bash
set -e

cd empirical_tests/full

#ls *.gz | while read i; do
#    echo "../../../wavy_choose.py -w 500 -m 200 -t 1 <(gunzip -c $i) | \
#    pigz -p 7 > test_results/`basename $i _clustered.fa.gz`_chosen.fa.gz"
#done | \
#parallel -j 4 {}

python3 ../../plot_emptest.py \
    <(gunzip -c mrna_align.REF_PGA_scaffold_5__62_contigs__length_17832310_carnac_out_clustered.fa.gz) \
    <(gunzip -c test_results/mrna_align.REF_PGA_scaffold_5__62_contigs__length_17832310_carnac_out_chosen.fa.gz) \
    50 \
    test_results/test_plot
