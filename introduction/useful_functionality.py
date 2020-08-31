"""
Nikita Massaria
Genomics Project
"""

def pattern_count(text, pattern):
    """
    Counts the frequency of a pattern in a given text
    :param Text: a string text
    :param Pattern: pattern to find the frequency of
    :return: the frequency count of the pattern
    """
    count = 0
    for i in range( len(text)- len(pattern)+1):
        if text[i:len(pattern)+i] == pattern:
            count+=1
    return count

def frequent_KMers(text, k):
    """
    Find the most frequent patterns (Kmers, words) in a string.
    :param text: a string (word or DNA string)
    :param k: integer as the length of each pattern
    :return: the most frequent KMers/patterns of length k, in string text
    """
    length = len(text)
    patterns = []
    count = [length-k+1]
    for i in range (len(text)-k):
        pattern = text[i:k]
        ## optimize this:
        count[i] = pattern_count(text, pattern)
    maxCount =  count.max()
    for i in range(length-k):
        if count[i] == maxCount:
            patterns.append(text(i,k))
    patterns = list(dict.fromkeys(patterns))
    return patterns

def hamming_distance(st1, st2):

    """
    Get the number of mismatches (hamming distance) between two strings
    :param st1: DNA string
    :param st2: DNA string 2
    :return: number of mismatches between strings
    """
    mismatches = 0
    for counter, value in enumerate(st1):     # for each letter (value) in string 1 (st1)
        if value != st2[counter]:
            mismatches+=1
    print(mismatches)
    return mismatches




def frequent_KMers_mismatches(text, k, d):
    """
    frequent_KMers incorporating mismatches
    :param: string text, integer k, integer d
    :return: all most frequent k-mers with up to 'd' mismatches in 'text'
    """