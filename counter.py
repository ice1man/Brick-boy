import brick
from time import sleep

def main():
    c = 0
    while True:
        brick.display_text.clear()
        brick.display_text.putstr(str(c))
        brick.key_input()
        c += 1
        sleep(0.1)
