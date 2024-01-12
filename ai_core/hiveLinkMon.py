
import datetime as dt
import threading as th
import time, asyncio
# -- system --
from ai_core.ai_structs import hbIcons, keyWords
from sys_core.vtxOverlay import vtxOverlay


class hiveLinkMon(object):

   MAX_GAP_SECS: float = 0.800
   MAX_GAP_DELAY: float = 2.0
   MAX_GAP_CALLBACK: float = 4.0

   def __init__(self, overlay: vtxOverlay, ai_status: str):
      self.overlay: vtxOverlay = overlay
      self.ai_status: str = ai_status
      self.dts_last_hbtick = dt.datetime.min
      self.hb_icons: hbIcons = hbIcons()
      self.run_thread: th.Thread = th.Thread(target=self.__run_thread)
      self.run_thread.start()
      self.link_status: int = 0

   def hb_tick(self):
      self.dts_last_hbtick = dt.datetime.now()

   def __run_thread(self):
      # -- -- -- --
      while True:
         time.sleep(0.200)
         delta: dt.timedelta = (dt.datetime.now() - self.dts_last_hbtick)
         total_seconds: float = delta.total_seconds()
         if total_seconds < hiveLinkMon.MAX_GAP_SECS:
            self.overlay.last_rf_hb = self.hb_icons.next(code=0)
            self.link_status = 0
            continue
         if hiveLinkMon.MAX_GAP_SECS < total_seconds < hiveLinkMon.MAX_GAP_DELAY:
            self.overlay.last_rf_hb = self.hb_icons.next(code=1)
            self.link_status = 1
            continue
         if total_seconds > hiveLinkMon.MAX_GAP_DELAY:
            self.overlay.last_rf_hb = self.hb_icons.next(code=2)
            self.link_status = 2
            continue
