
def nucleotide_counting(dnaStr):
    """
    Counts each occurrence of nucleotide molecules (A, C, G, T) in a DNA string and prints them
    :return: None
    """
    print ("DNA String: ", dnaStr)
    print ("'A' Count: ", dnaStr.count("A"))
    print ("'C' Count: ", dnaStr.count("C"))
    print ("'G' Count: ", dnaStr.count("G"))
    print ("'T' Count: ", dnaStr.count("T"))

def dna_transcribe_rna(dnaStr):
    #TODO CHECK THIS
    """
    Given DNA string (coding strand), transcribe by replacing all 'T' instances with 'U"
    (DNA to RNA ('A', 'C', 'G', 'U')).
    DNA string length <=1000 nt.
    :return: Transcribed RNA string of the DNA string.
    """
    for i in dnaStr:
        if i == "T": i = "U"
    return dnaStr

def reverse_complement(dnaStr):
    """
    Complements in DNA Strings are 'A' and 'T', as well as 'C' and 'G'.
    Given a DNA string, the reverse complement is reversing the symbols of the string, then taking
    the complement of each symbol.
    :return: The reverse complement of a DNA string of length <= 1000 bp.
    """
    reverse = dnaStr[::-1]
    for i in reverse:
        if i == "A": i = "T"
        elif i == "T": i = "A"
        elif i == "G": i = "C"
        elif i == "C": i = "G"
        else:
            print("Error")
    return reverse



def get_gc_content():
    """
    GC-content is percentage of symbols in string that are 'C' or 'G', where the reverse complement has the same
    GC-content. Databases hold labeled DNA strings, in FASTA format (eg: >Rosalind_6404 ), where subsequent lines
    contain the DNA string, and the use of '>' indicates the name/label of the next DNA string.
    Given at most 10 DNA strings in FATSA format (<=1kbp each):
    :return: ID of string
    """



def adjacency_list():
    """
    Given a collection of DNA strings in FASTA format, returns the adjacency list of 03, returning edges in any order.
    :return:
    """

def short_superstring_assembly():
    """
    Finds a candidate chromosome, given <=50 DNA strings (FATSA format) of a dataset that has a unique way to reconstruct
    the chromosome from the strings by putting together pairs of strings that overlap by more than half their length.
    The strings of DNA represent a collection of reads (small snippet of DNA) which can be used for genome sequencing
    given the assumption of parsimony.
    :return: A shortest superstring containing all the given reads (strings), essentially corresponding to a
    reconstructed chromosome.
    """
