class flashcard:

    def __init__(self, word, meaning):
        
        self.word = word
        self.meaning = meaning

    def __str__(self):
        
        return self.word+ '(' +self.meaning+ ')'
    
flash = []

print("Welcome to Flashcards from Python!")

while (True):
    word = input("Enter a word that you would like for your flashcard: ")
    meaning = input("Enter the meaning of that word: ")
    flash.append(flashcard(word,meaning)) 
    
    option = int(input("Enter 0 if you want to enter another flascard, otherwise enter 1: "))
    
    if option:
        break

print("\n Flashcards: ")

for i in flash:
    print(">", i)