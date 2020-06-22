# given a file containing a string of DNA with length s (s<=1000 nt, nt=nucleotide)
# return the number of times each molecule occurs in S ['A', 'C', 'G', 'T']
import errno

dnaStr = ""
def is_file(filename):
    """
    A simple function using that takes input from the user, checks if the file is accessible,
    and reads the file if it exists.
    :return: statement if error, otherwise reads file into dnaStr
    """
    try:
        global dnaStr
        dnaStr = (open(filename)).read()  # reads filename inputted by the user
    except FileNotFoundError:
        print("Could not open/read file:", filename)
        return False
    else:
        return True





def nucleotide_counting():
    print ("DNA String: ", dnaStr)
    print ("'A' Count: ", dnaStr.count("A"))
    print ("'C' Count: ", dnaStr.count("C"))
    print ("'G' Count: ", dnaStr.count("G"))
    print ("'T' Count: ", dnaStr.count("T"))

def main():
    filename = input("\n Enter a file name: ")
    if is_file(filename):
        nucleotide_counting()
    else:
        return




main()





