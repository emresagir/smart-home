import serial, time

data = serial.Serial('COM3', 9600, timeout = 1)

def led_on():
    data.write('1'.encode())

def led_off():
    data.write('0'.encode())

time.sleep(3)
for _ in range(0, 10):
    time.sleep(1)
    led_on()
    time.sleep(1)
    led_off()
print("Done!")

