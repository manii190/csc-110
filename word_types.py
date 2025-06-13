'''
 Mani Abhiram
CSC-110
Project-9
This project reads a text file, analyzes the word usage, and outputs
statistics in a separate file.
'''
def text_to_list(file_name):
    '''
    Reads a file and returns a list of words.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        list: A list of words in the file.
    '''
def load_words_from_file(file_path):
    '''
    Reads a file and returns a list of words.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        list: A list of words found in the file.
    '''
    words = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                for word in line.split():
                    words.append(word)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    return words

def count_word_frequencies(words):
    '''
    Counts the frequency of each word in a list.

    Args:
        words (list): A list of words.

    Returns:
        dict: A dictionary with words as keys and their frequencies as values.
    '''
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies

def get_most_frequent_words_by_size(word_frequencies):
    '''
    Returns the most frequent words categorized by their size (small, medium, large).

    Args:
        word_frequencies (dict): A dictionary of word frequencies.

    Returns:
        tuple: Three words with the highest frequencies in their size categories (small, medium, large).
    '''
    small_word = None
    medium_word = None
    large_word = None
    small_count = 0
    medium_count = 0
    large_count = 0

    for word, count in word_frequencies.items():
        word_length = len(word)
        if word_length <= 4:
            if count > small_count:
                small_word, small_count = word, count
        elif 5 <= word_length <= 7:
            if count > medium_count:
                medium_word, medium_count = word, count
        elif word_length >= 8:
            if count > large_count:
                large_word, large_count = word, count

    return small_word, medium_word, large_word

def count_case_variations(word_frequencies):
    '''
    Counts the number of capitalized and non-capitalized words.

    Args:
        word_frequencies (dict): A dictionary of word frequencies.

    Returns:
        tuple: Two integers representing the count of capitalized and non-capitalized words.
    '''
    capitalized_count = 0
    non_capitalized_count = 0
    for word in word_frequencies:
        if "A" <= word[0] <= "Z":
            capitalized_count += 1
        else:
            non_capitalized_count += 1
    return capitalized_count, non_capitalized_count

def count_punctuation(word_frequencies):
    '''
    Counts the number of words with and without punctuation.

    Args:
        word_frequencies (dict): A dictionary of word frequencies.

    Returns:
        tuple: Two integers representing the count of punctuated and non-punctuated words.
    '''
    punctuated_count = 0
    non_punctuated_count = 0
    for word in word_frequencies:
        if word[-1] in ".,!?;:":
            punctuated_count += 1
        else:
            non_punctuated_count += 1
    return punctuated_count, non_punctuated_count

def count_word_sizes(word_frequencies):
    '''
    Counts the number of small, medium, and large words.

    Args:
        word_frequencies (dict): A dictionary of word frequencies.

    Returns:
        tuple: Three integers representing the count of small, medium, and large words.
    '''
    small_count = 0
    medium_count = 0
    large_count = 0
    for word in word_frequencies:
        word_length = len(word)
        if word_length <= 4:
            small_count += 1
        elif 5 <= word_length <= 7:
            medium_count += 1
        else:
            large_count += 1
    return small_count, medium_count, large_count

def write_analysis_to_file(word_frequencies, input_file):
    '''
    Writes the analysis results to an output file.

    Args:
        word_frequencies (dict): A dictionary of word frequencies.
        input_file (str): The name of the input file being analyzed.

    Returns:
        None
    '''
    output_file_name = input_file[:-4] + "_analysis.txt"
    try:
        with open(output_file_name, 'w') as output_file:
            unique_word_count = len(word_frequencies)
            most_frequent_small, most_frequent_medium, most_frequent_large = get_most_frequent_words_by_size(word_frequencies)
            small_count, medium_count, large_count = count_word_sizes(word_frequencies)
            capitalized_count, non_capitalized_count = count_case_variations(word_frequencies)
            punctuated_count, non_punctuated_count = count_punctuation(word_frequencies)
            
            output_file.write(f"Total unique words: {unique_word_count}\n")
            output_file.write("Most frequent words by size:\n")
            output_file.write(f"* Small: {most_frequent_small}\n")
            output_file.write(f"* Medium: {most_frequent_medium}\n")
            output_file.write(f"* Large: {most_frequent_large}\n\n")
            
            output_file.write("Word Lengths:\n")
            output_file.write(f"* Small: {small_count} ({round(small_count / unique_word_count * 100, 2)}%)\n")
            output_file.write(f"* Medium: {medium_count} ({round(medium_count / unique_word_count * 100, 2)}%)\n")
            output_file.write(f"* Large: {large_count} ({round(large_count / unique_word_count * 100, 2)}%)\n")
            
            # Bar representation
            small_bar = '#' * round(small_count / unique_word_count * 50)
            medium_bar = '%' * round(medium_count / unique_word_count * 50)
            large_bar = '*' * round(large_count / unique_word_count * 50)
            output_file.write(small_bar + medium_bar + large_bar + "\n\n")
            
            output_file.write("Capitalization:\n")
            output_file.write(f"* Capitalized: {capitalized_count} ({round(capitalized_count / unique_word_count * 100, 2)}%)\n")
            output_file.write(f"* Non-capitalized: {non_capitalized_count} ({round(non_capitalized_count / unique_word_count * 100, 2)}%)\n")
            
            # Bar representation
            capitalized_bar = '#' * round(capitalized_count / unique_word_count * 50)
            non_capitalized_bar = '%' * round(non_capitalized_count / unique_word_count * 50)
            output_file.write(capitalized_bar + non_capitalized_bar + "\n\n")
            
            output_file.write("Punctuation:\n")
            output_file.write(f"* Punctuated: {punctuated_count} ({round(punctuated_count / unique_word_count * 100, 2)}%)\n")
            output_file.write(f"* Non-punctuated: {non_punctuated_count} ({round(non_punctuated_count / unique_word_count * 100, 2)}%)\n")
            
            punctuated_bar = '#' * round(punctuated_count / unique_word_count * 50)
            non_punctuated_bar = '%' * round(non_punctuated_count / unique_word_count * 50)
            output_file.write(punctuated_bar + non_punctuated_bar)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = "text_sample.txt"  # Replace with the path to your actual file
words = load_words_from_file(file_path)
word_frequencies = count_word_frequencies(words)
write_analysis_to_file(word_frequencies, file_path)








