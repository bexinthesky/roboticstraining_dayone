# print 'Hello World'
# name = raw_input('Your name: Rebecca')
# print name
# if hitsObject():
#    goBack()
# if 1 == 1:
#    print 'Yes'
#def myFirstFunction():
#    print 'Function ran'
#myFirstFunction()
# def functionWithInput(name, age):
#     print name
#     print age
# functionWithInput('Rebecca', 27)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# colors = ['magenta', 'lavender', 'turquoise', 'not found']
# print numbers[0]
# for number in numbers:
#     if number % 2 == 0: 
#         print number
# for color in colors:
#     if color == 'magenta':
#         print 'You printed magenta'
#     elif color == 'lavender':
#         print 'You printed lavender'
#     elif color == 'turquoise':
#         print 'You printed turquoise'
#     else:
#         print 'Color not found'

noun1 = raw_input('Please enter a noun:')
verb1 = raw_input('Please enter a verb:')
noun2 = raw_input('Please enter another noun:')
verb2 = raw_input('Please enter another verb:')
# verisimilitude
# objurgate
#snowflake obsidian
#erupt


def check_input(user_input):
    if user_input != '' or user_input != ' ':
        return user_input
    else:
        print 'You entered an incorrect input!'
        return

def start_game():
    print 'You were walking along one day, when you heard a faint noise from overhead. You looked up and a giant %s was floating in the sky. You panicked, because well, why is a giant %s floating in the sky? Seconds later, it started to %s You started to run in fear, but it was gaining on you. Your only hope was a %s' %(noun1, noun1, verb1, noun2)
    
start_game()

# alternative version from adam
# def startGame(noun1, noun2, verb1):
#  print('You were walking along one day, when you heard a faint noise from overhead. You looked up and a giant ' + noun1 + ' was floating in the sky. You panicked, because well, why is a giant ' + noun1 + ' floating in the sky? Seconds later, it started to '+ verb1 + ' You started to run in fear, but it was gaining on you. Your only hope was a' + noun2)



#startGame('hippopotomas', 'bat', 'run')