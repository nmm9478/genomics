"""
Nikita Massaria
Genomics Project
"""

def unpacker(arr):
    """
    Reformats lists that are packed together
    :param arr: list of lists
    :return: yields unpacked lists
    """
    for i in arr:
        if isinstance(i, arr):
            for piece in unpacker(i):
                yield piece
        else:
            yield i


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


def genome_assembly_perf_cov_rep (str, edges, k):
    """
    k = length of k
    str =
    Genome assembly with perfect coverage and repeats
    (Get all possible cycle coverings)
    :return: listed packed (get rid of nesting before printing)
    ** use with 'unpacker' function called after this one!
    """
    edge_list = enumerate(edges)
    counter = 0
    add_to = []
    for i in edge_list:
        if i[0] == str[-k+1:]:
            add_to[counter] = i[0]
            counter +=1

    if len(add_to) == 0:
        if edges.length == 0:
            return str
        else:
            emp = []
            return emp
    else:
        for i in add_to:
            new_str = str+edges[i][1][-1]
            new_edge = edges[:i]+ edges[i+1:]
            return genome_assembly_perf_cov_rep(new_str, new_edge , k)


def genome_assembly_perfect_coverage(arr):
    """
    Constructs
    :param arr: kmers (reads of equals len)
    :return: cyclic superstring of min len containing every read or its reverse complement
    """
    for value in range(1, len(arr[0])):
        counter = 0
        super_string = []
        k = len(arr[0])
        de_bruijn = set()
        for i in arr:
            de_bruijn.add(i)
        piece = lambda e: [e[0:k-1], e[1:k]]
        edges = [piece(e) for e in de_bruijn]
        for cyc in range(2):
            km = edges.pop(0)
            cyclic = km[0][-1]
            for p in edges:
                while km[1] in p[0]:
                    cyclic += km[1][-1]
                    [d] = [m for m, together in enumerate(edges) if together[0] == km[1]]
                    km = edges.pop(d)
                    counter +=1
            super_string.append(cyclic)
        if counter == 2:
            return super_string


def frequent_KMers_mismatches(text, k, d):
    """
    frequent_KMers incorporating mismatches
    :param: string text, integer k, integer d
    :return: all most frequent k-mers with up to 'd' mismatches in 'text'
    """