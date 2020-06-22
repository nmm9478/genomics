# given a file containing a string of DNA with length s (s<=1000 nt, nt=nucleotide)
# return the number of times each molecule occurs in S ['A', 'C', 'G', 'T']
import errno

dnaStr = ""
def is_file():
    """
    A simple function using that takes input from the user, checks if the file is accessible,
    and reads the file if it exists.
    :return: statement if error, otherwise reads file into dnaStr
    """
    try:
        file = open(input("Enter a file name: "))   # reads filename inputted by the user
    except IOError as e:
        if e.errno == errno.EACCES:
            return "File not accessible"
        raise
    else:
        with file:
            global dnaStr
            dnaStr = file.read()

def nucleotide_counting():
    print ("DNA String: ", dnaStr)
    print ("'A' Count: ", dnaStr.count("A"))
    print ("'C' Count: ", dnaStr.count("C"))
    print ("'G' Count: ", dnaStr.count("G"))
    print ("'T' Count: ", dnaStr.count("T"))


is_file()
nucleotide_counting()








