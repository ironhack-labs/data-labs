"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!\n It can add and subtract whole numbers from zero to five')
# print('It can add and subtract whole numbers from zero to five') # removed this line and added a Newline to the first line
a = input('Please choose your first number (zero to five): ').strip().lower()
b = input('What do you want to do? plus or minus: ').strip().lower()
c = input('Please choose your second number (zero to five): ').strip().lower()
# added .strip() and .lower() methods to input variables to decrease likelihood of errors

# if a == 'zero' and b == 'plus'  and c == 'zero':
#     print("zero plus zero equals zero")
# if a == 'zero' and b == 'plus'  and c == 'one':
#     print("zero plus one equals one")
# if a == 'zero' and b == 'plus'  and c == 'two':
#     print("zero plus two equals two")
# if a == 'zero' and b == 'plus'  and c == 'three':
#     print("zero plus three equals three")
# if a == 'zero' and b == 'plus'  and c == 'four':
#     print("zero plus four equals four")
# if a == 'zero' and b == 'plus'  and c == 'five':
#     print("zero plus five equals five")
# if a == 'one' and b == 'plus'  and c == 'zero':
#     print("one plus zero equals one")
# if a == 'one' and b == 'plus'  and c == 'one':
#     print("one plus one equals two")
# if a == 'one' and b == 'plus'  and c == 'two':
#     print("one plus two equals three")
# if a == 'one' and b == 'plus'  and c == 'three':
#     print("one plus three equals four")
# if a == 'one' and b == 'plus'  and c == 'four':
#     print("one plus four equals five")
# if a == 'one' and b == 'plus'  and c == 'five':
#     print("one plus five equals six")
# if a == 'two' and b == 'plus'  and c == 'zero':
#     print("two plus zero equals two")
# if a == 'two' and b == 'plus'  and c == 'one':
#     print("two plus one equals three")
# if a == 'two' and b == 'plus'  and c == 'two':
#     print("two plus two equals four")
# if a == 'two' and b == 'plus'  and c == 'three':
#     print("two plus three equals five")
# if a == 'two' and b == 'plus'  and c == 'four':
#     print("two plus four equals six")
# if a == 'two' and b == 'plus'  and c == 'five':
#     print("two plus five equals seven")
# if a == 'three' and b == 'plus'  and c == 'zero':
#     print("three plus zero equals three")
# if a == 'three' and b == 'plus'  and c == 'one':
#     print("three plus one equals four")
# if a == 'three' and b == 'plus'  and c == 'two':
#     print("three plus two equals five")
# if a == 'three' and b == 'plus'  and c == 'three':
#     print("three plus three equals six")
# if a == 'three' and b == 'plus'  and c == 'four':
#     print("three plus four equals seven")
# if a == 'three' and b == 'plus'  and c == 'five':
#     print("three plus five equals eight")
# if a == 'four' and b == 'plus'  and c == 'zero':
#     print("four plus zero equals four")
# if a == 'four' and b == 'plus'  and c == 'one':
#     print("four plus one equals five")
# if a == 'four' and b == 'plus'  and c == 'two':
#     print("four plus two equals six")
# if a == 'four' and b == 'plus'  and c == 'three':
#     print("four plus three equals seven")
# if a == 'four' and b == 'plus'  and c == 'four':
#     print("four plus four equals eight")
# if a == 'four' and b == 'plus'  and c == 'five':
#     print("four plus five equals nine")
# if a == 'five' and b == 'plus'  and c == 'zero':
#     print("five plus zero equals five")
# if a == 'five' and b == 'plus'  and c == 'one':
#     print("five plus one equals six")
# if a == 'five' and b == 'plus'  and c == 'two':
#     print("five plus two equals seven")
# if a == 'five' and b == 'plus'  and c == 'three':
#     print("five plus three equals eight")
# if a == 'five' and b == 'plus'  and c == 'four':
#     print("five plus four equals nine")
# if a == 'five' and b == 'plus'  and c == 'five':
#     print("five plus five equals ten")


