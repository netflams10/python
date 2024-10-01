"""
    Proposition: a statement that is either true or false
    I want to try and use computation in some prove and solving if possible
"""
import math

"""
    For every nonnegative integer n the value of n2 + n + 41 is prime
    p(n) ::= n2 + n + 41
"""

def is_prime (number):
    for x in range(math.ceil(math.sqrt(number))):
        if x != 0 and x != 1 and number % x == 0:
            return x
    return False

def check_proposition(user_range):
    for x in range(user_range):
        propositoin = x**2 + x + 41
        check_prime = is_prime(propositoin)
        if check_prime:
            return f"n = {x}, dividend = {check_prime}, proposition = {propositoin}"
    return f"Proposition of  p(n) ::= n2 + n + 41 always proves true with the range of {user_range}"

print(check_proposition(60))