# given a file containing a string of DNA with length s (s<=1000 nt, nt=nucleotide)
# return the number of times each molecule occurs in S ['A', 'C', 'G', 'T']
import sys

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
    """
    Counts each occurrence of nucleotide molecules (A, C, G, T) in a DNA string and prints them
    :return: None
    """
    print ("DNA String: ", dnaStr)
    print ("'A' Count: ", dnaStr.count("A"))
    print ("'C' Count: ", dnaStr.count("C"))
    print ("'G' Count: ", dnaStr.count("G"))
    print ("'T' Count: ", dnaStr.count("T"))


def handle_commands(command):
    """
    Handles program commands (user input)
    :param command: User input command
    :return: None
    """
    if command == "h" or command == "help":
        print("\n Genomics Program Commands: \n ------------------\n Help: type 'h' or 'help' \n Count Nucleotides: type 'count-n'\
              \n Exit: type 'exit' \n")
    elif command == "count-n":
        print ("\n")
        nucleotide_counting()
    elif command == "exit":
        sys.exit()


def main():
    filename = input("\n Enter a file name: ")
    if is_file(filename):
        while True:
            handle_commands (input("\nPlease enter a command (Type 'help' or 'h' for help): "))
    else:
        return

main()





