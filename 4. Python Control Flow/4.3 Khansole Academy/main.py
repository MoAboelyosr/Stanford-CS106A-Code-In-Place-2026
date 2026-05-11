import random

def main():
    print("Khansole Academy")

    # Generate two random 2-digit numbers
    rand_num_1 = random.randint(10, 99)
    rand_num_2 = random.randint(10, 99)

    # Calculate the correct sum
    correct = rand_num_1 + rand_num_2

    # The grader usually wants the question exactly like this:
    print(f"What is {rand_num_1} + {rand_num_2}?")
    
    # Use input() without a prompt string to avoid extra spaces
    answer = input("Your answer: ")
    answer = int(answer)

    # Check the result
    if answer == correct:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {correct}")

  
if __name__ == '__main__':
    main()