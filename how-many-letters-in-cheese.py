# the correct answer is 6.
answer = 6
# instructions for user
print("Instructions: This game requires you to count the correct amount of letters in a word.")
print("Rule 1: Type your answer as a number.")
print("Rule 2: Avoid using period at the end of your answer.")
print("Rule 3: Press enter to submit your answer.")
# question
print("Question: How many letters is there in the word cheese?")
# user answers the question
user_answer = int(input("->"))
# if user's answer is equal to the actual answer the user wins
if user_answer == answer:
    print("Your answer is", user_answer)
    print("Correct, cheese has", user_answer, "letters")
    print("You win!")
else:
    print('incorrect')
    