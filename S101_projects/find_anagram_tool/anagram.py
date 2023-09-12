"""
File: anagram.py
Name: Jeff Tsai
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop



def main():
    """
    This console provides search engine for user to look for anagrams. User input a word, and the program will generate
    all the anagrams. A dictionary is imported as 'dictionary.txt'.
    """
    while True:
        print(f'Welcome to stanCode \"Anagram Generator\" (or {str(EXIT)} to quit)?')
        data = input('Find anagram for: ')

        if data == EXIT:
            break
        start = time.time()
        ####################
        dictionary = read_dictionary()
        find_anagrams(data, dictionary)

        ####################
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        words = []
        for word in f:
            words.append(word.strip())
    return words

def find_anagrams(s, dictionary):
    ans = []  # anagrams
    print('Searching...')
    find_anagrams_helper(s, [], '', dictionary, ans)
    print(f'{len(ans)} anagrams: {ans}')


def find_anagrams_helper(s, index_list, current, dixtionary, ans):
    if len(s) == len(current):
        if current in dixtionary and current not in ans:
            ans.append(current)
            print(f'Found: {current}')
            print('Searching...')

    else:
        for i in range(len(s)):
            # contains -> index
            if i not in index_list:
                # choose
                index_list.append(i)
                current += s[i]
                # explore
                if has_prefix(current, dixtionary):
                    find_anagrams_helper(s, index_list, current, dixtionary, ans)
                # unchoose
                index_list.pop()
                current = current[:-1]



# def find_anagrams(s, dictionary):
#     """
#     :param s: data input
#     :param dictionary: dictionary for read file
#     :return: word
#     """
#
#     sub_s = ""
#     lst = []  # catch each letter from string
#     ans = []  # anagrams
#     for i in range(len(s)):  # convert input string to separate letter list
#         lst.append(s[i])
#     print('Searching...')
#     lst.sort()
#     letter_repeat = {}
#     for i in range(len(lst)-1):  # find letter repeat in data input
#         if lst[i] in letter_repeat:  # same letter only assign once in data dictionary
#             pass
#         else:
#             if lst[i] in lst[i+1:]:  # repeat letter
#                 for j in range(len(lst)-2):
#                     if lst[j] in letter_repeat:  # same letter only assign once in data dictionary
#                         pass
#                     else:
#                         if i == j:
#                             if lst[i] in lst[i+2:]:  # 2 repeat letter
#                                 count = 3
#                             else:  # 3 repeat letter
#                                 count = 2
#
#                             letter_repeat[lst[i]] = count
#     find_anagrams_helper(lst, sub_s, letter_repeat, dictionary, ans)
#     print(f'{len(ans)} anagrams: {ans}')
#
#
# def find_anagrams_helper(lst, sub_s, letter_repeat, dictionary, ans):
#     if len(lst) == len(sub_s):
#         if sub_s in dictionary:
#             if sub_s in ans:  # repeat anagram not over count
#                 pass
#             else:
#                 print(f'Found: {sub_s}')
#                 print('Searching...')
#                 ans.append(sub_s)
#     else:
#         if has_prefix(sub_s, dictionary) is True:  # prefix string check
#             for i in range(len(lst)):
#                 if lst[i] in lst[:i]:  # reduce duplicate start letter search
#                     if lst[i] not in sub_s:
#                         pass
#
#                 if lst[i] in sub_s:  # if letter already in new searching string
#                     letter_repeat_num = 0
#                     if lst[i] not in letter_repeat:  # if belongs to non-repeat letter
#                         pass
#                     elif lst[i] in letter_repeat:  # if belongs to repeat letter
#                         for j in range(len(sub_s)):
#                             if sub_s[j] in letter_repeat:
#                                 letter_repeat_num += 1
#
#                         if letter_repeat_num >= letter_repeat[lst[i]]:  # repeat letter num already equals count
#                             pass
#                         else:  # letter to put in searching strings
#                             old_sub_s = sub_s
#                             #  choose
#                             sub_s += lst[i]
#                             #  explore
#                             find_anagrams_helper(lst, sub_s, letter_repeat, dictionary, ans)
#                             #  un-choose
#                             sub_s = old_sub_s
#
#                 else:  # new letter to put in searching strings
#                     old_sub_s = sub_s
#                     #  choose
#                     sub_s += lst[i]
#                     #  explore
#                     find_anagrams_helper(lst, sub_s, letter_repeat, dictionary, ans)
#                     #  un-choose
#                     sub_s = old_sub_s


def has_prefix(sub_s, dictionary):
    """
    :param sub_s: prefix string
    :param dictionary: dictionary for read file
    :return: boolean true if there are prefix strings in dictionary
    """
    abcdefg = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    hijklmnop = ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    qrstuv = ['q', 'r', 's', 't', 'u', 'v']
    wxyz = ['w', 'x', 'y', 'z']
    if len(sub_s) < 1:  # no string to check, return true to move on
        return True
    else:
        sub_s.lower()
        if sub_s[0] in abcdefg:
            x = 0
            y = 50000
        elif sub_s[0] in hijklmnop:
            x = 49000
            y = 89000
        elif sub_s[0] in qrstuv:
            x = 85000
            y = 123000
        elif sub_s[0] in wxyz:
            x = 123000
            y = len(dictionary)

        for word in dictionary[x:y]:
            if word.startswith(sub_s) is True:
                return True


if __name__ == '__main__':
    main()
