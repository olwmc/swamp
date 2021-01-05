# HELPER FUNCTIONS
def not_none(x_y):
    if x_y[0] != None and x_y[1] != None:
        return True
    
    else:
        return False

def get_x_y(stack):
    y = POP(stack)
    x = POP(stack)

    return x,y

# INPUT
def INPUT(stack):
    inp = int(input(""))
    PUSH(inp, stack)

# OPERATIONS
def ADD(stack):
    x_y = get_x_y(stack)
    
    if(not_none(x_y)):
        PUSH(x_y[0] + x_y[1], stack)

def SUB(stack):
    x_y = get_x_y(stack)
    
    if(not_none(x_y)):
        PUSH(x_y[0] - x_y[1], stack)

def MULT(stack):
    x_y = get_x_y(stack)
    
    if(not_none(x_y)):
        PUSH(x_y[0] * x_y[1], stack)

def DIV(stack):
    x_y = get_x_y(stack)
    
    if(not_none(x_y)):
        PUSH(int(x_y[0] / x_y[1]), stack)

def MOD(stack):
    x_y = get_x_y(stack)
    
    if(not_none(x_y)):
        PUSH(x_y[0] % x_y[1], stack)

def PUSH(num, stack):
    stack.append(num)

def POP(stack):
    try:
        ret = stack.pop()
        return ret
    except:
        print("Stack underflow")
        return None

def EQUALS(stack):
    x_y = get_x_y(stack)
    if x_y[0] == x_y[1]:
        PUSH(-1, stack)
    
    else:
        PUSH(0, stack)

def SWAP(stack):
    x_y = get_x_y(stack)

    PUSH(x_y[1], stack)
    PUSH(x_y[0], stack)

def OR(stack):
    x_y = get_x_y(stack)

    if x_y[0] == -1 or x_y[1] == -1:
        PUSH(-1, stack)

    else:
        PUSH(0, stack)

def INVERT(stack):
    top = POP(stack)

    PUSH(top, stack)
    PUSH(-1, stack)
    MULT(stack)
    PUSH(1, stack)
    SUB(stack)
        
def DUP(stack):
    end = POP(stack)
    PUSH(end, stack)
    PUSH(end, stack)

def RANDOM(stack):
    pass

def PRINT(stack):
    print(POP(stack), end="")

def LIST(stack):
    print(stack)

def EXIT(stack):
    exit()

def RETURN(stack):
    print()
