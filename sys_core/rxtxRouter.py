
import time
import typing as t
import threading as th
import configparser as cp
# -- -- -- --
from sys_core.utils import utils
from sys_core.rxtxPipeQ import rxtxPipeQ


class rxtxRouter(object):

   def __init__(self, ini: cp.ConfigParser):
      self.ini: cp.ConfigParser = ini
      self.ini_sec: cp.SectionProxy = self.ini["RXTX_PIPES"]
      self.pipes_arr: [] = None
      self.rxtx_pqs: t.List[rxtxPipeQ] = []
      self.router_thread: th.Thread = th.Thread(target=self.__router_thread)

   def load_ini(self) -> int:
      try:
         tmp: str = self.ini_sec["PIPES"]
         print(tmp)
         if tmp in ["", None]:
            pass
         self.pipes_arr = tmp.split("\n")
         self.rxtx_pqs = [rxtxPipeQ(pipe_str=pstr) for pstr in self.pipes_arr]
         return 0
      except Exception as e:
         utils.log_err(e)
         return 1
      finally:
         pass

   def start(self) -> int:
      self.router_thread.start()
      for rxtx_item in self.rxtx_pqs:
         rxtx_item.init()
         rxtx_item.start()
      return 0

   def stop(self) -> int:
      return 0

   def __router_thread(self):
      print("\n[ __router_thread ]\n")
      rxtx_air: rxtxPipeQ = [i for i in self.rxtx_pqs if str(i.qtag).strip() == "AIR_RXTX"][0]
      rxtx_fc: rxtxPipeQ = [i for i in self.rxtx_pqs if str(i.qtag).strip() == "FC_RXTX"][0]
      rxtx_ai: rxtxPipeQ = [i for i in self.rxtx_pqs if str(i.qtag).strip() == "AI_RXTX"][0]
      print(f"|< {rxtx_air} | {rxtx_fc} | {rxtx_ai} >|")
      while True:
         try:
            # -- read air & write fc --
            if len(rxtx_air.rxtx_arr_in) > 0:
               btmp: bytes = rxtx_air.rxtx_arr_in.pop()
               rxtx_fc.rxtx.write(btmp)
            # -- -- -- --
            time.sleep(0.01)
         except Exception as e:
            utils.log_err(e)
         finally:
            pass
