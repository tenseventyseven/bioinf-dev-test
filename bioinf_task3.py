#!/usr/bin/env python3

with open("region.bed", "w") as outfile:
    for i in range(250):
        outfile.write(f"chr1\t{i * 1000000}\t{(i + 1) * 1000000}\n")
