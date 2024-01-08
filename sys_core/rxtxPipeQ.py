
import time, threading as th
import serial, typing as t
# -- -- -- --
from sys_core.utils import utils


AI_DEV_PATH = "/dev/ttyAI"


class rxtxPipeQ(object):

   """
      # dev_path, baud, qtag
   """
   def __init__(self, pipe_str: str):
      self.info_arr: [] = pipe_str.split(",")
      self.dev_path, self.baud, self.qtag = self.info_arr
      self.baud: int = int(self.baud)
      self.rxtx: serial.Serial = t.Any
      self.rxtx_thread: th.Thread = t.Any
      self.pipe_thread: th.Thread = t.Any
      self.rxtx_buff_in: bytearray = bytearray()

   def init(self):
      try:
         print(f"[ qpipe:init - {self.qtag} ]")
         if self.dev_path != AI_DEV_PATH:
            self.rxtx = serial.Serial(port=self.dev_path, baudrate=self.baud)
            if not self.rxtx.is_open:
               self.rxtx.open()
            else:
               self.rxtx_thread = th.Thread(target=self.__rxtx_thread)
         elif self.dev_path == AI_DEV_PATH:
            self.rxtx_thread = th.Thread(target=self.__ai_thread)
      except Exception as e:
         utils.log_err(e)
      # -- -- -- --
      self.pipe_thread = th.Thread(target=self.__pipe_thread)

   def start(self):
      self.rxtx_thread.start()
      self.pipe_thread.start()

   def __rxtx_thread(self):
      self.rxtx_buff_in.clear()
      while True:
         try:
            if self.rxtx.in_waiting > 0:
               tmpbuff: bytes = self.rxtx.read_all()
               tmpstr: str = tmpbuff.decode("utf-8").strip()
               print(f"<< {self.qtag} | {tmpstr} >>")
               if tmpstr in ["<CLR>"]:
                  self.rxtx_buff_in.clear()
               else:
                  self.rxtx_buff_in.extend(tmpbuff)
            else:
               time.sleep(0.01)
         except Exception as e:
            utils.log_err(f"e: {self.qtag} | {e}")

   def __ai_thread(self):
      while True:
         try:
            print(f"__ai_thread | qtag: {self.qtag}")
            time.sleep(4.0)
         except Exception as e:
            utils.log_err(f"e: {self.qtag} | {e}")

   def __pipe_thread(self):
      while True:
         try:
            print(f"__pipe_thread | qtag: {self.qtag}")
            print(f"\trxtx_in: {self.rxtx_buff_in}")
            time.sleep(2.0)
         except Exception as e:
            utils.log_err(e)