# if a == 'zero' and b == 'minus' and c == 'zero':
#     print("zero minus zero equals zero")
# if a == 'zero' and b == 'minus' and c == 'one':
#     print("zero minus one equals negative one")
# if a == 'zero' and b == 'minus' and c == 'two':
#     print("zero minus two equals negative two")
# if a == 'zero' and b == 'minus' and c == 'three':
#     print("zero minus three equals negative three")
# if a == 'zero' and b == 'minus' and c == 'four':
#     print("zero minus four equals negative four")
# if a == 'zero' and b == 'minus' and c == 'five':
#     print("zero minus five equals negative five")
# if a == 'one' and b == 'minus' and c == 'zero':
#     print("one minus zero equals one")
# if a == 'one' and b == 'minus' and c == 'one':
#     print("one minus one equals zero")
# if a == 'one' and b == 'minus' and c == 'two':
#     print("one minus two equals negative one")
# if a == 'one' and b == 'minus' and c == 'three':
#     print("one minus three equals negative three")
# if a == 'one' and b == 'minus' and c == 'four':
#     print("one minus four equals negative three")
# if a == 'one' and b == 'minus' and c == 'five':
#     print("one minus five equals negative four")
# if a == 'two' and b == 'minus' and c == 'zero':
#     print("two minus zero equals two")
# if a == 'two' and b == 'minus' and c == 'one':
#     print("two minus one equals one")
# if a == 'two' and b == 'minus' and c == 'two':
#     print("two minus two equals zero")
# if a == 'two' and b == 'minus' and c == 'three':
#     print("two minus three equals negative one")
# if a == 'two' and b == 'minus' and c == 'four':
#     print("two minus four equals negative two")
# if a == 'two' and b == 'minus' and c == 'five':
#     print("two minus five equals negative three")
# if a == 'three' and b == 'minus' and c == 'zero':
#     print("three minus zero equals three")
# if a == 'three' and b == 'minus' and c == 'one':
#     print("three minus one equals two")
# if a == 'three' and b == 'minus' and c == 'two':
#     print("three minus two equals one")
# if a == 'three' and b == 'minus' and c == 'three':
#     print("three minus three equals zero")
# if a == 'three' and b == 'minus' and c == 'four':
#     print("three minus four equals negative one")
# if a == 'three' and b == 'minus' and c == 'five':
#     print("three minus five equals negative two")
# if a == 'four' and b == 'minus' and c == 'zero':
#     print("four minus zero equals four")
# if a == 'four' and b == 'minus' and c == 'one':
#     print("four minus one equals three")
# if a == 'four' and b == 'minus' and c == 'two':
#     print("four minus two equals two")
# if a == 'four' and b == 'minus' and c == 'three':
#     print("four minus three equals one")
# if a == 'four' and b == 'minus' and c == 'four':
#     print("four minus four equals zero")
# if a == 'four' and b == 'minus' and c == 'five':
#     print("four minus five equals negative one")
# if a == 'five' and b == 'minus' and c == 'zero':
#     print("five minus zero equals five")
# if a == 'five' and b == 'minus' and c == 'one':
#     print("five minus one equals four")
# if a == 'five' and b == 'minus' and c == 'two':
#     print("five minus two equals three")
# if a == 'five' and b == 'minus' and c == 'three':
#     print("five minus three equals two")
# if a == 'five' and b == 'minus' and c == 'four':
#     print("five minus four equals one")
# if a == 'five' and b == 'minus' and c == 'five':
#     print("five minus five equals zero")
    
# instead of conditionals, I used a dictionary for the potential values.
# the input values have to be positive whole numbers, so there is a standalone dictionary for that
potential_input_dict = { 
    'zero' : 0,
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
}

# the resulting output could be a range of numbers of from (-5) to (+10), also stored in a dictionary
result_dict = {
    -5: 'negative five',
    -4: 'negative four',
    -3: 'negative three',
    -2: 'negative two',
    -1: 'negative one',
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
}


# if (not a == 'zero' and not a == 'one' and not a == 'two' and not a == 'three' and not a == 'four' and not a == 'five') or (not c == 'zero' and not c == 'one' and not c == 'two' and not c == 'three' and not c == 'four' and not c == 'five') or (not b == 'plus' and not b == 'minus'):
#     print("I am not able to answer this question. Check your input.")

# the error handling can be combined with the math for efficiency
# here is the input validation
if a in potential_input_dict.keys() and c in potential_input_dict.keys() and b in ['plus', 'minus']:
    if b == 'plus':
        # perform the calculation on the integers, and return the string components desired
        d = result_dict[(potential_input_dict[a] + potential_input_dict[c])]
        # print the strings using f-string formatting to dynamically update the print statement
        print(f"{a} plus {c} equals {d}")
    else: # if input 2 was selected as a minus, the only alternative to plus that is accepted in the start of this block
        d = result_dict[(potential_input_dict[a] - potential_input_dict[c])]
        print(f"{a} minus {c} equals {d}")
else:
    print("I am not able to answer this question. Check your input.")


# keep this
print("Thanks for using this calculator, goodbye :)")
