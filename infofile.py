import os
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
    words = []
    file = open(file_name, 'r')
    for line in file:
        line = line.strip()
        for word in line.split():
            words.append(word)
    file.close()
    return words

def count_words(words):
    '''
    Counts the occurrences of each word in a list.

    Args:
        words (list): A list of words.

    Returns:
        dict: A dictionary with words as 
        keys and their counts as values.
    '''
    counts = {}
    for word in words:  
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def most_frequent(word_counts):
    '''
    Returns the most frequent words by their 
    size (small, medium, large).

    Args:
        word_counts (dict): A dictionary of word counts.

    Returns:
        tuple: Three words (small, medium, large) 
        with the highest frequencies in their size category.
    '''
    
    small = None
    medium = None
    large = None
    small_count = 0
    medium_count = 0
    large_count = 0

    for word, count in word_counts.items():
        length = len(word)
        if length <= 4:
            if count > small_count:
                small, small_count = word, count
        elif 5 <= length <= 7:
            if count > medium_count:
                medium, medium_count = word, count
        elif length >= 8:
            if count > large_count:
                large, large_count = word, count
    return small, medium, large


def count_capitalized(word_counts):
    '''
    Counts the capitalized and non-capitalized words.

    Args:
        word_counts (dict): A dictionary of word counts.

    Returns:
        tuple: Two roundegers representing the
          number of capitalized and non-capitalized words.
    '''
    capitalized = 0
    non_capitalized = 0
    for word in word_counts:
        if "A" <= word[0] <= "Z":
            capitalized += 1
        else:
            non_capitalized += 1
    return capitalized, non_capitalized

def count_punctuated(word_counts):
    '''
    Counts the punctuated and non-punctuated words.

    Args:
        word_counts (dict): A dictionary of word counts.

    Returns:
        tuple: Two roundegers representing the number 
        of punctuated and non-punctuated words.
    '''
    punctuated = 0
    non_punctuated = 0
    for word in word_counts:
        if word[-1] in ".,!?;:":
            punctuated += 1
        else:
            non_punctuated += 1
    return punctuated, non_punctuated

def count_sizes(word_counts):
    '''
    Counts the number of small, medium, and large words.

    Args:
        word_counts (dict): A dictionary of word counts.

    Returns:
        tuple: Three roundegers representing the number
          of small, medium, and large words.
    '''
    small = 0
    medium = 0
    large = 0
    for word in word_counts:
        length = len(word)
        if length <= 4:
            small += 1
        elif 5 <= length <= 7:
            medium += 1
        else:
            large += 1
    return small, medium, large

def write_results(word_counts, filename):
    '''
    This function writes the analysis results to a file.

    Args:
        word_counts(dict): A dictionary of word counts.
        filename(str): The name of the input file.
        
    Returns:
        None
    '''    
    output_file = open(filename[:-4] + "_results.txt", 'w')
    unique_count = len(word_counts)
    (common_small, common_med, common_large) = most_frequent(word_counts)
    small_count, med_count, large_count = count_sizes(word_counts)
    capitalized_count, non_capitalized_count = count_capitalized(word_counts)
    punctuated_count, non_punctuated_count = count_punctuated(word_counts) 
    
    output_file.write(f"Total number of unique words: {unique_count}\n")
    output_file.write("Most frequent words by size:\n")
    output_file.write(f"* Small: {common_small}\n")
    output_file.write(f"* Medium: {common_med}\n")
    output_file.write(f"* Large: {common_large}\n\n")
    output_file.write("Length:\n")
        
    output_file.write(f"* Small: {small_count} ")
    output_file.write(f"({round(small_count / unique_count * 100, 2)}%)\n")
        
    output_file.write(f"* Medium: {med_count} ")
    output_file.write(f"({round(med_count / unique_count * 100, 2)}%)\n")
        
    output_file.write(f"* Large: {large_count} ")
    output_file.write(f"({round(large_count / unique_count * 100, 2)}%)\n")
        
        # Fixing the bar representation
    small_bar = '#' * round(small_count / unique_count * 50)
    med_bar = '%' * round(med_count / unique_count * 50)
    large_bar = '*' * round(large_count / unique_count * 50)
        
    output_file.write(small_bar )
    output_file.write(med_bar )
    output_file.write(large_bar + "\n\n")
        
    output_file.write("Capitalization:\n")
    output_file.write(f"* Capitalized: {capitalized_count} ")
    output_file.write(f"({round(capitalized_count/unique_count*100,2)}%)\n")
        
    output_file.write(f"* Non-capitalized: {non_capitalized_count} ")
    output_file.write(
        f"({round(non_capitalized_count / unique_count * 100, 2)}%)\n"
        )
        
        # Fixing the bar representation
    capitalized_bar = '#' * round(capitalized_count / unique_count * 50)
    non_capitalized_bar = '%' * round(non_capitalized_count / unique_count*50)
        
    output_file.write(capitalized_bar )
    output_file.write(non_capitalized_bar + "\n\n")
        
    output_file.write("Punctuation:\n")
    output_file.write(f"* Punctuated: {punctuated_count} ")
    output_file.write(f"({round(punctuated_count/unique_count*100,2)}%)\n")
        
    output_file.write(f"* Non-punctuated: {non_punctuated_count} ")
    output_file.write(
        f"({round(non_punctuated_count / unique_count * 100, 2)}%)\n"
        )
        
    punctuated_bar = '#' * round(punctuated_count / unique_count * 50)
    non_punctuated_bar = '%' * round(non_punctuated_count / unique_count * 50)
        
    output_file.write(punctuated_bar)
    output_file.write(non_punctuated_bar)
    output_file.close()





