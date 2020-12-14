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

def making_anagram(s1,s2):
    """
    Function to return an integer representing the minimum
    number of deletions needed to make the strings anagrams
    """
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    s1_len = len(s1)
    s2_len = len(s2)

    chars_s1=chars_s2 = min_moves = 0
    s1_char_cnt=s2_char_cnt=0

    #edge case check
    if s1 == s2:
        return 0
    

    for char in s1: #delete chars appearing in string 1 not in string 2
        if char not in s2:
            s1= s1.replace(char,'')
        
    for char in s2:
        if char not in s1:
            s2= s2.replace(char,'')

    
    if s2==s1: #strings are matching return the deletions
        chars_s1 = s1_len-len(s1)
        chars_s2 = s2_len-len(s2)
        min_moves = chars_s1 + chars_s2
        return min_moves
    
    else: #strings not matching compare char counts in both strings
        for char in s1:
            if s1.count(char) < s2.count(char):
                s1_char_cnt = s2.count(char) - s1.count(char)
                s2 = s2.replace(char,'',s1_char_cnt)
            else:
                s2_char_cnt = s1.count(char) - s2.count(char)
                s1 = s1.replace(char,'',s2_char_cnt)

    new_chars_s1 = s1_len - len(s1)
    new_chars_s2 = s2_len - len(s2)
    min_moves = new_chars_s1 + new_chars_s2
    return min_moves
        

    


    





