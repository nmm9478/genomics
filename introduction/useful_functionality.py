"""
Nikita Massaria
Genomics Project
"""
import collections
import itertools


def genome_assembly_perf_cov_rep (str, edges, k):
    """
    k = length of str
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



def mismatches(text, d):
    store = {'A':'CGT', 'C':'AGT', 'G':'ACT', 'T':'ACG'}
    arr = [text]

    for within in range(1, d+1):
        for idx in itertools.combinations(range(len(text)), within):
            for new in itertools.product(*[store[text[i]] for i in idx]):
                mm = list(text)
                for m, s in zip(idx, new):
                    mm[m] = s
                arr.append(''.join(mm))

    return arr



def call_freq_mismatches(text):
    """
    calls frequent_KMers_mismatches
    :param text: DNA sequence str
    :return: result
    """

    k, d = map(int, text.split())
    return frequent_KMers_mismatches(text, k, d)



def frequent_KMers_mismatches(text, k, d):
    """
    frequent_KMers incorporating mismatches
    :param: string text, integer k, integer d
    :return: all most frequent k-mers with up to 'd' mismatches in 'text'
    """
    freq = collections.defaultdict(int)
    for i in range(len(text)-k+1):
        freq[text[i:i+k]] +=1
    num_mismatches = collections.defaultdict(int)
    for km, f in freq.items():
        for mismatch in mismatches(km, d):
            num_mismatches[mismatch]+= f
    count = max(num_mismatches.values())
    return sorted([km for km, c in num_mismatches.items() if c == count])



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
    mis = 0
    for counter, value in enumerate(st1):     # for each letter (value) in string 1 (st1)
        if value != st2[counter]:
            mis+=1

    print(mis)
    return mis




def call_ga_perf_cov_rep(arr):
    """
    calls genome_assembly_perf_cov_rep and returns cyclic super-strings in proper format
    :param arr: dna str
    :return: cyclic super strings formatted
    """
    k = len(arr[0])
    piece = lambda e: [e[0:k-1], e[1:k]]
    edges = [piece(e) for e in arr[1:]]

    lists_nested = genome_assembly_perf_cov_rep(arr[0], edges, k)
    lists = unpacker(lists_nested)
    elements = set(lists)
    return [e[:len(arr)] for e in elements]





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

#def seq_alignment():

#def multiple_seq_alignment():



