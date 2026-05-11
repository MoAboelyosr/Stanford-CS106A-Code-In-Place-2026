import random

def main():
    side = input("How many sides does your dice have? ")
    side = int(side)
    print("Your roll is", random.randint(1, side))



if __name__ == '__main__':
    main()