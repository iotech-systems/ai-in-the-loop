
import cv2, time
from picamera2 import MappedArray

colour = (0, 255, 0)
dts_org = (20, 30)
mode_org = (380, 30)
targ_org_s = (210, 130)
targ_org_e = (430, 350)
targ_sleep_color = (100, 100, 100)
targ_track_color = ()
targ_kill_color = ()
font = cv2.FONT_HERSHEY_SIMPLEX
thickness = 2
scale = 0.8


class vtxOverlay(object):

   def __init__(self):
      pass

   def update(self, req):
      with MappedArray(req, "main") as m:
         self.__datetime(m)
         self.__mode(m)
         self.__target_box(m)

   def __datetime(self, m: MappedArray):
      timestamp = time.strftime("%Y/%m/%d %X")
      cv2.putText(m.array, timestamp, dts_org, font, scale, colour, thickness)

   def __mode(self, m: MappedArray):
      mode = time.strftime("mode: pilot")
      cv2.putText(m.array, mode, mode_org, font, scale, colour, thickness)

   def __target_box(self, m: MappedArray):
      cv2.rectangle(m.array, targ_org_s, targ_org_e, targ_sleep_color, thickness)
