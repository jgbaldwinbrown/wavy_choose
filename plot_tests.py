#!/usr/bin/env python3

import sys
import re
import matplotlib.pyplot as plt
import numpy as np
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

def falens_allcl(conn):
    lens_allcl = {}
    cluster = ""
    curlen = 0
    for l in conn:
        l=l.decode("utf-8").rstrip('\n')
        if len(l) == 0:
            pass
        elif l[0] == ">":
            if curlen > 0 and len(cluster) > 0:
                if not cluster in lens_allcl:
                    lens_allcl[cluster] = []
                lens_allcl[cluster].append(curlen)
            curlen = 0
            cluster = l.rstrip('\n').split()[1].split(':')[0]
        else:
            curlen += len(l)
        if curlen > 0 and len(cluster) > 0:
            if not cluster in lens_allcl:
                lens_allcl[cluster] = []
            lens_allcl[cluster].append(curlen)
    return(lens_allcl)

def plothist(origlens, finallens, opath, cl_mincount):
    if len(origlens) > cl_mincount and len(finallens) > 0:
        try:
            print(origlens)
            print(finallens)
            sns.distplot(origlens)
            for i in finallens:
                plt.axvline(i, 0, color="red")
            plt.savefig(opath)
            plt.close()
        except np.linalg.LinAlgError:
            print("singular matrix:", opath)
            pass

def plothist_allcl(origlens_allcl, finallens_allcl, opath_prefix, cl_mincount):
    for cluster, lens in finallens_allcl.items():
        plothist(origlens_allcl[cluster], lens, opath_prefix + "_cluster_" + str(cluster) + "_test.pdf", cl_mincount)

def main():
    paths = [x.rstrip('\n') for x in sys.stdin]
    
    cl_mincount = int(sys.argv[1])
    clre = re.compile(r"_clustered")
    clre2 = re.compile(r"_clustered.fa.gz")
    paths_nocl = [clre.sub("_chosen", path) for path in paths]
    opath_prefixes = [clre2.sub("", path) for path in paths]
    
    for path, path_nocl, opath_prefix in zip(paths, paths_nocl, opath_prefixes):
        with gzip.open(path, "r") as conn:
            origlens_allcl = falens_allcl(conn)
        with gzip.open(path_nocl, "r") as conn:
            finallens_allcl = falens_allcl(conn)
        plothist_allcl(origlens_allcl, finallens_allcl, opath_prefix, cl_mincount)

if __name__ == "__main__":
    main()
