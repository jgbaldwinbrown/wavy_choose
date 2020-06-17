#!/usr/bin/env python3

#import scipy
#from scipy.signal import find_peaks
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
    for e in enumerate(fadat):
        out.append((e[0],len(e[1][1])))
    return(out)

def getpeak(lens, percent_larger):
    slens = sorted(lens, reverse=True, key=lambda x: x[1])
    index_to_take = int(round((len(slens) * (1.0 - percent_larger))))
    i=0
    out = None
    for j in slens:
        if i==index_to_take:
            out = j
            break
        i += 1
    return(out)

def getfasta(peak, fadat):
    return(fadat[peak[0]])

def writefasta(fasta):
    print(fasta[0])
    print(fasta[1])

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Identify the reads that best represent each transcript in a cluster.")
    parser.add_argument("infasta", help="The input fasta in which to identify transcripts.")
    parser.add_argument("-p", "--percent_larger", help="Percent of the data that the selected read should be larger than (default=0.95).")

    args = parser.parse_args()

    if args.infasta == "-":
        inconn = sys.stdin
    else:
        inconn = open(args.infasta,"r")

    if args.percent_larger:
        percent_larger = float(args.percent_larger)
    else:
        percent_larger = 0.95

    fadat = readfasta(inconn)
    falens = getlens(fadat)
    peaks = getpeak(falens, percent_larger)
    peakfasta = getfasta(peaks, fadat)
    writefasta(peakfasta)

    #print("fadat:")
    #print(fadat)
    #print("falens:")
    #print(falens)
    #print("peaks:")
    #print(peaks)
    #print("peakfasta:")
    #print(peakfasta)
    inconn.close()
