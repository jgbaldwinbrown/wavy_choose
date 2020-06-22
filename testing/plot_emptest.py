#!/usr/bin/env python3

import sys
import re
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import gzip

def add_to_count(counts, header, length):
    name = header[1:].split(":")[0]
    if name not in counts:
        counts["name"] = []
    counts["name"].append(length)

def get_counts(conn):
    counts = {}
    curlen = 0
    header = ""
    for l in conn:
        l = l.rstrip('\n')
        if len(l) == 0:
            continue
        elif l[0] == ">":
            if curlen > 0:
                add_to_count(counts, header, curlen)
            header = l
            curlen = 0
        else:
            curlen += len(l)
    if curlen > 0:
        add_to_count(counts, header, curlen)
    return(counts)

def combine_counts(orig_counts, clustered_counts):
    out = {}
    for key, value in orig_counts.items():
        if key in clustered_counts:
            out[key] = {"orig": value, "clustered": clustered_counts[key]}
    return(out)

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

def plothist_all(allcounts, opath_prefix, cl_mincount):
    for cluster, countsdict in allcounts.items():
        plothist(countsdict["orig"], countsdict["clustered"], opath_prefix + "_cluster_" + str(cluster) + "_test.pdf", cl_mincount)

def main():
    orig_path = sys.argv[1]
    clustered_path = sys.argv[2]
    cl_mincount = int(sys.argv[3])
    opath_prefix = sys.argv[4]
    
    with open(orig_path, "r") as origconn:
        all_orig_counts = get_counts(origconn)
    with open(clustered_path, "r") as clusteredconn:
        all_clustered_counts = get_counts(clusteredconn)
    all_counts = combine_counts(all_orig_counts, all_clustered_counts)
    plothist_all(allcounts, opath_prefix, cl_mincount)

if __name__ == "__main__":
    main()
