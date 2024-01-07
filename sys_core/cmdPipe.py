
import serial


class cmdPipe(object):

   def __init__(self):
      self.ser_from_air: serial.Serial = serial.Serial()
      self.ser_to_fc = None
