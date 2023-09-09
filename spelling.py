from spellchecker import SpellChecker

# Initialize the SpellChecker
spell = SpellChecker()

# Function to detect misspelled words in a file
def detect_misspelled_words(original.txt):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()

        misspelled = spell.unknown(words)

        return misspelled

if __name__ == "__main__":
    file_path = 'your_text_file.txt'  # Replace with the path to your text file
    misspelled_words = detect_misspelled_words(file_path)

    if misspelled_words:
        print("Misspelled words:")
        for word in misspelled_words:
            print(word)
    else:
        print("No misspelled words found.")
