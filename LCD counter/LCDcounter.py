import board
import time
import touchio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
# some LCDs are 0x3f... some are 0x27.
touchstate = True
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

touch = touchio.TouchIn(board.A1)

touch1 = touchio.TouchIn(board.A3)

x = 0

while True:
    if touch.value:
        lcd.set_cursor_pos(1, 0)
        lcd.print(str(x+1))
        lcd.print("  ")
        lcd.set_cursor_pos(0, 0)
        lcd.print("Counting Up:  ")
        x = x + 1
        time.sleep(.01)
        while touch.value:
            pass
    if touch1.value:
        lcd.set_cursor_pos(1, 0)
        lcd.print(str(x-1))
        lcd.print("  ")
        lcd.set_cursor_pos(0, 0)
        lcd.print("Counting Down:")
        x = x - 1
        time.sleep(.01)
        while touch1.value:
            pass