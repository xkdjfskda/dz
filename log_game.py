import time
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='logs_example.log',
                    filemode='w',
                    format='NEW LOG - %(asctime)s - %(levelname)s: %(message)s')

true = ["T", "t", "True"]
false = ["F", "f", "False"]
correct = 0  # Storing the correct answers

name = input("What's your name?")  # Storing the user's name
logging.info('user name - '+name)

print
"\nOK, " + name + ", let's get started. Remember, the following answers are only True or False."
time.sleep(2)

print("\nParis is the captial of France.")
choice = input(">>> ")
if choice in true:
    correct += 1 # If correct, the user gets one point
    print('Correct!')
    logging.info(name+' choose Correct answer!')
else:
    correct += 0
    print('Incorrect!')
    logging.info(name + ' choose Incorrect answer!')

print("\nEngland is an island.")
choice = input(">>> ")
if choice in false:
    correct += 1
    print('Correct!')
    logging.info(name + ' choose Correct answer!')
else:
    correct += 0
    print('Incorrect!')
    logging.info(name + ' choose Incorrect answer!')

print("\nNorthern Ireland isn't part of Great Britian.")
choice = input(">>> ")
if choice in false:
    correct += 1
    print('Correct!')
    logging.info(name + ' choose Correct answer!')
else:
    correct += 0
    print('Incorrect!')
    logging.info(name + ' choose Incorrect answer!')

print("\nAndorra is between France and Spain.")
choice = input(">>> ")
if choice in true:
    correct += 1
    print('Correct!')
    logging.info(name + ' choose Correct answer!')
else:
    correct += 0
    print('Incorrect!')
    logging.info(name + ' choose Incorrect answer!')

print("\nIran use to be part of the Perisan Empire.")
choice = input(">>> ")
if choice in true:
    correct += 1
    print('Correct!')
    logging.info(name + ' choose Correct answer!')
else:
    correct += 0
    print('Incorrect!')
    logging.info(name + ' choose Incorrect answer!')

print("\nTurkmenistan isn't a real country.")
choice = input(">>> ")
if choice in false:
    correct += 1
    print('Correct!')
    logging.info(name + ' choose Correct answer!')
else:
    correct += 0
    print('Incorrect!')
    logging.info(name + ' choose Incorrect answer!')

print("\nYou're finished, " + name + ". You got", correct, "out of 6 correct.")
logging.info(name + 'score = '+str(correct))