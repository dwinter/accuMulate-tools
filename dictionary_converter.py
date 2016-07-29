#!/usr/bin/python
import sys
from Bio import SeqIO 

def main():
    """Represent a reference genome as a dictionary of chromosome names 
    and chromosome lengths for the purpose of using the dictionary to 
    create windows of non-overlapping genomic regions to run the software 
    accuMUlate in parallel. 
    Usage: 
        $python2 dictionary_converter.py [reference_genome.fasta]
    """  
    with open(sys.argv[1]) as file_input:
        records=SeqIO.parse(file_input, "fasta")
        fasta={x.id:len(x) for x in records} 
        for k,v in fasta.iteritems():
	    print k+"\t",v
    
if __name__ == "__main__":
    main()
