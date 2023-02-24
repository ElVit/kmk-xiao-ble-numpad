print("Starting")

import board

from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.statusled import statusLED
from kmk.hid import HIDModes

# KEYTBOARD SETUP
keyboard = KMKKeyboard()
layer_ext = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layer_ext, encoder_handler]

mediakeys_ext = MediaKeys()
statusled_ext = statusLED(led_pins=[board.LED_GREEN])

keyboard.extensions = [mediakeys_ext, statusled_ext]

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
LYR_STD, LYR_FN = 0, 1

TO_STD = KC.DF(LYR_STD)
TO_FN = KC.MO(LYR_FN)

# keyboard.debug_enabled = True

# KEYMAPS
keyboard.keymap = [

  # STANDARD LAYER
  # .---------------------------.
  # |  ENC | XIAO | CALC |  FN  |   --> Holding FN will activate the Function Layer
  # |------+------+------+------|
  # |  DEL |   /  |   *  |   -  |
  # |------+------+------+------|
  # |   7  |   8  |   9  |      |
  # |------+------+------+   +  |
  # |   4  |   5  |   6  |      |
  # |------+------+------+------|
  # |   1  |   2  |   3  |   E  |
  # |------+------+------|   N  |
  # |      0      |   ,  |   T  |
  # '---------------------------'
  #
  [
    KC.MUTE,   KC.PSLS,   KC.HID,    TO_FN,
    KC.BSPC,   KC.P8,     KC.PAST,   KC.PMNS,
    KC.P7,     KC.P5,     KC.P9,     KC.PPLS,
    KC.P4,     KC.P2,     KC.P6,     KC.PENT,
    KC.P1,     KC.P0,     KC.P3,     KC.PDOT,
  ],

  # FUNCTION LAYER
  # .---------------------------.
  # | ENC  | XIAO |      |      |
  # |------+------+------+------|
  # | BOOT |      |      | HID  |   --> Change between USB and BLE Mode
  # |------+------+------+------|
  # |      |      |      |  BT  |
  # |------+------+------+      |   --> Previous BLE connection [KC.BT_PRV] (is not implemented in kmk firmware yet)
  # |      |      |      | PREV |
  # |------+------+------+------|
  # |      |      |      |  BT  |
  # |------+------+------|      |   --> Next BLE connection [KC.BT_NXT] (is not implemented in kmk firmware yet)
  # |    BT-CLR   |      | NEXT |
  # '---------------------------'
  #        '-> Clear BLE connection [KC.BT_CLR]  (is not implemented in kmk firmware yet)
  [
    _______,   _______,   _______,   KC.BLE_REFRESH,
    KC.RESET,  _______,   _______,   KC.HID,
    _______,   _______,   _______,   _______,
    _______,   _______,   _______,   _______,
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
  keyboard.go(hid_type=HIDModes.BLE, secondary_hid_type=HIDModes.USB, ble_name='XiaoNumpad')
