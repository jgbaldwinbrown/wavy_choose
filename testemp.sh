cd empdir
#
#ls *_clustered.fa.gz | while read i; do
#    echo "../choose_cwt.py -w 500 -m 200 <(gunzip -c $i) | pigz -p 7 > `basename $i _clustered.fa.gz`_chosen.fa.gz"
#done | \
#parallel -j 4 {}

ls | grep '_cluster_[0-9]*.fa.gz' | while read i; do
    echo "../choose_cwt.py -w 500 -m 200 <(gunzip -c $i) | pigz -p 7 > `basename $i _clustered.fa.gz`_chosen.fa.gz"
done | \
parallel -j 4 {}
