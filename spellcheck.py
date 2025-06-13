def read_spellings():
    misspellings = {}
    with open("misspellings.txt", 'r') as file:
        for line in file:
            spellings = line.strip().split("->")
            misspellings[spellings[0].lower()] = spellings[1]  # Ensure the keys are lowercase
    return misspellings


def correct_spelling(file_name, spell_dict):
    def handle_punctuation(word):
        punctuation = ""
        if word[-1] in ".,?;!":
            punctuation = word[-1]
            word = word[:-1]  # Remove punctuation
        return word, punctuation

    # Open the input and output files using 'with open' to ensure they are closed automatically
    with open(file_name, 'r') as file, open("output_" + file_name, 'w') as output_file:
        for line in file:
            # Split the line into words, handling multiple spaces
            list_of_words = line.split()  # This handles any amount of whitespace
            
            i = 0  # Use a simple index-based while loop instead of enumerate()
            while i < len(list_of_words):
                word = list_of_words[i]
                original_word = word  # Preserve the original word for punctuation handling
                # Handle punctuation and strip it from the word
                word, punctuation = handle_punctuation(word)

                # Check if the word is in the dictionary and correct it if necessary
                if word.lower() in spell_dict:
                    corrected_word = spell_dict[word.lower()]
                    
                    # If the original word was capitalized, capitalize the corrected word
                    if word[0].isupper():
                        corrected_word = corrected_word.capitalize()
                    
                    word = corrected_word  # Update the word with the corrected spelling
                
                word += punctuation  # Reattach punctuation

                # Write the corrected word to the output file
                output_file.write(word)

                # Add a space between words if it's not the last word in the line
                if i < len(list_of_words) - 1:
                    output_file.write(" ")

                i += 1  # Increment index

            # Add a newline after processing each line
            output_file.write("\n")
spell_dict = read_spellings()
correct_spelling("words_1.txt", spell_dict)


