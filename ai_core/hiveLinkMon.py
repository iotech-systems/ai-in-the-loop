
import datetime as dt
import threading as th


class hiveLinkMon(object):

   MAX_GAP_MILLISECS: int = 480

   def __init__(self):
      self.dts_last_hbtick = dt.datetime.now()

   def update(self, d: object = None):
      delta: dt.timedelta = (dt.datetime.now() - self.dts_last_hbtick)
      delta_ms: int = int(delta.microseconds / 1000)

   def hb_tick(self):
      pass
