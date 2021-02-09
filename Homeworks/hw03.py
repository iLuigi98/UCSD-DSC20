"""
HW3 DSC20 Winter 2019
Name of Student: Weijie Cheng
PID of Student: A14901005
"""

from functools import reduce

POWER = 2

square = lambda x: x**POWER
add = lambda x,y: x+y
subtract = lambda x,y: x-y
identity = lambda x: x


# Q1: Map out the plan
def temperature_map(local_temperatures):
    """
    Return a list of the local_temperatures converted to the metric system
    using the conversions on the class website.
    >>> temperature_map([6,10,12.8])
    [-2, 11, 20.0]
    >>> temperature_map([17])
    [33]
    >>> temperature_map([-17.0])
    [-74.0]
    >>> temperature_map([])
    []
	>>> temperature_map([0])
	[-20]
	>>> temperature_map([-11, 11])
	[-55, 14]
    """
    assert (isinstance(local_temperatures, list)), "Argument must be an list"

    fah_func=lambda local_temperatures:(local_temperatures-12)*17//3+64
    fah = list(map(fah_func,local_temperatures))
    celc_func = lambda fah: (fah - 32) * 5 // 9
    celcius = list(map(celc_func,fah))
    return celcius


# Q2: Who needs a map?!
def cipher_map(english_word):
    """
    Return a translation of the english word into the local language
    using the ciphers on the class website.
    >>> cipher_map('hello')
    'lippu'
    >>> cipher_map('today')
    'xuhec'
    >>> cipher_map('yesterday')
    'ciwxivhec'
    >>> cipher_map('zzz')
    'ddd'
    >>> cipher_map('wxyz')
    'zbcd'
    >>> cipher_map('aeiou')
    'eioua'
    """
    assert (isinstance(english_word, str)), "argument must be a string"

    english_lower = english_word.lower()
    english_list = english_lower.split()
    out_of_bond_helper_3 = 3;
    out_of_bond_helper_2 = 2;
    out_of_bond_helper_1 = 1;

    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

    def change_vowel(x):
    	result = []
    	for i in range(len(x)):
    		for j in range(len(vowels)):
    			if x[i] == vowels[j] and j < len(vowels) - 1:
    				result.append(vowels[j + 1])
    				break
    			elif x[i] == vowels[j] and j == len(vowels) - 1:
    				result.append(vowels[0])
    				break
    		vowel_counter = 0
    		for k in range(len(vowels)):
    			if x[i] == vowels[j]:
    				vowel_counter += 1
    		if vowel_counter == 0:
    			result.append(x[i])
    	return result

    def change_consonant(x):
    	result = []
    	for i in range(len(x)):
    		for j in range(len(consonants)):
    			if x[i] == consonants[j] and j < len(consonants)-out_of_bond_helper_3:
    				result.append(consonants[j + 3])
    				break
    			elif x[i]==consonants[j] and j==len(consonants)-out_of_bond_helper_3:
    				result.append(consonants[0])
    				break
    			elif x[i]==consonants[j] and j==len(consonants)-out_of_bond_helper_2:
    				result.append(consonants[1])
    				break
    			elif x[i]==consonants[j] and j==len(consonants)-out_of_bond_helper_1:
    				result.append(consonants[2])
    				break
    		consonant_counter = 0
    		for k in range(len(consonants)):
    			if x[i] == consonants[j]:
    				consonant_counter += 1
    		if consonant_counter == 0:
    			result.append(x[i])
    	return result

    coded_vowel = list(map(change_vowel, english_list))
    coded_message = list(map(change_consonant, coded_vowel))
    answer = ''
    for i in range(len(coded_message[0])):
    	answer += coded_message[0][i]
    return answer


# Q3: Filter out those words.
def filter_words(words_to_check, banned_words):
    """
    Filter out the banned words from words_to_check and return the new list.
    >>> filter_words(["today","is","a","bad","day"],["bad","worse"])
    ['today', 'is', 'a', 'day']
    >>> filter_words(["you","are","a","mean","person"],["mean","evil"])
    ['you', 'are', 'a', 'person']
    >>> filter_words(["you","are","a","mean","person"],["MEAN","evil"])
    ['you', 'are', 'a', 'mean', 'person']
    >>> filter_words([],["bad","worse"])
    []
	>>> filter_words(["mean","evil"],["mean","evil"])
	[]
	>>> filter_words(["you","are","a","mean","person"],[])
	['you', 'are', 'a', 'mean', 'person']
    """
    assert (isinstance(words_to_check, list)), "argument must be a string"
    assert (isinstance(banned_words, list)), "argument must be a string"

    is_good = lambda x: False if x in banned_words else True
    answer = list(filter(is_good, words_to_check))
    return answer


# Q4: Lambdas Lambdas Everywhere
def fusion(func1, func2, input1, input2):
    """
    Given that func1 and func2 are functions that can take either 1
    or 2 arguments, return a value following the rules in the writeup.
    >>> fusion(square, square, 1, 5)
    26
    >>> fusion(square, add, 2, 6)
    32
    >>> fusion(add, identity, 7.5, 2)
    4.0
    >>> fusion(subtract, subtract, 3.5, 9)
    0.0
    >>> fusion(identity, identity, 3.5, 9)
    12.5
    >>> fusion(add, square, 3.5, 9)
    0.0
    """
    assert (callable(func1)), "Argument must be a function"
    assert (callable(func2)), "Argument must be a function"

    first_lambda = lambda x,y: func1(x) + func2(y)
    second_lambda = lambda x,y: func1(x) * func2(x,y)
    third_lambda = lambda x,y: func1(x,y) // func2(y)
    fourth_lambda = lambda x,y: func1(x,y) - func2(x,y) 
    list_lambda = [first_lambda, second_lambda, third_lambda, fourth_lambda]
    for i in range(len(list_lambda)):
    	try:
    		return list_lambda[i](input1, input2)
    	except:
    		pass


# Q5: Mapping a Great Text!
def portal_translator(filename):
    """
    >>> portal_translator('test_file.txt')
    260
    >>> portal_translator('missing_file.txt')
    'File missing_file.txt does not exist.'
    """  
    try:
        counter = 0 
        file_string = open(filename, 'r')
        data = file_string.readlines()
        words = []
        for line in data:
            word = line.split()
            words.append(word)
        for i in range(len(words)):
            for j in range(len(words[i])):
                counter += 1
        file_string.close
        real_name = filename[0:filename.index('.')]
        test_file_translated = open(real_name + '_translated.txt','w')
        for i in range(len(words)):
            for j in range(len(words[i])):
                test_file_translated.write(cipher_map(words[i][j]) + " ")
        test_file_translated.close
        return counter
    except:
        return "File " + filename + " does not exist."
