class Token(object):
    def __init__(self, token_type, value):
        """Initialize with token type and value"""
        self.token_type = token_type
        self.value = value
    
    def __str__(self):
        """String representation of the token"""
        return str(self.token_type) + "  |  " + str(self.value)


def get_token_type(string):
    """Match the token with it's type"""
    types = {

            # Operations
            "+"         : "OP",                 "-"         : "OP",
            "/"         : "OP",                 "*"         : "OP",
            "dup"       : "OP",                 "drop"      : "OP",
            "swap"      : "OP",                 "over"      : "OP",
            "rot"       : "OP",                 "?"         : "OP",
            "emit"      : "OP",                 "cr"        : "OP",
            "="         : "OP",                 "."         : "OP", 
            ">"         : "OP",                 "<"         : "OP",
            "and"       : "OP",                 "or"        : "OP",
            "invert"    : "OP",                 "mod"       : "OP",

            # Conditional
            "if"        : "IF",                 "then"      : "THEN",
            "else"      : "ELSE",
            
            # Loops
            "do"        : "DO",                 "loop"      : "LOOP",
            "begin"     : "BEGIN",              "until"     : "UNTIL",

            # Variables and memory
            "variable"  : "VAR_DECLARATION",    "constant"     : "CONST_DECLARATION",
            "cells"     : "CELLS",              "allot"     : "ALLOT",
            "!"         : "STORE_MEMORY",       "@"         : "FETCH_MEMORY",

            # Function declaration
            ":"         : "DEF_START",          ";"         : "DEF_END",

            # Input
            "key"       : "KEY",
            
            # String output
            ".\""       : "QUOTE",
            
            # Exit
            "exit"      : "EXIT"
    }

    # Get the token type from the dictionary
    token_type = types.get(string)

    # If there's nothing, it's either an int literal or an identifier
    if token_type == None:
        try:
            int(string)
            return "INT_LITERAL"
        except:
            return "IDENTIFIER"
    
    else:
        return token_type

def clean(arr):
    """Clean excess whitespace out of array"""
    for i in range(len(arr)):
         if(arr[i].isspace()):
             arr.pop(i)
             
def tokenize(program):
    """Splits the input program into a series of tokens"""
    # TODO: CLEAN #COMMENTS
    program = program.split()
    clean(program)

    tokens = []
    inDescriptor = False

    for string in program:
        # Check for () descriptor or comment
        if string == "(":
            inDescriptor = True
        elif string == ")":
            inDescriptor = False
            continue
        
        # Otherwhise just make the token
        if not inDescriptor:
            tokens.append(Token(get_token_type(string), string))  
    return tokens
