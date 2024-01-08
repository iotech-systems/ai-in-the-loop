
import serial as ser


class devPort(object):

   def __init__(self, dev: str, baud: int):
      self.dev: str = dev
      self.baud: int = baud
      self.ser: ser.Serial = ser.Serial(port=self.dev, baudrate=self.baud)
      if not self.ser.is_open:
         self.ser.open()
