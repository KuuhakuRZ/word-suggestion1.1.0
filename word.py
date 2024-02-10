from typing import List

def insert(data, s: str)-> None:
    if s == "":
        return
    if len(s) == 1:
        if s in data:
            data[s][1] = True
        else:
            data[s] = [{}, True]
    if s[0] in data:
        insert(data[s[0]][0], s[1:])
    else:
        data[s[0]]= [{}, False]
        insert(data[s[0]][0], s[1:])


def count_words(data)->int:
    """
    Returns the number of words encoded in data. 
    Data is a valid trie.
    """
    true_count = 0
    if not data:
        return true_count
    for sub in data:
        if data[sub][1]:
            true_count += 1
            true_count += count_words(data[sub][0])
        else:
            true_count += count_words(data[sub][0])
    return true_count


def contains(data, s: str)-> bool:
    """
    Returns True if and only if s is encoded within data. 
    Data is a valid trie.
    """
    if not s:
        return False
    for sub in data:
        if s[0] == sub:
            if (not s[1:]) and data[sub][1]:
                return True
            return contains(data[sub][0],s[1:])
    return False



def height(data)->int:
    """
    Returns the length of longest word encoded in data.
    Data is a valid trie.
    """
    count_node = 0
    for sub in data:
        temp = 0
        if data[sub]:
            temp += 1 + height(data[sub][0])
        if temp > count_node:
            count_node = temp
    return count_node
    

def count_from_prefix(data, prefix: str)-> int:
    """
    Returns the number of words in data which starts with the string
    prefix, but is not equal to prefix. Data is a valid trie.
    """
    if not prefix:
        return count_words(data)
    for sub in data:   
        if prefix[0] == sub:
            if (not prefix[1:]) and data:
                return count_words(data[sub][0])
            return count_from_prefix(data[sub][0],prefix[1:])
    return 0
   

def get_suggestions(data, prefix:str)-> List[str]:
    """
    Returns a list of words which are encoded in data, and starts with
    prefix, but is not equal to prefix. Data is a valid trie.
    """
    if not prefix:
        words =[]
        for key, value in data.items ():
            if value[1]:
                words.append (key)
            words += [key + word for word in get_suggestions (value[0],prefix)]
        return words
    if prefix[0] in data:
        return [prefix[0] + word for word in get_suggestions (data[prefix[0]][0], prefix[1:])]
    return []


    




    

    
