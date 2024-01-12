
from ai_core.aiBot import aiBot


class msgThread(object):

   def __init__(self, botAIself: aiBot):
      self.aibot: aiBot = botAIself

   # -- call the class --
   def __call__(self, *args, **kwargs):
      pass

   def mainLoop(self):
      # # -- -- -- --
      # def __tick() -> int:
      #    try:
      #       if len(self.rxtx_arr_in) == 0:
      #          return 1
      #       # -- -- -- --
      #       bytes_msg: bytes = self.rxtx_arr_in.pop()
      #       str_msg: str = str(bytes_msg)
      #       # -- -- AI MODE | ACT TO TAKE -- --
      #       if f"[#{aiNav.AI_NXT_MODE.name}#]" in str_msg:
      #          if self.ai_status == keyWords.OFF:
      #             return 0
      #          self.ai_mode = self.ai_modes.nxt()
      #          self.vtx_stream.vtxoverlay.update(ai_m=self.ai_mode)
      #          return 0
      #       elif f"[#{aiNav.AI_PRV_MODE.name}#]" in str_msg:
      #          if self.ai_status == keyWords.OFF:
      #             return 0
      #          self.ai_mode = self.ai_modes.prv()
      #          self.vtx_stream.vtxoverlay.update(ai_m=self.ai_mode)
      #          return 0
      #       # -- -- AI TAKE ACTION ON -- --
      #       elif f"[#{aiNav.AI_NXT_ACTON.name}#]" in str_msg:
      #          if self.ai_status == keyWords.OFF:
      #             return 0
      #          self.ai_acton = self.ai_actons.nxt()
      #          self.vtx_stream.vtxoverlay.update(ai_a=self.ai_acton)
      #          self.__arm_acton()
      #          return 0
      #       elif f"[#{aiNav.AI_PRV_ACTON.name}#]" in str_msg:
      #          if self.ai_status == keyWords.OFF:
      #             return 0
      #          self.ai_acton = self.ai_actons.prv()
      #          self.vtx_stream.vtxoverlay.update(ai_a=self.ai_acton)
      #          self.__arm_acton()
      #          return 0
      #       # -- -- TURN AI ON / OFF -- --
      #       elif f"[#{aiNav.AI_ON.name}#]" in str_msg:
      #          self.__set_ai_vals(keyWords.RDY)
      #          self.vtx_stream.vtxoverlay.update(self.ai_mode, self.ai_acton, self.ai_status)
      #          return 0
      #       elif f"[#{aiNav.AI_OFF.name}#]" in str_msg:
      #          self.__set_ai_vals(keyWords.OFF)
      #          self.vtx_stream.vtxoverlay.update(self.ai_mode, self.ai_acton, self.ai_status)
      #          return 0
      #       # -- -- HEARTBEAT -- --
      #       elif f"[#HB#]" in str_msg:
      #          self.ai_hiveLnk.hb_tick()
      #          self.vtx_stream.vtxoverlay.last_rf_hb = self.hb_icons.next(0)
      #          return 0
      #       # -- -- -- --
      #       return 100
      #    except Exception as e:
      #       print(e)
      #       return 200
      #    finally:
      #       pass
      # -- -- -- --
      while True:
         # tick_val: int = __tick()
         # time.sleep(aiBot.SLEEP_SECS)
         pass
      # -- -- -- --
