print("Starting")

import board
from kmk.hid import HIDModes
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D10,board.D9,board.D8,board.D7,)
keyboard.row_pins = (board.D0,board.D1,board.D2,board.D3,board.D6,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [[
  KC.MUTE, KC.PSLS, KC.A,    KC.A,
  KC.BSPC, KC.P8,   KC.PAST, KC.PMNS,
  KC.P7,   KC.P5,   KC.P9,   KC.PPLS,
  KC.P4,   KC.P2,   KC.P6,   KC.PENT,
  KC.P1,   KC.P0,   KC.P3,   KC.PDOT,
]]

if __name__ == '__main__':
    keyboard.go()
