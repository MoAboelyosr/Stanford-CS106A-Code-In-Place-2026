def main():
    words = load_words_from_file("words.txt")
    
    # Step 1: Create a dictionary to store word counts
    word_counts = {}
    
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in word_counts:
            word_counts[word] += 1
        # If the word is new, add it to the dictionary with a count of 1
        else:
            word_counts[word] = 1
            
    # Step 2: Loop through the dictionary and print the histogram
    for word in word_counts:
        count = word_counts[word]
        print_histogram_bar(word, count)

def print_histogram_bar(word, count):
    """
    Prints one bar in the histogram.
    """
    # {word : <8} ensures the word column is 8 characters wide
    # 'x' * count repeats the character 'x' based on the frequency
    print(f"{word : <8}: {'x' * count}")

def load_words_from_file(filepath):
    """
    Loads words from a file into a list and returns it.
    (Do not modify this function)
    """
    words = []
    try:
        with open(filepath, 'r') as file_reader:
            for line in file_reader.readlines():
                cleaned_line = line.strip()
                if cleaned_line != '':
                    words.append(cleaned_line)
    except FileNotFoundError:
        print(f"Could not find {filepath}")
    
    return words

if __name__ == '__main__':
    main()
