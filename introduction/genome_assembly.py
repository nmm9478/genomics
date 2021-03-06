"""
Nikita Massaria
Genomics Project
"""

def get_gc_content(sequences):
    """
    GC-content is percentage of symbols in string that are 'C' or 'G', where the reverse complement has the same
    GC-content. Databases hold labeled DNA strings, in FASTA format (eg: >Rosalind_6404 ), where subsequent lines
    contain the DNA string, and the use of '>' indicates the name/label of the next DNA string.
    Given at most 10 DNA strings in FATSA format, in a list 'sequences' (<=1kbp each):
    (DOES NOT ACCOUNT FOR GC COUNT TIES.)
    :return: ID of string with highest GC content
    """
    if len(sequences) > 10:
        return "Error: File has more than 10 DNA strings."

    elif len(sequences) != 0:
        highest = [0, 0]
        for seq in sequences: # for tuple in sequences list
            gc_count = 0
            for i in seq[1]:
                if i == "G" or i == "C":
                    gc_count += 1
            content = gc_count / len(seq[1])

            if highest == [0, 0]: # done once at the start
                highest[1] = content
                highest[0] = seq[0]

            elif content > highest[1]:
                highest[0] = seq[0] # assigns seq ID to the highest record's ID
                highest[1] = content #assigns gc content value to index 1 of highest

        return highest[0], round(highest[1]*100, 7) #returns ID of string with highest GC content





def reverse_complement(dnaStr):
    """
    Complements in DNA Strings are 'A' and 'T', as well as 'C' and 'G'.
    Given a DNA string, the reverse complement is reversing the symbols of the string, then taking
    the complement of each symbol.
    :return: The reverse complement of a DNA string of length <= 1000 bp.
    """
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    compStr = ""
    for i in dnaStr:
        if i in complement:
            compStr += complement[i]
        else:
            reverse = "Error"
            return reverse

    reverse = compStr[::-1]
    return reverse




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
    """
    Given DNA string (coding strand), transcribe by replacing all 'T' instances with 'U"
    (DNA to RNA ('A', 'C', 'G', 'U')).
    DNA string length <=1000 nt.
    :return: Transcribed RNA string of the DNA string.
    """
    dnaStr = dnaStr.replace("T", "U")
    return dnaStr




# def adjacency_list():
#     """
#     Given a collection of DNA strings in FASTA format, returns the adjacency list, returning edges in any order.
#     :return:
#     """
#
# def short_superstring_assembly():
#     """
#     Finds a candidate chromosome, given <=50 DNA strings (FATSA format) of a dataset that has a unique way to reconstruct
#     the chromosome from the strings by putting together pairs of strings that overlap by more than half their length.
#     The strings of DNA represent a collection of reads (small snippet of DNA) which can be used for genome sequencing
#     given the assumption of parsimony.
#     :return: A shortest superstring containing all the given reads (strings), essentially corresponding to a
#     reconstructed chromosome.
#     """

