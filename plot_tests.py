#!/usr/bin/env python3

import sys
import re
import matplotlib.pyplot as plt
import seaborn as sns
import gzip

def falens(conn):
    lens = []
    curlen = 0
    for l in conn:
        l=l.decode("utf-8").rstrip('\n')
        if len(l) == 0:
            pass
        elif l[0] == ">" and curlen > 0:
            lens.append(curlen)
            curlen = 0
        else:
            curlen += len(l)
        if curlen > 0:
            lens.append(curlen)
            curlen = 0
    return(lens)

def plothist(origlens, finallens, opath):
    #sns.set_style('darkgrid')
    sns.distplot(origlens)
    for i in finallens:
        plt.axvline(i, 0, color="red")
    plt.savefig(opath)
    plt.close()
    #plt.axvline(2.8, 0,0.17)

def main():
    #paths = [x.rstrip('\n') for x in sys.stdin]
    
    cl_mincount = int(sys.argv[1])
    clre = re.compile(r"_clustered")
    clre2 = re.compile(r"_clustered.fa.gz")
    paths_nocl = [clre.sub("_chosen", path) for path in paths]
    opath_prefixes = [clre2.sub("_test.pdf", path) for path in paths]
    
    for path, path_nocl, opath in zip(paths, paths_nocl, opaths):
        with gzip.open(path, "r") as conn:
            origlens = falens(conn)
        with gzip.open(path_nocl, "r") as conn:
            finallens = falens(conn)
        plothist(origlens, finallens, opath)

if __name__ == "__main__":
    main()
