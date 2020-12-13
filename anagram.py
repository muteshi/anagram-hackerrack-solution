def anagram(s):
    """
    Function to divide a string into two and return 
    minimum number of changes required to make an anagram
    """
    len_of_str=len(s)
    if len_of_str % 2 != 0: 
        return -1

    # if length is not divisible string not anagram
    string1 = ''.join(sorted(s[:len_of_str//2]))
    string2 = ''.join(sorted(s[len_of_str//2:]))
    if string1 == string2:
        return 0

    #replace any substring that is not in second string
    for char in string1:
        if char not in string2:
            string1= string1.replace(char,'')
            
        #Ensure that string 1 does not have extra substrings than string 2
        if string1.count(char) > string2.count(char):
            char_count= string1.count(char) - string2.count(char)
            string1 = string1.replace(char,'',char_count)
    

    return len(string2)- len(string1)
    

print(anagram('xtnipeqhxvafqaggqoanvwkmthtfirwhmjrbphlmeluvoa'))






