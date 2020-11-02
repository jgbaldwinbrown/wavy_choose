# Wavy_choose

Wavy_choose is a tool for identifying full-length transcripts from Oxford Nanopore mRNA sequencing data using read length distribution.

# Dependencies

- Python 3
- Scipy

# Installation

Wavy_choose comes as a single python3 script, and can be installed by adding
its containing directory to you `$PATH`. The below script will create a new
directory, `~/mybin`, and will add wavy_choose to it.

```sh
mkdir -p ~/mybin
cp wavy_choose.py ~/mybin/wavy_choose
export PATH=$PATH:~/mybin
```

Following on the above example, to make wavy_choose permanently available, you
simply need to add its containing folder permanently to your PATH by adding the
following line to your `.bashrc`:

```sh
export PATH=$PATH:~/mybin

# Usage

```
usage: wavy_choose.py [-h] [-w MAX_WIDTH] [-m MIN_WIDTH] [-l MIN_LENGTH]
                      [-t MIN_TRANSCRIPTS]
                      infasta

Identify the reads that best represent each transcript in a cluster.

positional arguments:
  infasta               The input fasta in which to identify transcripts.

optional arguments:
  -h, --help            show this help message and exit
  -w MAX_WIDTH, --max_width MAX_WIDTH
                        The largest acceptable peak width.
  -m MIN_WIDTH, --min_width MIN_WIDTH
                        The smallest acceptable peak width.
  -l MIN_LENGTH, --min_length MIN_LENGTH
                        The smallest acceptable read length.
  -t MIN_TRANSCRIPTS, --min_transcripts MIN_TRANSCRIPTS
                        Minimum number of transcripts that must be taken per
                        cluster.
```

# Workflow

## Align mRNA reads with `minimap2`

Minimap2 is available here: [https://github.com/lh3/minimap2](https://github.com/lh3/minimap2)

Align reads to each other using Minimap2:

```sh
minimap2 -x ava-ont minion_rna_reads.fq minion_rna_reads.fq > ovlpfull.paf
```

## Convert file formats:

Convert read fastq to fasta:

```sh
cat minion_rna_reads.fq | sed -n '1~4s/^@/>/p;2~4p' > minion_rna_reads.fa
```

Convert minimap paf format to carnac format:

Carnac-LR and paf_to_CARNAC.py available here: [https://github.com/kamimrcht/CARNAC-LR](https://github.com/kamimrcht/CARNAC-LR)

```sh
paf_to_CARNAC.py ovlpfull.paf minion_rna_reads.fa input_CARNAC.txt
```

## Run carnac on all reads to generate clusters

Here, `ulimit -s unlimited` increases the process stack size to allow for deeper recursion, which carnac requires.

```sh
temp/minion_rnaseq_carnac/1/output_CARNAC.txt: temp/minion_rnaseq_carnac/1/input_CARNAC.txt 
	ulimit -s unlimited && CARNAC-LR -f input_CARNAC.txt -o output_CARNAC.txt
```
		
Convert carnac files to fasta:

carnac2fa.py is included with wavy_choose

```sh
scripts/carnac/carnac2fa.py temp/minion_rnaseq_carnac/1/output_CARNAC.txt temp/minion_rnaseq_carnac/1/minion_rna1-4_1d_combo.fa
	mkdir -p outs
	python carnac2fa.py output_CARNAC.txt minion_rna_reads.fa > output_CARNAC.fa
```
