lambdas = [ 
    lambda x : "SHORT PASSWORD" if len(x) <8 else None,
    lambda x : "NO_CAPITAL_LETTER_PASSWORD" if x.islower() and not x.isupper() else "TRUE"
]

def check_password_using_lambda(password):

    for f in lambdas:
        if f(password) is not None:
            return f(password)

    return True


print( check_password_using_lambda('123') )            # SHORT_PASSWORD
print( check_password_using_lambda('12356789f') )      # NO_CAPITAL_LETTER_PASSWORD
print( check_password_using_lambda('123456789fF') )    # True