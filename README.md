# bioinf-dev-test

There are three tasks to complete within the hour.  Use Google and ask questions if you get stuck!

## Initial setup

Create a virtual environment:

`$ python3 -m venv venv`

Activate the new virtual environment:

`$ source venv/bin/activate`

Install requirements:

`$ python3 -m pip install -r requirements.txt`

## Coding tasks

- Make a branch for your solutions.
- Commit and push your local changes to the remote repository.

### Coding task 1 - file parsing

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

### Coding task 2 - API call

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

## Bioinformatics tasks

Run `docker run --rm -it edmundlth/bioinf_tech_interview:latest`, this will download and run a docker container in interactive mode. 
`python3` and `samtools` are installed in this container.

Running in this mode, there are some programs like text editors that are not accessible. So the Python task should just be written and run in Python interactive mode within the container as well. 

Please note that these are contrived tasks to test your ability to understand and use existing tools. There might be alternative methods you can think of that do not involve the tools suggested, but we encourage that you read and understand the documentations of the tools (if you aren’t already familiar with them). 

### Bioinformatics task 1

Question: Which tag in the BAM file header gives a record of programs that have been run on the BAM file? 

Extract the corresponding program records of the provided BAM file into a plain text file. 

Commands to use: 
- `samtools view`
- `grep`

References:
- SAM / BAM file format reference: https://samtools.github.io/hts-specs/SAMv1.pdf

### Bioinformatics task 2

Suppose those programs are industry secrets (they aren’t) and we would like to remove them. 
In this task, we would like to produce a new BAM file that is identical to the old one except it will have no @PG tag. 

Commands to use: 
- `samtools view`
- `grep -v` 
- `samtools reheader`

References:
- SAMtools documentation: http://www.htslib.org/doc/samtools.html


### Bioinformatics task 3

Use Python to create a BED file with each row being a 1 million base pair window of chromosome 1 of the human genome (hg19). The regions in the BED file should jointly cover the chromosome. 

Hints:
- BED files are 0-indexed. 
- Use the `chr` prefix in the BED file chromosome name. 
- Chromosome 1 has <250 million base pairs. 

References:
- BED file format: http://genome.ucsc.edu/FAQ/FAQformat#format1
- SAMtools documentation: http://www.htslib.org/doc/samtools.html

Find out the total coverage for each of the regions defined above. 

Commands to use: 
- `samtools sort`
- `samtools index`
- `samtools bedcov`

