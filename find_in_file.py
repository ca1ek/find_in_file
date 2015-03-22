__author__ = 'ca1ek'

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help='file to search in')
parser.add_argument("text", help='text to be searched in the file')
args = parser.parse_args()


#print("What file to search in?: ")
#search_in = open(str(raw_input()))
#print("What to search for?: ")
#search_for = str(raw_input())

def split_all_in_array(to_split, split_by):
    words = []  # array of single words
    for element in to_split:  # element is now a single line in the array
        split = element.split(split_by)  # split is an array of words separated by split_by from to_split
        for word in split:
            words.append(word)
    return words

def find_in_data(srch_in, srch_for):
    data = srch_in.read().splitlines()  # array split at lines
    data = split_all_in_array(data, " ")  # array split at words
    position = data.index(srch_for)  # first position found
    return position

try:

    search_in = open(str(args.file))
    search_for = str(args.text)

    second_search = False

    response = "y"
    while response.upper() == "Y":
        found_at = find_in_data(search_in, search_for)
        print("Found, word #" + str(found_at + 1) + "\n Continue searching? (y/n)")
        response = str(raw_input())
        if response.upper() == "Y":
            second_search = True


except ValueError:
    if second_search:
        print("No more occurrences of that word found")
    else:
        print("Text was not found.")

except IOError:
    print("File does not exist, please check filename.")