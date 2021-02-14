# bioinf-dev-test

## Setup

Create a virtual environment:

`$ python3 -m venv venv`

Activate the new virtual environment:

`$ source venv/bin/activate`

Install requirements:

`$ python3 -m pip install -r requirements.txt`

## Before and after tasks

- Make a branch for your solutions.
- Commit and push your local changes to the remote repository.

## Task 1 - File parsing

Using the `csv` module, read the contents of `files.txt` and print a list of the filtered FastQ and BAM files and their total size.

The expected output of `python3 task1.py` is:

```
FastQ filenames: ['204007381_LA.204007381_LA_0_filtered_R1.fastq.gz', '204007381_LA.204007381_LA_0_filtered_R2.fastq.gz'], total bytes: 302509058

BAM filenames: ['204007381_LA.alignments.bam', '204007381_LA.transcriptome.bam', '204007381_LA.bam'], total bytes: 1152888006

```

Notes:
- `files.txt` is pipe-delimited
- there is a header
- there are comments starting with `#`
- there blank lines

## Task 2 - API call

Using the `requests` module, make an API call to https://api.quotable.io/quotes (see: https://github.com/lukePeavey/quotable)

Get 5 quotes tagged wisdom" or "happiness" and print out the quotes and their author.

The expected output of `python3 task2.py` is:

```
1. Wisdom is a kind of knowledge. It is knowledge of the nature, career, and consequences of human values. -- Sidney Hook

2. The three great essentials to achieve anything worth while are: Hard work, Stick-to-itiveness, and Common sense. -- Thomas Edison

3. If you are bitter, you are like a dry leaf that you can just squash, and you can get blown away by the wind. There is much more wisdom in forgiveness. -- Vusi Mahlasela

4. Applause is a receipt, not a bill. -- Dale Carnegie

5. The greatest obstacle to being heroic is the doubt whether one may not be going to prove one's self a fool; the truest heroism is to resist the doubt; and the profoundest wisdom, to know when it ought to be resisted, and when it be obeyed. -- Nathaniel Hawthorne

```

## Task 3 - Bioinformatics

Edmund?!