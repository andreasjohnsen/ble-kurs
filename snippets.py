from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import Advertisement, to_hex

ble = BLERadio()
print("scanning")

for advertisement in ble.start_scan(minimum_rssi=-75):
    name = advertisement.complete_name or advertisement.short_name

    if name:
        print(name, advertisement.address.type)

        #try:
        #    print(advertisement)
        #except:
        #    print("Ups...")

print("scan done")
