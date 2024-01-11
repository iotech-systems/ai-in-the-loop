
import time, uuid
import typing as t
import threading as th
from pynput import keyboard as kbd
# -- core --
from core.datatypes.structs import *
from core.devPort import devPort


class radioSim(object):

   # 9600, 14400, 19200, 38400, 57600, 115200
   # 0.01 run at 100hz so every 10ms
   # 0.02 run at 50hz so every 20ms
   # SLEEP_SECS: float = 0.02
   SLEEP_SECS: float = 2.0
   HB_SLEEP_SECS: float = 0.25

   def __init__(self, dev: str, baud: int):
      self.dev: str = dev
      self.baud: int = baud
      self.call_cnt: int = 0
      self.dev_port: devPort = t.Any
      self.main_thread: th.Thread = t.Any
      self.kbd_thread: th.Thread = t.Any
      self.hb_thread: th.Thread = t.Any

   def init(self):
      self.dev_port: devPort = devPort(dev=self.dev, baud=self.baud)
      self.main_thread: th.Thread = th.Thread(target=self.__main_thread)
      self.hb_thread: th.Thread = th.Thread(target=self.__hb_thread)
      # -- this should be last --
      self.kbd_thread: th.Thread = th.Thread(target=self.__kbd_start)

   def start(self):
      self.main_thread.start()
      self.hb_thread.start()
      # -- -- this has to be last -- --
      self.kbd_thread.start()

   def __hb_thread(self):
      time.sleep(2.0)
      print("[ __hb_thread ]")
      while True:
         try:
            bmsg: bytes = self.__get_ai_heartbeat()
            self.dev_port.send_bytes(msg=bmsg, withEcho=True)
            time.sleep(radioSim.HB_SLEEP_SECS)
         except Exception as e:
            print(e)
         finally:
            pass

   def __kbd_start(self):
      with kbd.Listener(on_press=self.__on_key_press,
         on_release=self.__on_key_release) as _l:
         _l.join()

   def __main_thread(self):
      def __tick():
         try:
            bbuff: bytes = self.__get_next_buff()
            self.dev_port.send_bytes(bbuff, withEcho=True)
         except Exception as e:
            print(e)
      # -- -- -- --
      while True:
         __tick()
         time.sleep(radioSim.SLEEP_SECS)
      # -- -- -- --

   def __get_next_buff(self) -> bytes:
      buff_str: str = str(uuid.uuid4()).upper() + "\n"
      return buff_str.encode("utf-8")

   def __on_key_press(self, key: kbd.Key):
      pass

   def __on_key_release(self, key: kbd.Key):
      try:
         ai_msg: bytes = self.__get_ai_tag(key)
         self.dev_port.send_bytes(ai_msg, withEcho=True)
      except Exception as e:
         print(e)
      finally:
         pass

   """
      ai_cmd = "kbd.Key.down", ai_cmd = "kbd.Key.up"
   """
   def __get_ai_tag(self, key: kbd.Key) -> bytes | None:
      ai_cmd: str = self.__key_to_cmd(key)
      # -- -- -- --
      xbuff0: str = uuid.uuid1().hex[:16]
      xbuff1: str = uuid.uuid1().hex[:16]
      buff: str = f"{xbuff0}_AI:[#{ai_cmd}#]_{xbuff1}"
      # -- -- -- --
      return bytes(buff, "utf-8")

   def __get_ai_heartbeat(self):
      xbuff0: str = uuid.uuid1().hex[:16]
      xbuff1: str = uuid.uuid1().hex[:16]
      return bytes(f"{xbuff0}_AI:[#HB#]_{xbuff1}", "utf-8")

   def __key_to_cmd(self, key: kbd.Key) -> str:
      if key == kbd.Key.down:
         return sysNav.PRV_MODE
      elif key == kbd.Key.up:
         return sysNav.NXT_MODE
      elif key == kbd.Key.left:
         return sysNav.PRV_ACTON
      elif key == kbd.Key.right:
         return sysNav.NXT_ACTON
      elif key == kbd.Key.enter:
         return str(kbd.Key.enter)
      else:
         print(f"other key: {key}")
         return ""
