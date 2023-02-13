print("Starting")

import board

from kmk.hid import HIDModes
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.statusled import statusLED

# KEYTBOARD SETUP
keyboard = KMKKeyboard()
layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]

mediaKeys = MediaKeys()
statusLED = statusLED(led_pins=[board.LED])

keyboard.extensions = [mediaKeys, statusLED]

# SWITCH MATRIX
keyboard.col_pins = (board.D10,board.D9,board.D8,board.D7,)
keyboard.row_pins = (board.D0,board.D1,board.D2,board.D3,board.D6,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ENCODERS
encoder_handler.pins = ((board.D4, board.D5, None, False, 2),)

# FILLER KEYS
_______ = KC.TRNS
xxxxxxx = KC.NO
tbdtbd = KC.A

# LAYERS
LYR_STD, LYR_BT = 0, 1

TO_STD = KC.DF(LYR_STD)
TO_BT = KC.MO(LYR_BT)

# KEYMAPS
keyboard.keymap = [
  # STANDARD LAYER
  [
    KC.MUTE,   KC.PSLS,   tbdtbd,    TO_BT,
    KC.BSPC,   KC.P8,     KC.PAST,   KC.PMNS,
    KC.P7,     KC.P5,     KC.P9,     KC.PPLS,
    KC.P4,     KC.P2,     KC.P6,     KC.PENT,
    KC.P1,     KC.P0,     KC.P3,     KC.PDOT,
  ],
  # BLUETOOTH LAYER
  [
    _______,   _______,   _______,   _______, # KC.HID --> Change HID Mode
    _______,   _______,   _______,   _______, # KC.BT_NXT --> Next BLE connection
    _______,   _______,   _______,   _______, # KC.BT_PRV --> Previous BLE connection
    _______,   _______,   _______,   _______, # KC.BT_CLR --> Clear BLE connection
    _______,   _______,   _______,   _______,
  ]
]

# ROTARY ENCODER
encoder_handler.map = [
    # STANDARD LAYER
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
    # BLUETOOTH LAYER
    ((KC.UP,   KC.DOWN, KC.MUTE),),
]

if __name__ == '__main__':
    # keyboard.go(hid_type=HIDModes.BLE, secondary_hid_type=HIDModes.USB, ble_name='XiaoNumpad')
    keyboard.go()
