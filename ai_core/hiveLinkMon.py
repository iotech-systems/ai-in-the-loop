
import datetime as dt
import threading as th
import time

from ai_core.ai_structs import hbIcons
from sys_core.vtxOverlay import vtxOverlay


class hiveLinkMon(object):

   on_link_broken: callable = None
   MAX_GAP_SECS: float = 0.800
   MAX_GAP_DELAY: float = 2.0

   def __init__(self, overlay: vtxOverlay):
      self.overlay: vtxOverlay = overlay
      self.dts_last_hbtick = dt.datetime.min
      self.hb_icons: hbIcons = hbIcons()
      self.run_thread: th.Thread = th.Thread(target=self.__run_thread)
      self.run_thread.start()

   def hb_tick(self):
      self.dts_last_hbtick = dt.datetime.now()

   def __run_thread(self):
      while True:
         time.sleep(0.200)
         delta: dt.timedelta = (dt.datetime.now() - self.dts_last_hbtick)
         total_seconds: float = delta.total_seconds()
         if total_seconds < hiveLinkMon.MAX_GAP_SECS:
            self.overlay.last_rf_hb = self.hb_icons.next(code=0)
            continue
         if hiveLinkMon.MAX_GAP_SECS < total_seconds < hiveLinkMon.MAX_GAP_DELAY:
            self.overlay.last_rf_hb = self.hb_icons.next(code=1)
            continue
         if total_seconds > hiveLinkMon.MAX_GAP_DELAY:
            self.overlay.last_rf_hb = self.hb_icons.next(code=2)
            continue
