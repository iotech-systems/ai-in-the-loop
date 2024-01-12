
import time, asyncio
import threading as th
import configparser as cp
# -- shared --
from shared.datatypes.structs import *
# -- ai space --
from ai_core.ai_structs import *
from ai_core.hiveLinkMon import hiveLinkMon
# -- sys core --
from sys_core.vtxStream import vtxStream
from sys_core.sysColors import sysColors
from sys_core.sensStream import sensStream


class aiBot(object):

   SLEEP_SECS: float = 0.008
   MAIN_SLEEP_SECS: float = 2.0
   vtx_stream: vtxStream = vtxStream(cam_code="PICAM2")
   sens_stream: sensStream = sensStream()

   def __init__(self, ini: cp.ConfigParser):
      self.ini: cp.ConfigParser = ini
      self.rxtx_arr_in: t.List[bytes] = []
      # -- -- -- --
      self.ai_hiveLnk: hiveLinkMon = hiveLinkMon()
      self.ai_mode: str = keyWords.OFF
      self.ai_acton: str = keyWords.OFF
      self.ai_status: str = keyWords.OFF
      # -- -- -- --
      self.msg_thread: th.Thread = t.Any
      self.main_thread: th.Thread = t.Any
      self.sens_thread: th.Thread = t.Any
      self.ai_status_thread: th.Thread = t.Any
      # -- -- -- --
      self.ai_tacking: aiTracking = aiTracking()
      self.hb_icons: hbIcons = hbIcons()
      self.ai_modes: aiModes = aiModes()
      self.ai_actons: aiActOn = aiActOn()

   def init(self):
      # -- init vtx cam --
      aiBot.vtx_stream.init_cam()
      aiBot.vtx_stream.start()
      # -- bot threads --
      self.sens_thread = th.Thread(target=self.__sens_thread)
      self.msg_thread = th.Thread(target=self.__msg_thread)
      self.main_thread = th.Thread(target=self.__main_thread)
      self.ai_status_thread = th.Thread(target=self.__ai_status_thread)

   def start(self):
      self.sens_thread.start()
      self.main_thread.start()
      self.msg_thread.start()

   def __msg_thread(self):
      # -- -- -- --
      def __tick() -> int:
         try:
            if len(self.rxtx_arr_in) == 0:
               return 1
            # -- -- -- --
            bytes_msg: bytes = self.rxtx_arr_in.pop()
            str_msg: str = str(bytes_msg)
            # -- -- AI MODE | ACT TO TAKE -- --
            if f"[#{aiNav.AI_NXT_MODE.name}#]" in str_msg:
               if self.ai_status == keyWords.OFF:
                  return 0
               self.ai_mode = self.ai_modes.nxt()
               self.vtx_stream.vtxoverlay.update(ai_m=self.ai_mode)
               return 0
            elif f"[#{aiNav.AI_PRV_MODE.name}#]" in str_msg:
               if self.ai_status == keyWords.OFF:
                  return 0
               self.ai_mode = self.ai_modes.prv()
               self.vtx_stream.vtxoverlay.update(ai_m=self.ai_mode)
               return 0
            # -- -- AI TAKE ACTION ON -- --
            elif f"[#{aiNav.AI_NXT_ACTON.name}#]" in str_msg:
               if self.ai_status == keyWords.OFF:
                  return 0
               self.ai_acton = self.ai_actons.nxt()
               self.vtx_stream.vtxoverlay.update(ai_a=self.ai_acton)
               self.__arm_acton()
               return 0
            elif f"[#{aiNav.AI_PRV_ACTON.name}#]" in str_msg:
               if self.ai_status == keyWords.OFF:
                  return 0
               self.ai_acton = self.ai_actons.prv()
               self.vtx_stream.vtxoverlay.update(ai_a=self.ai_acton)
               self.__arm_acton()
               return 0
            # -- -- TURN AI ON / OFF -- --
            elif f"[#{aiNav.AI_ON.name}#]" in str_msg:
               self.__set_ai_vals(keyWords.RDY)
               self.vtx_stream.vtxoverlay.update(self.ai_mode, self.ai_acton, self.ai_status)
               return 0
            elif f"[#{aiNav.AI_OFF.name}#]" in str_msg:
               self.__set_ai_vals(keyWords.OFF)
               self.vtx_stream.vtxoverlay.update(self.ai_mode, self.ai_acton, self.ai_status)
               return 0
            # -- -- HEARTBEAT -- --
            elif f"[#HB#]" in str_msg:
               self.ai_hiveLnk.hb_tick()
               self.vtx_stream.vtxoverlay.last_rf_hb = self.hb_icons.next(0)
               return 0
            # -- -- -- --
            return 100
         except Exception as e:
            print(e)
            return 200
         finally:
            pass
      # -- -- -- --
      while True:
         tick_val: int = __tick()
         time.sleep(aiBot.SLEEP_SECS)
      # -- -- -- --

   def __set_ai_vals(self, keyword):
      self.ai_mode = keyword
      self.ai_acton = keyword
      self.ai_status = keyword

   def __arm_acton(self):
      async def arm_action():
         self.ai_status = keyWords.RDY
         self.vtx_stream.vtxoverlay.update(ai_s=self.ai_status)
         await asyncio.sleep(1.2)
         self.ai_status = keyWords.ARMED
         self.vtx_stream.vtxoverlay.update(ai_s=self.ai_status)
      asyncio.run(arm_action())

   def __ai_status_thread(self):
      pass

   def __sens_thread(self):
      def __tick():
         m, p = aiBot.sens_stream.baro()
         tp = aiBot.sens_stream.temp()
         self.vtx_stream.vtxoverlay.baro_temp = (m, p, tp)
      # -- -- -- --
      while True:
         __tick()
         time.sleep(0.100)

   def __main_thread(self):
      while True:
         print("[ __main_thread: aibot ]")
         time.sleep(aiBot.MAIN_SLEEP_SECS)
