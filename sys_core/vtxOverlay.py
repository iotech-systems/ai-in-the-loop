
import cv2, time
from picamera2 import MappedArray
# -- system --
from sys_core.sysColors import sysColors


# color r,g,b
col_green = (0, 255, 0)
dts_org = (20, 30)
mode_org = (380, 30)
targ_org_s = (210, 130)
targ_org_e = (430, 350)
font = cv2.FONT_HERSHEY_SIMPLEX
thickness = 2
scale = 0.8


class vtxOverlay(object):

   def __init__(self):
      self.ai_mode: str = "pilot"
      self.targ_box_color = sysColors.sleep

   def update(self, req):
      with MappedArray(req, "main") as m:
         self.__datetime(m)
         self.__mode(m)
         self.__target_box(m)

   def __datetime(self, m: MappedArray):
      timestamp = time.strftime("%Y/%m/%d %X")
      cv2.putText(m.array, timestamp, dts_org, font, scale, sysColors.green, thickness)

   def __mode(self, m: MappedArray):
      mode: str = f"mode: {self.ai_mode}"
      cv2.putText(m.array, mode, mode_org, font, scale, sysColors.green, thickness)

   def __target_box(self, m: MappedArray):
      cv2.rectangle(m.array, targ_org_s, targ_org_e, self.targ_box_color, thickness)
