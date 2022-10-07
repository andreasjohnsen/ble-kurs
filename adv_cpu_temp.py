from adafruit_ble import BLERadio
from adafruit_ble.advertising import Advertisement

import struct
import time
from microcontroller import cpu

ble = BLERadio()
ble.name = "ARJxxx1"


myAdv = Advertisement()
myAdv.short_name = "TestXXX"
myAdv.tx_power = -4

#myAdv.data_dict[0xff] = struct.pack("<H", 0x33ff)
#myAdv.data_dict[0xff] = struct.pack("<H", 0x00c4) + "Hallo verden".encode("utf-8")

print(int(cpu.temperature))

# ble.start_advertising(myAdv)


i = 0

while True:
    temp = int(cpu.temperature)
    print(temp)
    myAdv.data_dict[0xff] = struct.pack("<HB", 0x00c4, temp)
    ble.start_advertising(myAdv)
    time.sleep(1)
    ble.stop_advertising()
    i = i +1
    pass
