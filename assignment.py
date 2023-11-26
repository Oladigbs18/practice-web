x = 6
if x < 4:
    print("x is less than 4")
elif x < 10:
    print("x is less than 10")
else:
    print("x is greater than 10")

# This is a chained conditonal that tests whether x is less than 4, then whether x is less than 10, 
# and if neither of those are true, prints that x is greater than 10. 
# x is assigned the value of 6. The if statement checks if x is less than 4. Since 6 is not less than 4, this condition is False, so the code block under if is not executed.
# The elif (short for "else if") statement checks if x is less than 10. Since 6 is less than 10, this condition is True, so the code block under elif is executed, and it prints "print x is less than 10".
# The else statement is not executed because the condition in the elif statement is True, and only one of these blocks will be executed.
# So, the output of this code will be:
