
import cv2, time
from picamera2 import MappedArray
# -- system --
from sys_core.sysColors import sysColors


# -- color r, g, b --
col_green = (0, 255, 0)
dts_org = (20, 30)
ai_mode_org = (440, 30)
ai_stat_org = (450, 60)
baro_org = (80, 466)
targ_org_s = (210, 130)
targ_org_e = (430, 350)
# -- -- text & etc -- --
scale = 0.72
font = cv2.FONT_HERSHEY_SIMPLEX


class vtxOverlay(object):

   def __init__(self):
      self.ai_mode: str = "OFF"
      self.ai_stat: str = "RDY"
      self.baro_temp: () = (0.0, 0.0, 0.0)
      self.targ_box_color = sysColors.sleep
      self.draw_thickness = 2
      self.last_rf_hb: int = 0

   """
      -- -- -- --
   """
   def update(self, req):
      with MappedArray(req, "main") as m:
         self.__datetime(m)
         self.__ai_mode(m)
         self.__ai_status(m)
         self.__baro_temp(m)
         self.__target_box(m)

   """
      -- -- -- --
   """
   def __datetime(self, m: MappedArray):
      timestamp = time.strftime("%Y/%m/%d %X")
      cv2.putText(m.array, timestamp, dts_org, font, scale
         , sysColors.green, self.draw_thickness)

   """
      -- -- -- --
   """
   def __ai_mode(self, m: MappedArray):
      mode: str = f"AIm: {self.ai_mode}"
      cv2.putText(m.array, mode, ai_mode_org, font, scale
         , sysColors.green, self.draw_thickness)

   """
      -- -- -- --
   """
   def __ai_status(self, m: MappedArray):
      stat: str = f"AIs: {self.ai_stat}"
      cv2.putText(m.array, stat, ai_stat_org, font, scale
         , sysColors.green, self.draw_thickness)

   """
      -- -- -- --
   """
   def __baro_temp(self, m: MappedArray):
      alt, h, t = self.baro_temp
      buff: str = f"A: {alt}m P: {h}hPa T: {t}*C"
      cv2.putText(m.array, buff, baro_org, font, scale
         , sysColors.green, self.draw_thickness)

   """
      -- -- -- --
   """
   def __target_box(self, m: MappedArray):
      cv2.rectangle(m.array, targ_org_s, targ_org_e
         , self.targ_box_color, self.draw_thickness)
