import sys
from collections import defaultdict

chrom_list = sys.argv[1].split(",")  
filenam_prefix = sys.argv[2]       

# now I am making dict to store pointers of each chromosomes
fp_dict = {}
chrom_flag = defaultdict(lambda: False)

for chrom in chrom_list:
    fname = f"{filenam_prefix}chrom_{chrom}.bed"
    tmp_fp = open(fname, "w")
    fp_dict[chrom] = tmp_fp
    chrom_flag[chrom] = True

for line in sys.stdin:
    chrom_name = line.split("\t")[0]
    if chrom_flag[chrom_name]:
        fp_dict[chrom_name].write(line)

for chrom in chrom_list:
    fp_dict[chrom].close()
