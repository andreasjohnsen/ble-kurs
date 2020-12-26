import board
from pulseio import PWMOut
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.color_packet import ColorPacket

ble = BLERadio()
uart_server = UARTService()
advertisement = ProvideServicesAdvertisement(uart_server)

r = PWMOut(board.LED2_R, duty_cycle=0)
g = PWMOut(board.LED2_G, duty_cycle=0)
b = PWMOut(board.LED2_B, duty_cycle=0)

while True:
    ble.start_advertising(advertisement)  # Advertise when not connected.
    while not ble.connected:
        pass

    while ble.connected:
        packet = Packet.from_stream(uart_server)
        if isinstance(packet, ColorPacket):
            print(packet.color)
            dc = [-257*c+65535 for c in packet.color]
            r.duty_cycle, g.duty_cycle, b.duty_cycle = dc