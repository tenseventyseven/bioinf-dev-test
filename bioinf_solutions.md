Possible solutions provided by Edmund

### Bioinformatics task 1

Answer: @PG

Run: `samtools view -H input.bam | grep "^@PG" > program_tag.txt`

### Bioinformatics task 2

Run: `samtools view -H input.bam | grep -v “^@PG” > header.sam` to produce a SAM file with only the header with @PG tag removed. 

Run: `samtools reheader -P header.sam input.bam > new.bam`. Note that `-P` tag is required to not introduce a new `@PG` tag recording the reheader operation. 

### Bioinformatics task 3

See: `bioinf_task3.py`

Run `samtools sort input.bam > input.sorted.bam` to sort the BAM file (just as a precaution, the original file is actually sorted). 

Run `samtools index input.sorted.bam` to generate the index file. 

Run `samtools bedcov region.bed input.sorted.bam`

