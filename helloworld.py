"""
"Hello, World!" program using python art module

 _   _        _  _             _    _               _      _  _ 
| | | |      | || |           | |  | |             | |    | || |
| |_| |  ___ | || |  ___      | |  | |  ___   _ __ | |  __| || |
|  _  | / _ \| || | / _ \     | |/\| | / _ \ | '__|| | / _` ||_|
| | | ||  __/| || || (_) | _  \  /\  /| (_) || |   | || (_| ||_|
\_| |_/ \___||_||_| \___/ ( )  \/  \/  \___/ |_|   |_| \__,_|(_)
                          |/                                    
                                    Font: doom from art module  

It is fancy to say the least, and janky under the hood ;)
Using latest technology from "art" module (not builtin).
"""


MSG         = "Hello, World!"
FONT        = "doom" # "georgia11"
SPEED_RANGE = 1,20 # ms



from sys import stdout
from time import sleep
from random import randint


# replacement for ''.join([])
joinstr = lambda *args, sep='' : sep.join(args)

def draw_by_line():
    """
    Get fancy text from "art" and write it to the
    output one by one, also with a random delay
    between SPEED_RANGE
    """
    from art import text2art

    for c in text2art(MSG,FONT):
        stdout.write(c)
        if c == ' ':continue
        stdout.flush()
        sleep(randint(*SPEED_RANGE)*.001)

def main():
    """Catches Errors and Does stuff"""

    # Say bye bye to the cursor
    stdout.write("\033[?25l")

    # Catch Exceptions and draw it
    try: draw_by_line()
    except BaseException as e:
        stdout.write( joinstr(
                "\n\n\033[91m",repr(e),"\033[0m\n"
        ) )

    # Say hello to the cursor
    stdout.write("\033[?25h")


if __name__=="__main__":
    main()

