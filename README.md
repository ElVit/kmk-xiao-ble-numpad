# kmk-firmware-xiao-numpad
KMK Firmware for a XIAO BLE based Numpad

## Flash instructions

1. Download the newest CircuitPython UF2 file from [here](https://circuitpython.org/board/Seeed_XIAO_nRF52840_Sense/).  
   Make sure you dowloaded at least v7.0. I had issues with the UF2 file from SeeedStudio.
2. Press 2x the boot button (there is only one) to enter the bootloader.  
   A new drive with the name "XIAO-SENSE" should appear.
3. Copy the downloaded UF2 file to the drive "XIAO-SENSE".
4. The drive will automatically disconnect and a new drive with the name "CIRCUITPY" will appear.
5. Download the KMK frimware from (here)[https://github.com/KMKfw/kmk_firmware].
6. Extract the zip file and copy only the "kmk" folder to your "CIRCUITPY" drive (directly to the root directoy).
7. Downlaod the Adafruit BLE libraray from (here)[https://github.com/adafruit/Adafruit_CircuitPython_BLE].
8. Extract the zip file and copy only the "adafruit_ble" folder to your "CIRCUITPY" drive (directly to the root directoy).
9. Finally copy the "code.py" from this repository also to your "CIRCUITPY" drive (directly to the root directoy).

Now your Numpad is ready to be used :tada:
