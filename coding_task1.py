#!/usr/bin/env python3
import csv
import re

fastq_filenames = []
fastq_total_bytes = 0
bam_filenames = []
bam_total_bytes = 0

with open("files.txt") as csvfile:
    reader = csv.reader(csvfile, delimiter="|")

    # Skip header
    next(reader)

    for row in reader:
        # Skip empty rows
        if len(row) == 0:
            continue

        # Skip comments
        if row[0].startswith("#"):
            continue

        # Parse row
        filename = row[1]
        bytes = int(row[2])

        # FastQs
        if re.match(r"^.*filtered.*fastq.gz$", filename):
            fastq_filenames.append(filename)
            fastq_total_bytes += bytes

        # BAMs
        if filename.endswith(".bam"):
            bam_filenames.append(filename)
            bam_total_bytes += bytes

print(f"FastQ files: {fastq_filenames}, total bytes: {fastq_total_bytes}\n")
print(f"BAM files: {bam_filenames}, total bytes: {bam_total_bytes}\n")
