
from sys_core.sys_structs import *


class targetBox(object):

   """
      targ_org_s = (210, 130)
      targ_org_e = (430, 350)
   """
   def __init__(self, scr_wh: () = (640, 480), box_wh: () = (220, 220)):
      self.scr_w, self.scr_h = scr_wh
      self.box_w, self.box_h = box_wh

   def move(self, x: int, y: int):
      pass

   def re_center(self):
      pass

   def calc_location(self) -> targetBoxLocation | None:
      return None
