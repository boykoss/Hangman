import random
print("H A N G M A N")
print("Guess the word:")
l = ["python", "java", "swift", "javascript"]
word = random.choice(l)
answer = input()
if (answer == word):
    print("You survived!")
else:
    print("You lost!")
    print(answer)
    print(word)


