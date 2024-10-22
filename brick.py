import machine
from machine import I2C, PWM, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(1, sda=machine.Pin(18), scl=machine.Pin(19), freq=400000)
display_text = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    

BUTTON_A_PIN = 15
BUTTON_B_PIN = 14
BUTTON_C_PIN = 13
BUTTON_D_PIN = 12

button_a = machine.Pin(BUTTON_A_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_b = machine.Pin(BUTTON_B_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_c = machine.Pin(BUTTON_C_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_d = machine.Pin(BUTTON_D_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)

def key_input():
    while True:
        if button_a.value() == 1:
            return("A")
            break
        if button_b.value() == 1:
            return("B")
            break
        if button_c.value() == 1:
            return("C")
            break
        if button_d.value() == 1:
            return("D")
            break

def pick(items):
    t = 0
    items.append("End")
    while True:
        display_text.clear()
        display_text.move_to(0,0)
        display_text.putstr(items[t])
        display_text.move_to(1,1)
        display_text.putstr(items[t+1])
        move = key_input()
        if move == 'A':
            return(t)
        elif move == 'D':
            return("BACK")
            break
        elif move == 'B' and t < (len(items)-2):
            t += 1
            continue
        elif move == 'C' and t > 0:
            t -= 1
            continue
