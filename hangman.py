from random_word import RandomWords
import string

# 0-6 lives
HANGMAN_PICS = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========''',  # 6 
    '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========''',  # 5
    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========''',  # 4
    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''',  # 3
    '''
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========''',  # 2
    '''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========''',  # 1
    '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========='''   # 0
]

# Get a random word
r = RandomWords()
word = None

while not word or not word.isalpha() or len(word) < 3:
    word = r.get_random_word()
word = word.lower()

word_letters = set(word)
guessed_letters = set()
lives = 6

print("🎮 Welcome to Hangman!")
print("_ " * len(word))

# Game loop
while len(word_letters) > 0 and lives > 0:
    print(HANGMAN_PICS[6 - lives])  # Show hangman
    print("\nLives left:", lives)
    print("Guessed letters:", " ".join(sorted(guessed_letters)))

    # Display the hidden word
    word_display = [letter if letter in guessed_letters else "_" for letter in word]
    print("Word:", " ".join(word_display))

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or guess not in string.ascii_lowercase:
        print("❗ Enter a valid single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ Already guessed that.")
    elif guess in word_letters:
        guessed_letters.add(guess)
        word_letters.remove(guess)
        print("✅ Correct!")
    else:
        guessed_letters.add(guess)
        lives -= 1
        print("❌ Wrong guess!")


print(HANGMAN_PICS[6 - lives]) 

if lives == 0:
    print("\n💀 Game over! The word was:", word)
else:
    print("\n🎉 You won! The word was:", word)
