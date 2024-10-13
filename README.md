first creat suitable environment, acording to your requiremnts
activate the environment (conda activate quick_bed_sort) and go to the project folder, make sure you have all the files in that folder, you want to work on.
here you will have a scripts folder, a chrome_selection file and a snakemake file.
run snakemake file using command "snakemake -p --snakefile sort_bed_by_chrom.smk --cores all".
you will get output sorted merged file in, sorted folder.
