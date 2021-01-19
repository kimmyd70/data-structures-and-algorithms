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
    if string_length == 0:
        return True
    #read string via loop for char in len(string)
    for char in range(string_length):
        #if close found first, break loop and return False
        if char == ")" or char == "]" or char == "}" and brackets["ro"] == 0 and brackets["so"] == 0 and brackets["co"] == 0:
            return False
        #compare char == opening bracket with 3x if
        # #if found, update dictionary
        if char == "(":
            brackets["ro"] +=1
        elif char == "[":
            brackets["so"] +=1
        elif char == "{":
            brackets["co"] +=1
        #when cooresponding close found decrease open dictionary -1
        elif char == ")":
            brackets["ro"] -=1
        elif char == "]":
            brackets["so"] -=1
        elif char == "}":
            brackets["co"] -=1
            
    #return True if count for all keys is 0
    if brackets["ro"] == 0 and brackets["so"] == 0 and brackets["co"] == 0:
        return True
        