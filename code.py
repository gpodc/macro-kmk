print("Macro-Pico Initiated...")

import board
import supervisor
import digitalio
import storage
import usb_cdc
import usb_hid

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.modules.layers import Layers
from kmk.modules.macros import Press, Release, Tap
from kmk.extensions.media_keys import MediaKeys

# from kmk.extensions.LED import LED

#initialization
keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(Layers())
keyboard.modules.append(macros)
keyboard.extensions.append(MediaKeys())
keyboard.col_pins = (board.GP14, board.GP13, board.GP12, board.GP16, board.GP17, board.GP9)
keyboard.row_pins = (board.GP15, board.GP7)
# keyboard.diode_orientation = DiodeOrientation.COL2ROW

#kmk vars
COPY_KEY = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.C),
    Release(KC.LCTL)
)

# PASTE_KEY = KC.MACRO(
#     Press(KC.LCTL),
#     Tap(KC.V),
#     Release(KC.LCTL)
# )

PASTE_KEY2 = KC.LCTL(KC.V)

DISC_MUTE = KC.MACRO(
    Press(KC.RCTL),
    Press(KC.RSHIFT),
    Tap(KC.M),
    Release(KC.RCTL),
    Release(KC.RSHIFT)
)

DISC_DEAF = KC.MACRO(
    Press(KC.RCTL),
    Press(KC.RSHIFT),
    Tap(KC.D),
    Release(KC.RCTL),
    Release(KC.RSHIFT)
)
#layer change
LAYER_CHANGE1 = KC.DF(1)
LAYER_CHANGE0 = KC.DF(0)

#leds (circuitpy)
led1 = digitalio.DigitalInOut(board.GP5)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP28)
led2.direction = digitalio.Direction.OUTPUT

led_tog = True
def update_leds():
    if keyboard.active_layers[0] == 0 and led_tog is True:
        led1.value = True
        led2.value = False
    elif keyboard.active_layers[0] == 1 and led_tog is True:
        led1.value = False
        led2.value = True

keyboard.before_matrix_scan = update_leds

keyboard.keymap = [
    #LAYER 0
    [COPY_KEY, PASTE_KEY2, DISC_MUTE, DISC_DEAF, KC.MUTE, KC.TRNS,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, LAYER_CHANGE1],
    
    #LAYER 1
    [KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.TRNS,
     KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, LAYER_CHANGE0],
]

if __name__ == '__main__':
    keyboard.go()




