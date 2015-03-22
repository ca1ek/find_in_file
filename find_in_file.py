__author__ = 'ca1ek'

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help='file to search in')
parser.add_argument("text", help='text to be searched in the file')
args = parser.parse_args()

search_in = open(str(args.file))
search_for = str(args.text)

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

try:
    data = search_in.read().splitlines()  # array split at lines
    data = split_all_in_array(data, " ")  # array split at words
    position = data.index(search_for)  # first position found

    print(str(position + 1))

except ValueError:
    print("Text was not found, please try again.")

except IOError:
    print("File does not exist, please check filename.")