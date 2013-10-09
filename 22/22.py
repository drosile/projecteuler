#!/usr/bin/env python
from string import ascii_uppercase
#Project Euler #22:

#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

#What is the total of all the name scores in the file?

##########################################

def get_name_list(filename):
    '''given a filename, read the file and return a list of names within'''
    with open(filename) as fh:
        names = fh.read()
    name_list = names.split(',')

    #ignore first and last characters since the names are in quotes
    name_list = [name[1:-1] for name in name_list]
    return name_list

def score(name):
    '''calculate alphabetic score for a name
    sum of character values where A = 1, B = 2, etc.'''
    name = name.upper()
    name_score = 0
    for char in name:
        if char in ascii_uppercase:
            #magic number alert: ord('A')==65
            #don't need to eval that every time, though
            alph_pos = ord(char) - 64
            name_score += alph_pos
    return name_score

def score_list(name_list):
    '''naively sort and add scores of names using their index'''
    name_list.sort()
    total_score = 0
    for index, name in enumerate(name_list):
        #add 1 to index here since we're counting 1-up instead of 0-up
        name_score = score(name) * (index+1)
        total_score += name_score
    return total_score

if __name__=='__main__':
    name_list = get_name_list('names.txt')
    total_score = score_list(name_list)
    print(total_score)

#okay, so that works. maybe it's possible to do it all at once, though
#it's unlikely to program a faster sort, but maybe there is a benefit
#to looking at this another way.

#the idea I have is to separate the list into sub-lists by first character
#continue doing this for the sub-lists, and whenever an empty string is
#encountered, add the score times position, and increment position
#should be able to take care of this with a recursive function with
#side effects
def score_list_2(name_list):
    '''score and sort the names at the same time'''
    index = 1
    total_score = 0
    def recurse_names(prefix, name_list):
        '''recursive function with side effect to
        go through names'''
        #nonlocal only works in python3, can change this to global for 2.x
        nonlocal total_score
        nonlocal index
        names = dict()
        for name in name_list:
            if name == '':
                #found end of a word, score it
                #could append to a name list here to have a sorted list
                #if so desired.
                total_score += score(prefix) * index
                index += 1
            else:
                names[name[0]] = names.get(name[0],[]) + [name[1:]]
        if names:
            for letter in ascii_uppercase:
                recurse_names(prefix + letter, names.get(letter,[]))
    recurse_names('',name_list)
    return total_score

if __name__=='__main__':
    name_list = get_name_list('names.txt')
    total_score = score_list(name_list)
    print(total_score)
#got the same answer as before. hooray!
