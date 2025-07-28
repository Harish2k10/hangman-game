
+# 🎮 Hangman Game
+
+A fun and interactive command-line Hangman game written in Python! Guess the mystery word letter by letter before the hangman is fully drawn.
+
+## ✨ Features
+
+- 🎨 **ASCII Art**: Beautiful hangman drawings that progress with wrong guesses
+- 🎯 **Smart Word Selection**: Automatically filters words to ensure quality gameplay (alphabetic, 3+ letters)
+- 💬 **User-Friendly Interface**: Clear feedback with emojis and intuitive prompts
+- ✅ **Input Validation**: Prevents invalid inputs and duplicate guesses
+- 🎲 **Random Words**: Uses the `random-word` library for varied gameplay
+
+## 🚀 Quick Start
+
+### Prerequisites
+
+- Python 3.6 or higher
+- pip (Python package installer)
+
+### Installation
+
+1. **Clone the repository**
+   ```bash
+   git clone https://github.com/Harish2k10/hangman-game.git
+   cd hangman-game
+   ```
+
+2. **Install dependencies**
+   ```bash
+   pip install random-word
+   ```
+
+3. **Run the game**
+   ```bash
+   python hangman.py
+   ```
+
+## 🎯 How to Play
+
+1. The game will display blanks representing the mystery word
+2. Guess one letter at a time by typing it and pressing Enter
+3. Correct guesses reveal the letter's position(s) in the word
+4. Wrong guesses add a part to the hangman drawing
+5. Win by guessing all letters before the drawing is complete (6 wrong guesses max)
+6. Lose if the hangman drawing is completed before you guess the word
+
+## 📸 Game Preview
+
+```
+🎮 Welcome to Hangman!
+_ _ _ _ _ 
+
+     +---+
+     |   |
+         |
+         |
+         |
+         |
+    =========
+
+Lives left: 6
+Guessed letters: 
+Word: _ _ _ _ _
+Guess a letter: 
+```
+
+## 🛠️ Technical Details
+
+- **Language**: Python 3
+- **Dependencies**: 
+  - `random-word`: For generating random words
+  - `string`: Built-in module for letter validation
+- **Word Filtering**: Automatically ensures words are:
+  - Alphabetic characters only
+  - Minimum 3 letters long
+  - Converted to lowercase for consistency
+
+## 🤝 Contributing
+
+Feel free to fork this project and submit pull requests for improvements! Some ideas:
+- Add difficulty levels
+- Include word categories
+- Add a scoring system
+- Create a GUI version
+
+## 📄 License
+
+This project is licensed under the [MIT License](LICENSE.md) - see the file for details.
+
+## 👨‍💻 Author
+
+**Harish K** - [GitHub Profile](https://github.com/Harish2k10)
+
+---
+
+⭐ If you enjoyed this game, please give it a star on GitHub!