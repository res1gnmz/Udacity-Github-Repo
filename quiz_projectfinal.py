# For this project you'll be building a fill-in-the-blanks quiz.
# Your quiz will prompt a user with a sentence containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the sentence.

import re

intro = """*** Welcome to Allen's fill-in-the-blanks quiz! ***
Up to 4 attempts are allowed for each question. If your answer is a number, only type in positive
numbers only, and remember to use numerical figures instead of words - e.g. 10 instead of ten.
"""

quiz_easy = """*** Quiz: Easy Level ***
In Python, you can create a ___1___ by assigning a value to a name. These values can be various data types
such as numbers, a list, tuple, dictionary, and/or string. The expression "Hello " is an example of a ___2___.
If we want to concatenate the word "World" to said expression, which arithmetic operator would you use? ___3___
Now, let's say we assign the variable name 'intro' to this string and want to access parts of it:
What index number represents the character "W" in "Hello World"? intro[___4___]
Write a print statement that will extract the substring "World" from intro. ___5___
"""

quiz_normal = '''*** Quiz: Normal Level ***
How many inputs does the following procedure, or function, take?  ___1___
def sum(a, b):
	a = a + b
	return a

A while loop will continue to run as long as the defined condition evaluates to ___2___

What is the output of this function? ___3___
a = 2
b = 5
def is_bigger(a, b):
	print a > b

Which comparison operator is used to see if the values of two operands are not equal? ___4___

At what value of i will this code stop running? ___5___
i = 0
while i < 5:
	i = i + 1
return i
'''

quiz_hard = '''*** Quiz: Hard Level ***
The index position of 'Monkey' in list_of_things is [___1___][___2___].
list_of_things = ['Cars:', ['Honda', 'Tesla', 'Lexus'], 'Animals:', ['Dog', 'Cat', 'Monkey']]

What is the value of q[2] after the following code runs? ___3___
p = [23, 54, 84]
q = [34, 87, 50]
q.append(p)

What value will be printed below? ___4___
numbers = [2, 3, 1, 5]
def mult_list(numbers):
	result = 1
	for n in numbers:
		result = result * n
	return result
print mult_list(numbers)

For the following questions, only enter the name of the function; do not include the parentheses
- e.g. replace instead of replace()

Which function is needed to run this code without producing a syntax error?
print "There were " + ___5___(5) + " birds above us."

Which function is needed to prompt the user to enter their name in the following code?
user_input = ___6___("My name is: ")
'''

answers_easy = ["variable", "string", "+", "6", "print intro[6:]"]
answers_normal = ["2", "true", "false", "!=", "4"]
answers_hard = ["3", "2", "50", "30", "str", "raw_input"]

blanks = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___"]

def pick_difficulty():
	"""Prompts user to choose one of three difficulty level and outputs that choice (input) as a string"""
	commence = " mode commencing... \n"
	while True:
		user_diff_input = raw_input("Please pick one of the possible difficulty levels (easy, normal, hard): ").lower()
		if user_diff_input == 'easy' or user_diff_input == 'normal' or user_diff_input == 'hard':
			print user_diff_input + commence
			return user_diff_input
			break
		else:
			print "You must choose easy, normal, or hard."

def set_quiz(user_level):
	"""Returns corresponding quiz based on difficulty level chosen"""
	if user_level == 'easy':
		quiz = quiz_easy
	elif user_level == 'normal':
		quiz = quiz_normal
	elif user_level == 'hard':
		quiz = quiz_hard
	return quiz

def set_answers(user_level):
	"""Returns corresponding solutions based on difficulty level chosen"""
	if user_level == 'easy':
		answers = answers_easy
	elif user_level == 'normal':
		answers = answers_normal
	elif user_level == 'hard':
		answers = answers_hard
	return answers


def is_holder(holder, blank):
	"""Checks to see if the inputted numbered blank is contained in the placeholder that's passed thru"""
	if blank in holder:
		return blank
	return None

def fill_holder(quiz, blank, user_answer):
	"""Takes a quiz (easy, normal, hard) as input and splits into a list of words.
	If a placeholder is found, it is replaced by the input provided by user and added to an empty list.
	Otherwise, the word is simply added to the empty list. Once all words (including placeholders) are
	added to the empty list, it is joined into a new string and returned as output"""
	new_quiz = []
	# quiz = quiz.split()
	quiz = re.findall(r'\S+|\n', quiz)
	for holder in quiz:
		replacement = is_holder(holder, blank)
		# print replacement # check to see if function is_holder is returning the right output
		if replacement != None:
			answer = holder.replace(replacement, user_answer)
			new_quiz.append(answer)
		else:
			new_quiz.append(holder)
	filled_quiz = " ".join(new_quiz)
	return filled_quiz

def max_guesses(index, answers, user_answer):
	"""This function was added to shorten the length of start_quiz function."""
	max_guesses = 4
	attempted = index + 1
	if user_answer != answers[index]:
		max_guesses = max_guesses - attempted
		print "\nIncorrect, please try again. You have " + str(max_guesses) + " attempts left.\n ---------------------"
		if max_guesses == 0:
			print "Fail. Let's start over!"
			start_quiz()

def start_quiz():
	"""If user types in correct answer, fill_holder function executes and prints quiz level with placeholder replaced.
	Else, the user is told the answer is incorrect and the number of attempts remaining. The while loop allows the user
	to continue giving an answer input until all questions of that quiz level are correct, in which case a congrats
	statement and full solution is printed, or until user runs out of attempts, which restarts the quiz."""
	print intro
	level = pick_difficulty()
	quiz = set_quiz(level)
	answers = set_answers(level)
	index = 0
	while index+1 <= len(answers):
		print quiz
		user_answer = raw_input("What should take the place of " + blanks[index] + "? ")
		if user_answer == answers[index]:
			print "\nCorrect!"
			quiz = fill_holder(quiz, blanks[index], user_answer) #+ "\n"
			index += 1
		else:
			max_guesses(index, answers, user_answer)
			index += 1
	print "Congratulations on passing the " + level + " stage!\n<<Solution>>\n" + quiz

start_quiz()
