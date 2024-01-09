
import serial as ser
import threading as th


class devPort(object):

   THLOCK: th.Lock = th.Lock()

   def __init__(self, dev: str, baud: int):
      self.dev: str = dev
      self.baud: int = baud
      self.ser: ser.Serial = ser.Serial(port=self.dev, baudrate=self.baud)
      if not self.ser.is_open:
         self.ser.open()

   def send_bytes(self, msg: bytes):
      try:
         devPort.THLOCK.acquire()
         self.ser.write(msg)
      except Exception as e:
         print(e)
      finally:
         devPort.THLOCK.release()
