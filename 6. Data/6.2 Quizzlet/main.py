def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    # Initialize a counter for correct answers
    correct_count = 0
    
    # Loop over the dictionary
    # 'word' will be the English key, 'translation' will be the Spanish value
    for word, translation in translations.items():
        # Quiz the user
        user_answer = input(f"What is the Spanish translation for {word}? ")
        
        # Check if the answer is correct (case-insensitive is usually a good idea!)
        if user_answer.lower() == translation.lower():
            print("That is correct!")
            correct_count += 1
        else:
            print(f"That is incorrect, the Spanish translation for {word} is {translation}.")
        
        # Print a blank line for visual clarity
        print()

    # Final score summary
    total_words = len(translations)
    print(f"You got {correct_count}/{total_words} words correct, come study again soon!")

if __name__ == '__main__':
    main()