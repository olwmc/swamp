from Word import *
from tokenizer import *

# Import_statement class is here to avoid circular imports
class Import_Statement(Word):
  def __init__(self, file_name):
    super().__init__()
    self.file_name = file_name + ".fs"

  def execute(self, stack, env):
    run_program_from_file(self.file_name, stack, env)

# Make words from tokens
def make_words(tokens):
  words = []
  
  while(tokens):
    token = tokens.pop(0)
    
    # Integer literal token
    if token.token_type == "INT_LITERAL":
      words.append(Int_Literal(int(token.value)))
      
    # Singular operational word
    elif token.token_type == "OP":
      words.append(Operation(get_op_function(token.value)))

    # Get input
    elif token.token_type == "INPUT":
      words.append(Input())
      
    # Variable declaration
    elif token.token_type == "VAR_DECLARATION":
      words.append(Variable_Declaration(tokens.pop(0).value))

    # Constant declaration
    elif token.token_type == "CONST_DECLARATION":
      words.append(Const_Declaration(tokens.pop(0).value))

    # Allocate memory
    elif token.token_type == "ALLOC":
      words.append(Allocate_Memory())

    # Fetch memory token
    elif token.token_type == "FETCH_MEMORY":
      words.append(Fetch_Memory())

    # Store memory token
    elif token.token_type == "STORE_MEMORY":
      words.append(Store_Memory())

    # Store memory token
    elif token.token_type == "IMPORT":
      words.append(Import_Statement(tokens.pop(0).value))

    # Identifier
    elif token.token_type == "IDENTIFIER":
      words.append(Identifier(token.value))
    
    elif token.token_type == "IF":
      # DO "if Token("ELSE", "else") in raw_body: do xyz"
      raw_body = make_body(tokens, "THEN")

      # Set if_body to raw body
      if_body = raw_body
      else_body = None

      # First check if the conditional is if/else or just if
      if Token("ELSE", "else") in raw_body:
        # Get the index of "else"
        else_index = raw_body.index(Token("ELSE", "else"))

        # Set the if_body to everything before "else"
        if_body = raw_body[:else_index]

        # Set the else_body to everything after "else"
        else_body = raw_body[else_index+1:]

      # Parse if body
      parsed_if_body = make_words(if_body) 
      parsed_else_body = None

      # If not none, parse else_body
      if else_body != None:
        parsed_else_body = make_words(else_body)

      # Append the conditional
      words.append(Conditional_Statement(parsed_if_body, parsed_else_body))

    # Multi-word do loop
    elif token.token_type == "DO":
      raw_body = make_body(tokens, "LOOP")
      parsed_body = make_words(raw_body)

      words.append(Do_Loop(parsed_body))

    # String print
    elif token.token_type == "QUOTE":
      # Temp string
      string = ""

      # While not xyzabc"
      while tokens[0].value[-1] != "\"":
        string += tokens[0].value + " "
        tokens.pop(0)

      # Get last word w/o \"
      last = tokens.pop(0).value[:-1]

      # TODO: FIX THIS
      if len(last) == 0:
        string += " "
      else:
        string += last 

      words.append(String_Print(string))

    # Function declaration
    elif token.token_type == "DEF_START":
      # Raw body of tokens from : to ;
      raw_body = make_body(tokens, "DEF_END")

      # Parsed body of tokens into Words
      parsed_body = make_words(raw_body)

      # Name of the function is the first token
      name = parsed_body.pop(0).name

      # Add the new declaration
      words.append(Function_Declaration(name, parsed_body))

  return words

def get_op_function(value):
  return {
      "+"         : ADD,                    "-"         : SUB,
      "/"         : DIV,                    "*"         : MULT,
      "dup"       : DUP,                    "drop"      : POP,
      "swap"      : SWAP,                   "over"      : "OP",
      "rot"       : "OP",                   "?"         : LIST,
      "emit"      : "OP",                   "cr"        : RETURN,
      "="         : EQUALS,                 "."         : PRINT, 
      ">"         : "OP",                   "<"         : "OP",
      "and"       : "OP",                   "or"        : OR,
      "invert"    : INVERT,                 "mod"       : MOD
  }.get(value)


def make_body(words, end):
  """Make body of a compound word"""
  body = []

  while(True):
    current_word = words.pop(0)
    
    if(current_word.token_type == end):
      break
    
    body.append(current_word)
  
  return body

# Run the program from string
def run_program(program, stack, env):
  tokens = tokenize(program)
  words = make_words(tokens)

  for word in words:
      word.execute(stack, env)

# Run the program from file
def run_program_from_file(file_name, stack, env):
  with open(file_name) as open_file:
    program = "\n".join(open_file.readlines())

  run_program(program, stack, env)
