#!/usr/bin/env python3

import random
import math
import sys
import os
import tqdm

def getdist(mean, stdev, count):
    return [int(math.floor(random.gauss(mean, stdev))) for x in range(count)]

def getdists(stdev, readcount, peakcount, peakrange):
    fulldist = []
    peaks = []
    for i in range(peakcount):
        peaks.append(random.uniform(peakrange[0], peakrange[1]))
        fulldist.extend(getdist(peaks[-1], stdev, readcount))
    return((fulldist, peaks))

def printdist(dist, conn):
    n = 0
    drawlist = ["a","g","t","c"]
    for i in dist:
        if i > 0:
            conn.write(">" + str(n) + "\n")
            outline = [random.choice(drawlist) for x in range(i)]
            conn.write(''.join(outline) + "\n")
            n += 1

def printsum(summary, conn):
    for i in summary:
        conn.write(str(i) + "\n")

if __name__ == "__main__":
    if not os.path.isdir("testdir"):
        os.mkdir("testdir")
    
    for mypeakcount in tqdm.tqdm([1, 2, 3, 4], desc="peaks"):
        for myreadcount in tqdm.tqdm([50, 100, 300,1000], desc="reads"):
            for mystdev in tqdm.tqdm([1, 5, 10, 30], desc="stdev"):
                for myrep in tqdm.tqdm(range(3), desc="reps"):
                    mydist_and_sum = getdists(mystdev, myreadcount, mypeakcount, (1,1000))
                    path = "testdir/choosetest_peaks%d_reads%d_sd%d_rep%d.fa" % (mypeakcount, myreadcount, mystdev, myrep)
                    with open(path, "w") as conn:
                        printdist(mydist_and_sum[0], conn)
                    path2 = path.split('.')[0] + ".txt"
                    with open(path2, "w") as conn:
                        printsum(mydist_and_sum[1], conn)
