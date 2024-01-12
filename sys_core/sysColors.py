
from ai_core.ai_structs import keyWords


class sysColors(object):
   red = (255, 0, 0)
   red_1 = (186, 6, 27)
   red_2 = (173, 22, 9)
   green = (0, 255, 0)
   blue = (0, 0, 255)
   blue_1 = (25, 7, 122)
   purp_0 = (136, 11, 181)
   sleep = (180, 180, 188)
   d_yellow = (242, 201, 15)
   grey_a = (127, 126, 133)
   rdy = (128, 163, 75)
   armed = (166, 117, 113)

   @staticmethod
   def str_to_color(buff: str):
      if "kill" in buff.lower():
         return sysColors.red_1
      if "trk" in buff.lower():
         return sysColors.d_yellow
      if "rtn" in buff.lower():
         return sysColors.purp_0
      if keyWords.OFF in buff:
         return sysColors.grey_a
      if keyWords.RDY in buff:
         return sysColors.rdy
      if keyWords.ARMED in buff:
         return sysColors.armed
      if ":" in buff:
         return sysColors.d_yellow
      if keyWords.AI_ACTIVE in buff:
         return sysColors.red_2
      # -- -- -- --
      return sysColors.green
