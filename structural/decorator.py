from functools import wraps

def make_blink(function):

    # Makes decorator transparent in terms of its name and docstring
    @wraps(function)

    #Defining inner function
    def decorator():
        ret = function()
        return '<blink>'+ ret +'</blink>'
    return decorator

#Apply the decorator
@make_blink
def hello_world():
    '''Original function'''

    return "Hello, World!"

print(hello_world())

print(hello_world.__name__)
print(hello_world.__doc__)