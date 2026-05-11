from karel.stanfordkarel import *

def main():
    for i in range(4):
        build_column()
        move_to_next_column()


def build_column():
    turn_left()
    for i in range(5):
        if no_beepers_present():
            put_beeper()
        if front_is_clear():
            move()
    turn_around()
    for i in range(4):
        move()
    turn_left()


def move_to_next_column():
    for i in range(4):
        if front_is_clear():
            move()


# Helper functions
def turn_around():
    turn_left()
    turn_left()


if __name__ == '__main__':
    main()