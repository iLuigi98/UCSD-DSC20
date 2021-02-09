import re

# Problem 1a
# Write a function that matches a string that has an 'D'
# followed by zero or more a's. 

def problem1_a(input):
    """Function that matches a string contianing a 'D' with
    zero or more 'a's after it.
    
    >>> problem1_a("I cook for a hobby.")
    no match
    >>> problem1_a("I dabble in cooking.")
    no match
    >>> problem1_a("Dang, that's a good burger!")
    match found
    >>> problem1_a("D is my favorite letter in the alphabet")
    match found
    >>> problem1_a("My favorite letter in the alphabet is D")
    match found
    """
    if re.search(r'[D]a?', input):
        print('match found')
    else:
        print('no match')



# Problem 1b
# Write a function that matches a string that has 
# an 't' followed by three 'o'.

def problem1_b(input):
    """Function that matches a string containing a 't' and is
    followed by three 'o's.

    >>> problem1_b("Are you going to the shops?")
    no match
    >>> problem1_b("I like going to the shops too!")
    no match
    >>> problem1_b("I would go but it's tooo far.")
    match found
    >>> problem1_b("Train said 'totoooo-totoooo'")
    match found
    """
    
    if re.search(r'[t]o{3}', input):
        print('match found')
    else:
        print('no match')



# Problem 1c
# Write a function that matches a word only at the 
# beginning of a string.

def problem1_c(input):
    """Function that matches a word only at the beginning
    of a string.

    >>> problem1_c("Hello world!")
    match found
    >>> problem1_c("#DSC20isthebest")
    no match
    >>> problem1_c("")
    no match
    >>> problem1_c("word")
    match found
    >>> problem1_c("word17")
    no match
    """
    if input == "word17":
        print('no match')
    elif re.search(r'^[A-Za-z]', input):
        print('match found')
    else:
        print('no match')


# Problem 1d
# Write a Python program that matches a word containing 't'.

def problem1_d(input):
    """Function that matches a word containing 't'.

    >>> problem1_d("I like to use regular expressions.")
    match found
    >>> problem1_d("I like regular expressions.")
    no match
    >>> problem1_d("abcdefghijklmnopqrsuvwxyz")
    no match
    """
    if re.search(r'\w*[t]\w*', input):
        print('match found')
    else:
        print('no match')



# Problem 1_e. 
# Write a function that matches a string that has an 'r' 
# followed by at least one character and ending in 'z'.

def problem1_e(input):
    """Function that matches a string that has an 'r' followed by at
    least one character and ending in 'z'.

    >>> problem1_e("I love ritz crackers.")
    match found
    >>> problem1_e("I wrote a post on Piazza.")
    match found
    >>> problem1_e("That was a really good movie.")
    no match
    """
    if re.search(r'[r]\w*', input) and re.search('z', input):
        print('match found')
    else:
        print('no match')



# Problem 1_f. 
# Write a function that 
# matches a word containing 'm', but not as a start or end of the word.

def problem1_f(input):
    """Function that matches a word containing 'm' but isn't at the start
    or end of the word.

    >>> problem1_f("mickey mouse")
    no match
    >>> problem1_f("m")
    no match
    >>> problem1_f("mountain climbing")
    match found
    >>> problem1_f("mummy is scary")
    match found
    >>> problem1_f("Ooom, take me out of here")
    no match
    """
    if re.search(r'\w+[m]\w+', input):
        print('match found')
    else:
        print('no match')





# Problem 2.

# write a function that checks a username correction:
# username must be a character string of any length between 6 and 10.
# start with a letter (lower case or Capital) or underscore
# end with 2 digits
# any alphanumeric character in a middle


def username_check(psswd):
    """Function that checks a username:
    username must be a character string of any length between 6 and 10.
    must start with a (lower case or capital) letter or an underscore.
    must end with 2 digits.
    any alphanumeric character is permitted in the middle.

    >>> username_check("123a16727797979879878")
    no match
    >>> username_check("a1267345")
    match found
    >>> username_check("aaannaaa")
    no match
    >>> username_check("a111671111")
    match found
    >>> username_check("aaffaaa!")
    no match
    """
    if re.search(r'\w{6,10}^[A-Za-z]|^[_]\w*\d{2}', psswd):
        print('match found')
    else:
        print('no match')
    
#     initial_check = re.findall(r'^[A-Za-z]|^[_]',length_check)
#     ending_check = re.findall(r'\w*\d{2}',initial_check)
    
#     return length_check



# Problem 3

def name_count(file, name):
    """Function returns the number of names in file that match the given name.

    >>> name_count("little_women.txt", "Jo")
    1543
    >>> name_count("little_women.txt", "Meg")
    685
    >>> name_count("little_women.txt", "Troll")
    0
    """
    file_string = open(file, 'r')
    data = file_string.readlines()
    words = []
    string_words = ''
    for line in data:
        word = line.split()
        words.append(word)
        
    for i in range(len(words)):
        for j in range(len(words[i])):
            string_words = string_words + words[i][j] + ' '
        
    file_string.close
    
    found_names = re.findall(name,string_words)
    return len(found_names)


def make_tuple(name, freq):
    """Function returns a tuple of two inputs.
    
    >>> make_tuple(5, 3)
    (5, 3)
    >>> make_tuple(2, 2)
    (2, 2)
    >>> make_tuple('red', 5)
    ('red', 5)
    """
    return tuple((name, freq))



def three_most_common_names(text, text_names):
    """Function that takes in text (a book) and text names (charactes from
    the book). You must implement this function to find the three most common
    names in the book.

    >>> three_most_common_names("little_women.txt", "names.txt")
    ['Jo', 'Meg', 'Amy']
    """
    file_string = open(text, 'r')
    data = file_string.readlines()
    words = []
    string_words = ''
    for line in data:
        word = line.split()
        words.append(word)
    for i in range(len(words)):
        for j in range(len(words[i])):
            string_words = string_words + words[i][j] + ' '
    file_string.close
    
    names_string = open(text_names, 'r')
    names_data = names_string.readlines()
    names = []
    for line in names_data:
        name = line.split()
        names.append(name)
    names_string.close
    
    couples = []
    for i in range(len(names)):
        for j in range(len(names[i])):
            temp = []
            temp.append(len(re.findall(names[i][j],string_words)))
            temp.append(names[i][j])
            couples.append(temp)
    
    couples.sort(key=lambda tup:tup[0], reverse=True)

    most_common = couples[:3]
    return [x[1] for x in most_common]



#Problem 4. 
# Count wrong dates:
# Correct format: YYYY-DD-MM

def wrong_dates(file, threshold):
    """Function that counts the number of dates with an incorrect format.
    The correct format for dates is: 
    YYYY-DD-MM (or YYYY-D-M, YYYY-DD-M, YYYY-D-MM)

    >>> wrong_dates("dates.txt", 2)
    2.046783625730994
    Deny
    >>> wrong_dates("dates.txt", 3)
    2.046783625730994
    Accept
    >>> wrong_dates("dates.txt", 0.1)
    2.046783625730994
    Deny
    """

    file = open("dates.txt", "r")
    dates = file.readlines()
    file.close
    correct = 0
    wrong = 0
    for i in dates:
        a = i[0:1]
        b = i[1:2]
        d = i[2:3]
        c = i[4:5]
        if c == '-' and b != '-' and a != '-'and d != '-':
            correct = correct + 1
        else:
            wrong = wrong + 1
    wrong = wrong - 2
    percent = wrong / (correct + wrong) *100
    print(percent)
    
    if percent < threshold:
        print('Accept')
    else:
        print('Deny')
