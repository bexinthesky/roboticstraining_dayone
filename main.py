# simple print example below
# print 'Hello World'

# using raw input in a variable below
# name = raw_input('Your name: Rebecca')
# print name

# if statement below
# if hitsObject():
#    goBack()

#if statement below
# if 1 == 1:
#    print 'Yes'

# simple function below
#def myFirstFunction():
#    print 'Function ran'

# execute simple function below
#myFirstFunction()

# function with parameters below
# def functionWithInput(name, age):
#     print name
#     print age

# execute function with parameters below
# functionWithInput('Rebecca', 27)

# variables with arrays below
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# colors = ['magenta', 'lavender', 'turquoise', 'not found']

# print numbers variable while specifying which value to print below
# print numbers[0]

# using math in a for statement to print the even values in the numbers variable
# for number in numbers:
#     if number % 2 == 0: 
#         print number

# using a for statement to print the values in the colors variable below
# for color in colors:
#     if color == 'magenta':
#         print 'You printed magenta'
#     elif color == 'lavender':
#         print 'You printed lavender'
#     elif color == 'turquoise':
#         print 'You printed turquoise'
#     else:
#         print 'Color not found'

# variables for madlib function
noun1 = raw_input('Please enter a noun:')
verb1 = raw_input('Please enter a verb:')
noun2 = raw_input('Please enter another noun:')
verb2 = raw_input('Please enter another verb:')

# sample verbs and nouns to use below
# verisimilitude
# objurgate
# snowflake obsidian
# erupt

# function to check user input
def check_input(user_input):
    if user_input != '' or user_input != ' ':
        return user_input
    else:
        print 'You entered an incorrect input!'
        return

# defined a function for a madlib
def start_game():
    print 'You were walking along one day, when you heard a faint noise from overhead. You looked up and a giant %s was floating in the sky. You panicked, because well, why is a giant %s floating in the sky? Seconds later, it started to %s You started to run in fear, but it was gaining on you. Your only hope was a %s' %(noun1, noun1, verb1, noun2)

# execute the function for the madlib    
start_game()

# alternative madlib function from version from adam
# def startGame(noun1, noun2, verb1):
#  print('You were walking along one day, when you heard a faint noise from overhead. You looked up and a giant ' + noun1 + ' was floating in the sky. You panicked, because well, why is a giant ' + noun1 + ' floating in the sky? Seconds later, it started to '+ verb1 + ' You started to run in fear, but it was gaining on you. Your only hope was a' + noun2)

#startGame('hippopotomas', 'bat', 'run')