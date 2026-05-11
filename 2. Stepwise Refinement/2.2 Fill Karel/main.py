from karel.stanfordkarel import *

def main():
    fill_row()
    return_to_start()
    
    while left_is_clear():
        go_up()
        fill_row()
        return_to_start()
    
    move_to_top_right()


def fill_row():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()


def return_to_start():
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def go_up():
    turn_left()
    move()
    turn_right()


def move_to_top_right():
    while front_is_clear():
        move()


# helpers
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()