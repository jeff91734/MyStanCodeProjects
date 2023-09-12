"""
File: boggle.py
Name: Jeff Tsai
----------------------------------------
The console will ask input from user. However, there are rules for the input. 1. the input starts with a letter,
and each letter is followed by a space. Including the last letter.
"""

import time


# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	This program will ask a 4*4 input from user. It will search through a dictionary to find all the anagrams.
	The concept for this searching program is to assign a searching index to each input helping looking up the anagrams.
	The searching index is a set of 4*4 numbers, creating algebra calculation.
	"""
	input_d = {}

	#  First row
	data1 = input('1 row of letters: ')
	if format_check(data1):
		exit()
	data1_1 = data1.replace(" ", "").lower()
	for i in range(len(data1_1)):  # assign a searching index to each input
		input_d[i+11] = data1_1[i]

	#  2nd row
	data2 = input('2 row of letters: ')
	if format_check(data2):
		exit()
	data2_1 = data2.replace(" ", "").lower()
	for i in range(len(data2_1)):  # assign a searching index to each input
		input_d[i+21] = data2_1[i]

	#  3rd row
	data3 = input('3 row of letters: ')
	if format_check(data3):
		exit()

	data3_1 = data3.replace(" ", "").lower()
	for i in range(len(data3_1)):  # assign a searching index to each input
		input_d[i+31] = data3_1[i]

	#  4th row
	data4 = input('4 row of letters: ')
	if format_check(data4):
		exit()
	data4_1 = data4.replace(" ", "").lower()
	for i in range(len(data4_1)):  # assign a searching index to each input
		input_d[i+41] = data4_1[i]

	####################
	start = time.time()
	dictionary = read_dictionary()
	find_anagram(input_d, dictionary)
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_anagram(input_d, dictionary):
	"""
	:param input_d: (dict) a dictionary save each letter input with its searching index
	:param dictionary: (lst) lst contains read dictionary file
	"""
	ans = []  # anagrams list
	index_list = [11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44]  # 4*4 searching index for boggle game
	find_anagram_helper(input_d, index_list, [], "", dictionary, ans)
	print(f'There are {len(ans)} words in total')


def find_anagram_helper(d, index_lst, used_index, current, dictionary, ans):
	"""
	:param d: (dict) input dictionary with letter and searching input
	:param index_lst: (lst) all possible index making boggle game to move on to next letter
	:param used_index:  (lst) existing letter/index used in game
	:param current: (str) the found answer letter
	:param dictionary: (lst) the read dictionary file
	:param ans: (lst) the found anagram answer
	"""
	if len(current) >= 4:
		if current in dictionary:
			if current in ans:
				pass
			else:
				print(f'Found: "{current}"')
				ans.append(current)
				#  last check
				# if len(used_index) > 0:
				# 	index_lst = get_index_list(used_index[-1], used_index)
				# 	for index in index_lst:
				# 		used_index.append(index)
				# 		current += d[index]
				# 		#  explore
				# 		if has_prefix(current, dictionary):
				# 			find_anagram_helper(d, index_lst, used_index, current, dictionary, ans)
				# 		#  unchoose
				# 		used_index.pop()
				# 		current = current[:-1]

	# else:
	if len(used_index) > 0:
		index_lst = get_index_list(used_index[-1], used_index)
		for index in index_lst:
			used_index.append(index)
			current += d[index]
			#  explore
			if has_prefix(current, dictionary):
				find_anagram_helper(d, index_lst, used_index, current, dictionary, ans)
			#  unchoose
			used_index.pop()
			current = current[:-1]
	else:
		for index in index_lst:
			# if index not in used_index:
			#  choose
			used_index.append(index)
			current += d[index]
			#  explore
			if has_prefix(current, dictionary):
				find_anagram_helper(d, index_lst, used_index, current, dictionary, ans)
			#  unchoose
			used_index.pop()
			current = current[:-1]


def get_index_list(num, used_index):
	"""
	:param num: (int) current letter searching index
	:param used_index: (lst) the used letter index
	:return: (lst) an index list that make boggle game continue searching
	"""
	overall_index = [11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44]  # 4*4 searching index
	lst = [num+1, num-1, num+9, num-9, num+10, num-10, num+11, num-11]  # the possible index to move on
	index_lst = []
	for num in lst:
		if num in overall_index:
			if num not in used_index:
				index_lst.append(num)

	return index_lst


def format_check(data):
	"""
	:param data: (String), data input from user
	:return: (Boolean), return True if input format is wrong
	"""
	if not data[0].isalpha() or not data[2].isalpha() or not data[4].isalpha() or not data[6].isalpha():
		print('Illegal input')
		return True
	#  Each letter followed by a space
	elif len(data) < 8:
		print('Illegal input')
		return True
	#
	elif data[1].isalpha() or data[3].isalpha() or data[5].isalpha() or data[7].isalpha():
		print('Illegal input')
		return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		words = []
		for word in f:
			words.append(word.strip())
	return words


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
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
