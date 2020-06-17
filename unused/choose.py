#!/usr/bin/env python3

#import scipy
from scipy.signal import find_peaks
import sys
import argparse

def readfasta(inconn):
    header = ""
    seq = ""
    out = []
    for l in inconn:
        l=l.rstrip('\n')
        if l[0] == ">":
            if len(header) > 0 and len(seq) > 0:
                out.append((header, seq))
            header = l
            seq = ""
        else:
            seq = seq + l
    if l[0] == ">":
        if len(header) > 0 and len(seq) > 0:
            out.append((header, seq))
        header = l
        seq = ""
    return out

def getlens(fadat):
    out = []
    for i in fadat:
        out.append(len(i[1]))
    return(out)

def gethist(falens):
    out = []
    mymin = min(falens)
    mymax = max(falens)
    for i in range(mymin,mymax+1):
        out.append((i, falens.count(i)))
    return(out)

def getpeaks(hist, count, threshold, distance, prominence):
    histcounts = [x[1] for x in hist]
    out = find_peaks(histcounts, height = count, threshold = threshold, distance = distance, prominence = prominence)
    return(out[0])

def getfasta(peaks, hist, fadat):
    out = []
    histlens = [x[0] for x in hist]
    peaklens = [histlens[x] for x in peaks]
    for i in fadat:
        if len(i[1]) in peaklens:
            out.append(i)
    return(out)

def writefasta(fasta):
    for i in fasta:
        print(i[0])
        print(i[1])

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Identify the reads that best represent each transcript in a cluster.")
    parser.add_argument("infasta", help="The input fasta in which to identify transcripts.")
    parser.add_argument("-c", "--count", help="The minimum number of transcripts with matching lengths required for a hit (default=None).")
    parser.add_argument("-t", "--threshold", help="The difference in counts between peak and neighboring region to call peak (default=None).")
    parser.add_argument("-d", "--distance", help="The minimum distance between peaks (default=None).")
    parser.add_argument("-p", "--prominence", help="The minimum prominence required to call a peak (default=None).")

    args = parser.parse_args()

    if args.infasta == "-":
        inconn = sys.stdin
    else:
        inconn = open(args.infasta,"r")

    if args.count:
        count = args.count
    else:
        count = None

    if args.threshold:
        threshold = args.threshold
    else:
        threshold = None

    if args.distance:
        distance = args.distance
    else:
        distance = None

    if args.prominence:
        prominence = args.prominence
    else:
        prominence = None

    fadat = readfasta(inconn)
    print("fadat:")
    print(fadat)
    falens = getlens(fadat)
    print("falens:")
    print(falens)
    hist = gethist(falens)
    print("hist:")
    print(hist)
    peaks = getpeaks(hist, count, threshold, distance, prominence)
    print("peaks:")
    print(peaks)
    peakfasta = getfasta(peaks, hist, fadat)
    print("peakfasta:")
    print(peakfasta)
    writefasta(peakfasta)

    inconn.close()
