cd testdir
ls *.fa | while read i; do
    echo "../choose_cwt.py -w 30 -m 10 $i | mawk 'NR%2==0{print(length($1))}' | sort | uniq -c > `basename $i .fa`.out"
done | \
parallel -j 4 {}
