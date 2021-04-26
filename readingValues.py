import serial

data = serial.Serial("COM3", baudrate = 9600, timeout=1)

for _ in range (0,2):   #It's giving an error for first byte so with this loop we eliminate first two byte.
    arduinoData = data.readline()

while 1:
    arduinoData = data.readline().decode()
    arduinoData = int(arduinoData)
    arduinoData = (arduinoData/1024)*5
    print(arduinoData)
   