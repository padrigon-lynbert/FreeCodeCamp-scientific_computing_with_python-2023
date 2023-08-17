# import re 
import random

words = story = """
In a hidden forest, a courageous young sorceress stumbled upon a mystical amulet.
As she wore it, whispers of ancient magic consumed her, granting incredible powers. 
But with great power came a daunting choice: use it for good or succumb to darkness.
Her destiny began, teetering on a delicate thread.
""".lower().split() #lowercase story is now inside words=[] put as word 

words = [word.strip('.,:') for word in words] #remove special chars
exclude_words = ["do", "a", "in", "as", "on", "it", "or", "to", "of", "for", "with", "she", "her", "but"] #specify what to exclude
words = [word for word in words if word not in exclude_words] #remove excluded

for i in range(10): #test(10 times) if working
    random_word = random.choice(words)
    print(random_word)