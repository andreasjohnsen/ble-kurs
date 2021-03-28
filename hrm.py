import board
from pulseio import PWMOut
from adafruit_ble import BLERadio, __version__
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble_heart_rate import HeartRateService
from adafruit_ble.services.standard.device_info import DeviceInfoService

from adafruit_ble.services import Service
from adafruit_ble.uuid import StandardUUID
from adafruit_ble.characteristics.string import FixedStringCharacteristic
from adafruit_ble.characteristics.int import Uint16Characteristic
from adafruit_ble.characteristics import Characteristic

import _bleio

import digitalio

import time


pin = digitalio.DigitalInOut(board.SW1)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP

button_state = True
time_last_beat = time_current_beat = 0


def prettify(mac_string):
    return ':'.join('%02x' % b for b in mac_string)     # in Python 3: <bytes>.hex(":")

class MyService(Service):
    uuid = StandardUUID(0x180D) // Heart Reate Measurement Service
    hr = Uint16Characteristic(properties=Characteristic.NOTIFY, uuid=StandardUUID(0x2A37))

class MyServiceTemp(Service):
    uuid = StandardUUID(0x1809)  // Temperature Measurement Service
    hr = Uint16Characteristic(properties=Characteristic.NOTIFY, uuid=StandardUUID(0x2A37))

ble = BLERadio()
# hrs = HeartRateService()

device_info = DeviceInfoService(
    software_revision=__version__, manufacturer="Adafruit Industries"
)

myService = MyService()

ble.name = "myHeart"

print(prettify(ble.address_bytes))

advertisement = ProvideServicesAdvertisement(myService)

while True:

    ble.start_advertising(advertisement)  # Advertise when not connected.
    while not ble.connected:
        pass

    print("connected!")
    while ble.connected:
        # myService.hr = 0x22 << 8    # 0x2200
        time.sleep(0.1)
        pressed = pin.value
        if pressed != button_state:
            if button_state:
                if time_last_beat == 0:
                    time_last_beat = time.monotonic()
                else:
                    bpm = min(255, int(60/(time.monotonic() - time_last_beat)))
                    print(bpm)
                    myService.hr = bpm << 8
                    time_last_beat = time.monotonic()
            button_state = pressed