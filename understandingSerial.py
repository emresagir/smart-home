import serial, time
#from speechRecognition import lightSit
from tester import lightSit

timeFlag = 0

data = serial.Serial('COM3', 9600, timeout = 1)

for _ in range (0,2):   #It's giving an error for first byte so with this loop we eliminate first two byte.
    arduinoData = data.readline()

def led_on():
    data.write('1'.encode())

def led_off():
    data.write('0'.encode())

#while 1:
#   recData = data.readline().decode()
#   recData = int(recData)
#   recData = (recData/1024)*5
#   print(recData)
    
while 1:
    timeFlag = timeFlag + 1
    print(lightSit)
    if lightSit == 0:
        led_off()

    if lightSit == 1:
        led_on()

# for _ in range(0, 10):
#     time.sleep(1)
#     led_on()
#     time.sleep(1)
#     led_off()


    
#print("Done!")

