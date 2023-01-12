import random
import string
life = ["road", "week", "axe", "dart", "car", "bake", "jessy", "meat", "vase", "hen", "guide", "player", "kneel", "zeal", "affirm", "umbrella", "search", "blastphamy", "exquiste", "shame", "success", "jungle", "thugs", "shift", "al-sadd", "ja moa", "wish", "Momoa", "gra va", "messi", "armstrong", "ronaldo"]
def valid_word(life):
	word = random.choice(life)
	while " " in word or "-" in word:
		word = random.choice(life)
	return word.upper()
	
def hangman():
	word = valid_word(life)
	word_letters = set(word)
	used_letters = set()
	alphabet = set(string.ascii_uppercase)
	lives = 6
	
	while len(word_letters) > 0 and lives > 0:
		print("\nYou have tried these letter(s): ",' '.join(used_letters))
		current_word = [letter if letter in used_letters else "-" for letter in word]
		print("Current word: ", ' '.join(current_word))
		user_letters = input("Choose a letter: ").upper()
		if user_letters in alphabet - used_letters:
			used_letters.add(user_letters)
			if user_letters in word_letters:
				word_letters.remove(user_letters)
			else:
				 lives -= 1
				 print(f"Letter is not in word. You now have {lives} live(s). Try again.")
		elif user_letters in used_letters:
			print("You have used the letter. Try again.")
		else:
			print("Invalid input")
	if lives == 0:
		print(f"You died. The word was {word}")
	else:
		print(f"Yay! You got the word {word} right")
hangman()

