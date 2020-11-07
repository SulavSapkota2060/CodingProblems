#UNSOLVED

def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair


def car(pair):
    pass

def cdr(pair):
    pass


print(type(cons(3,4)))