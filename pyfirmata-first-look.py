from pyfirmata import Arduino, util
import time

board = Arduino('COM3')

board.digital[13].write(0)


it = util.Iterator(board)
it.start()
