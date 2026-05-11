from karel.stanfordkarel import *

def main():
    """
    Karel will start at the southwestern most point, place a beeper in that corner, and the southeastern most point.
    Karel will then ping pong back and forth on the southern wall, moving the two beepers closer to the center.
    What remains is one beeper at the center of the southern wall.
    """
    move_to_wall()
    turn_left()
    turn_left()
    if front_is_blocked():
        put_beeper()
    else:
        place_initial_beepers()
        move_to_wall()
        place_initial_beepers()
        turn_around()
        move()
        while no_beepers_present():
            move()
        while beepers_present():
            relocate_beeper()
        put_beeper()
    if facing_west():
        turn_left()
        turn_left()

def place_initial_beepers():
    if no_beepers_present():
        put_beeper()

#pre: Karel, while moving away from center, runs into a beeper
#post: Karel is now facing toward the center, and has moved the beeper one space toward the center.

def relocate_beeper():
    while beepers_present():
        pick_beeper()
        turn_around()
        move()
        if no_beepers_present():
            put_beeper()
            move()
            while no_beepers_present():
                move()
        else:
            pick_beeper()

def move_to_wall():
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

if __name__ == '__main__':
    main()