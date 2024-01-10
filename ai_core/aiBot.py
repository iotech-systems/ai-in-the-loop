
import time
import typing as t
import threading as th
import configparser as cp
# -- system --
from sys_core.vtxStream import vtxStream


class aiBot(object):

   MAIN_SLEEP_SECS: float = 2.0
   SLEEP_SECS: float = 0.008
   vtx_stream: vtxStream = vtxStream(cam_code="PICAM2")

   def __init__(self, ini: cp.ConfigParser):
      self.ini: cp.ConfigParser = ini
      self.rxtx_arr_in: t.List[bytes] = []
      self.msg_thread: th.Thread = t.Any
      self.main_thread: th.Thread = t.Any

   def init(self):
      # -- init vtx cam --
      aiBot.vtx_stream.init_cam()
      aiBot.vtx_stream.start()
      # -- bot threads --
      self.msg_thread = th.Thread(target=self.__msg_thread)
      self.main_thread = th.Thread(target=self.__main_thread)

   def start(self):
      self.main_thread.start()
      self.msg_thread.start()

   def __msg_thread(self):
      # -- -- -- --
      def __tick() -> int:
         try:
            if len(self.rxtx_arr_in) == 0:
               return 1
            bmsg: bytes = self.rxtx_arr_in.pop()
            print(f"<<<<<<<<<<<<[ {bmsg} ]>>>>>>>>>>>>>>")
            return 0
         except Exception as e:
            print(e)
            return 2
         finally:
            pass
      # -- -- -- --
      while True:
         tick_val: int = __tick()
         time.sleep(aiBot.SLEEP_SECS)
      # -- -- -- --

   def __main_thread(self):
      while True:
         print("[ __main_thread: aibot ]")
         time.sleep(aiBot.MAIN_SLEEP_SECS)
