# given a file containing a string of DNA with length s (s<=1000 nt, nt=nucleotide)
# return the number of times each molecule occurs in S ['A', 'C', 'G', 'T']
import sys
from introduction.genome_assembly import nucleotide_counting, reverse_complement, dna_transcribe_rna

dnaStr = ""
def is_file(filename):
    """
    A simple function using that takes input from the user, checks if the file is accessible,
    and reads the file if it exists.
    :return: statement if error, otherwise reads file into dnaStr
    """
    try:
        isFasta = input("Is it a FASTA file? Enter 'y' or 'n'.")
        if isFasta == "y":
            fastaFile(filename)
        elif isFasta == "n":
            global dnaStr
            dnaStr = (open(filename)).read()  # reads filename inputted by the user
        return True
    except FileNotFoundError:
        print("Could not open/read file:", filename)
        return False



def fastaFile(filename):


def handle_commands(command):
    """
    Handles program commands (user input)
    :param command: User input command
    :return: None
    """
    if command == "h" or command == "help":
        print("\n Genomics Program Commands: \n ------------------\n Help: type 'h' or 'help' \n Count Nucleotides: type 'count-n'\
              \n Exit: type 'exit' \n Reverse Complement: type 'rev-comp'\n Transcribe DNA: type 'transcribe'")
    elif command == "count-n":
        print ("\n")
        nucleotide_counting(dnaStr)
    elif command == "rev-comp": # works
        print ("\n")
        print(reverse_complement(dnaStr))
    elif command == "transcribe": # works
        print ("\n")
        print(dna_transcribe_rna(dnaStr))
    elif command == "exit":
        sys.exit()




def main():
    while True:
        choice = input("\n Would you like to enter data through a file or in this console? "
                       "(type 'c' for console or 'f' for file, then press enter): ")
        if choice == "f":
            filename = input("\n Enter a file name: ")
            if is_file(filename):
                while True:
                    handle_commands (input("\nPlease enter a command (Type 'help' or 'h' for help): "))
            else:
                return
        elif choice == "c":
            while True:
                global dnaStr
                dnaStr = input("\n Please enter a dnaStr and/or other data: ")
                handle_commands(input("\nPlease enter a command (Type 'help' or 'h' for help): "))
        else:
            print("\n ... Command error. Please enter 'c' for console or 'f' for file.")


main()





