import random

NUM_PAIRS = 3

def main():
    # Milestone #1: Create the truth list
    # Creates [0, 0, 1, 1, 2, 2...]
    truth = []
    for i in range(NUM_PAIRS):
        truth.append(i)
        truth.append(i)

    # Milestone #2: Shuffle the list
    random.shuffle(truth)

    # Milestone #3: Create a displayed list
    displayed = ['*'] * len(truth)

    # Milestone #6: Play multiple turns until all '*' are gone
    while '*' in displayed:
        clear_terminal()
        print(displayed)
        
        # Milestone #4 & #5: Get two indices and check for match
        index1 = get_valid_index(displayed)
        index2 = get_valid_index(displayed)
        
        # Ensure they didn't pick the exact same physical card twice
        while index1 == index2:
            print("You already picked that card! Choose a different second index.")
            index2 = get_valid_index(displayed)

        print(f"Value at index {index1} is {truth[index1]}")
        print(f"Value at index {index2} is {truth[index2]}")

        # Check if the values at those indices in the truth list match
        if truth[index1] == truth[index2]:
            print("Match!")
            displayed[index1] = truth[index1]
            displayed[index2] = truth[index2]
        else:
            print("No match. Try again.")
        
        input("Press Enter to continue... ")

    clear_terminal()
    print(displayed)
    print("Congratulations! You won!")

def get_valid_index(displayed):
    """
    Prompts user for an index and validates it.
    Returns a valid integer index.
    """
    while True:
        try:
            val = int(input("Enter an index: "))
            # Check if index is in bounds
            if val < 0 or val >= len(displayed):
                print(f"Invalid index. Must be between 0 and {len(displayed) - 1}.")
            # Check if index was already revealed
            elif displayed[val] != '*':
                print("That index is already revealed. Choose another.")
            else:
                return val
        except ValueError:
            print("Please enter a valid integer.")

def clear_terminal():
    for i in range(20):
        print('\n')

if __name__ == '__main__':
    main()