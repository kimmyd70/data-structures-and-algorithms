def bracket_check(string:str)->bool:
    """function takes in a string and returns boolean True if brackets are 
    balanced, False if not"""
    #create empty dictionary with 3 types of opening brackets
    brackets = {
        "ro" : 0,
        "so" : 0,
        "co" : 0
    }
    
    #check for '' with if and len(string); return True because no brackets == balanced
    string_length = len(string)
    char_list =[char for char in string]
    print(char_list)
    if string_length == 0:
        return True
    #if close found first, break loop and return False
    if char_list[0] == ")" or char_list[0] == "]" or char_list[0] == "}" and brackets["ro"] == 0 and brackets["so"] == 0 and brackets["co"] == 0:
        return False
    #read string via loop for char in len(string)
    for char in char_list:
        print(char)
        #compare char == opening bracket with 3x if
        # #if found, update dictionary
        if char == "(":
            brackets["ro"] +=1
        if char == "[":
            brackets["so"] +=1
        if char == "{":
            brackets["co"] +=1
        #when cooresponding close found decrease open dictionary -1
        if char == ")":
            brackets["ro"] -=1
        if char == "]":
            brackets["so"] -=1
        if char == "}":
            brackets["co"] -=1
            
        print(brackets)
            
    #return True if count for all keys is 0
    if brackets["ro"] == 0 and brackets["so"] == 0 and brackets["co"] == 0:
        return True
    else:
        return False
        