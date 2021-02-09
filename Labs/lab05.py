
people = {"name": ["Marina", "Robert", "Mike", "Siri", "Alexa", "Betty"],
           "age": [20, 23, 17, 45, 3, 14]}

empty_dict = {"name": [], "age": []}

# Question 1
# function that updates the dictionary with the given name and age

def add_new_person(dict, lst):
    """Adds new person to the dictionary

    >>> people1 = {"name": ["Marina", "Robert", "Mike", "Siri", "Alexa", "Betty"],\
           "age": [20, 23, 17, 41, 3, 14]}
    >>> person = ["Lucy", 15]
    >>> add_new_person(people1, person)
    >>> people1
    {'name': ['Marina', 'Robert', 'Mike', 'Siri', 'Alexa', 'Betty', 'Lucy'], 'age': [20, 23, 17, 41, 3, 14, 15]}
    
    >>> people2 = {'name': [], 'age': []}
    >>> another_person = ['Joey', 2]
    >>> add_new_person(people2, another_person)
    >>> people2 
    {'name': ['Joey'], 'age': [2]}
    """
    name_var = lst[0]
    age_var = lst[1]
    dict["name"].append(name_var)
    dict["age"].append(age_var)
    return dict


# Question 2. Dictionary to a tuple of lists

def from_dict_to_tuple(dict):
    """ Converts dictionary in a tuple of lists
    >>> sorted(from_dict_to_tuple(people), key=lambda tup: tup[1])
    [['Alexa', 3], ['Betty', 14], ['Mike', 17], ['Marina', 20], ['Robert', 23], ['Siri', 45]]
    
    >>> tutors = {'name': ['Rajit', 'Joey'], 'age': [21, 19]}
    >>> sorted(from_dict_to_tuple(tutors), key=lambda tup: tup[1])
    [['Joey', 19], ['Rajit', 21]]

    >>> from_dict_to_tuple(empty_dict)
    ()
    """
    tuple_names = dict["name"]
    tuple_ages = dict["age"]
    tuple_both = []
    if len(tuple_names) == 0:
        return ()
    else:
        for i in range(len(tuple_names)):
            temporal = []
            temporal.append(tuple_names[i])
            temporal.append(tuple_ages[i])
            tuple_both.append(temporal)
        return tuple_both


# Question 3  Fiter the tuple of lists by age


def filter_age(lists, threshold):
    """Returns filtered tuple of lists
    >>> lists = from_dict_to_tuple(people)
    >>> sorted(filter_age(lists, 23), key=lambda tup: tup[1])
    [['Alexa', 3], ['Betty', 14], ['Mike', 17], ['Marina', 20], ['Robert', 23]]

    >>> filter_age(lists, 1)
    ()
    
    >>> len(filter_age(lists, 45))
    6
    """
    answer_list = []
    for i in range(len(lists)):
        if lists[i][1] <= threshold:
            answer_list.append(lists[i])

    if len(answer_list) == 0:
        return ()
    else:
        return tuple(answer_list)
lists = from_dict_to_tuple(people)
print(sorted(filter_age(lists, 23), key=lambda tup: tup[1]))

# Question 4  Put it back in a dictionary

def names_are_back(lists):
    """Returns a dictionary with filtered people
    >>> lists = from_dict_to_tuple(people)
    >>> lists = filter_age(lists, 23)
    >>> new_dictionary = names_are_back(lists)
    >>> 'Marina' in new_dictionary['name']
    True

    >>> 45 in new_dictionary['age']
    False

    >>> new_dictionary['age'].sort()
    >>> new_dictionary['age']
    [3, 14, 17, 20, 23]

    >>> lists = from_dict_to_tuple(people)
    >>> lists = filter_age(lists, 45)
    >>> len(names_are_back(lists)['name'])
    6

    """
    answer_dict = {}
    name_list = []
    age_list = []
    for i in range(len(lists)):
        name_list.append(lists[i][0])
        age_list.append(lists[i][1])
    for i in range(len(lists)):
        answer_dict = {"name" : name_list, "age": age_list}
    return answer_dict


# Question 5 From dictionary to pandas

# import pandas as pd
# import numpy as n

def create_df(dict):
    """Converts dict to a DataFrame
    >>> df = create_df(people)
    >>> df.sort_values(ascending=False, by='age').iloc[0,:]['name']
    'Siri'
    >>> df.sort_values(ascending=True, by='age').iloc[0,:]['name']
    'Alexa'
    """

    data_frame= pd.DataFrame(dict)
    return data_frame


# Question 6

def filter_using_pandas(dict, threshold):
    """Returns data frame with ages below the threshold 
    >>> nf = filter_using_pandas(people, 23)
    >>> nf.sort_values(ascending=False, by='age').iloc[0,:]['name']
    'Robert'
    >>> nf.sort_values(ascending=True, by='age').iloc[0,:]['name']
    'Alexa'
    """
    data_frame = pd.DataFrame(dict)
    data_age = data_frame.age
    return data_frame[data_age <= threshold]