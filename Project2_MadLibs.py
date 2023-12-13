# Task 2
#Mad libz generator
"""
its a type of a story replaced by words. 
"""

# file handling used
# made txt file and opened it in read mode initially
with open("story.txt", "r") as f:
    story = f.read()

words = set()
initial_word = -1

# for angle bracket
check_first = "<"
check_last = ">"

for i, char in enumerate(story): # enumerate gives us access to the position as well as the element
    if char == check_first: #if its equal to the angle bracket in our story.txt file
        start = i

    if char == check_last and start != -1:
        word = story[start: i + 1]
        words.add(word)
        start = -1

answers = {}

for word in words:
    answer=input("Enter a word for " + word + ": ") # will access the word written in that angular bracket from story.txt file
    answers[word]=answer

for word in words:
    story=story.replace(word, answers[word]) # replacing the words you wrote instead and then printing the whole text at the end

print(story)