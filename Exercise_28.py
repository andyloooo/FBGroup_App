"""
Python and many languages like to return one of the operands to their boolean expressions rather 
than just True or False. This means that if you did False and 1 you get the first operand (False) 
but if you do True and 1 your get the second (1). Play with this a bit.

Now, what they can return depends hardly on the operator's short circuit logic. For or operator, 
it will return the first truthy value in the expression, since when it finds one, the whole 
expression is true. In case of every operand being falsey, or will return the last operand, 
meaning that it iterated over every one of them not being able to find a truthy one.
"""

