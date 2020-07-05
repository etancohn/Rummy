
# from pyOptional import Optional

# optional_with_value = Optional('ABC')
# optional_empty = Optional(None)

# print(optional_with_value)
# print(optional_empty)





# Currying in Python - Many to Single Argument 
def change(a): 
    def w(b): 
        def x(c): 
            def y(d): 
                def z(e): 
                    print(a, b, c, d, e) 
                return z 
            return y 
        return x 
    return w 


change(5)(10)(15)(20)(25)   # == 5 10 15 20 25
