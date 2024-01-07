
import serial as ser
import threading as th
# -- -- -- --
from datatypes.serInfo import serInfo


class cmdPipe(object):

   def __init__(self):
      self.ser_from_air: ser.Serial = ser.Serial()
      self.ser_to_fc = None
