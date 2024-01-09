
import time, uuid
import typing as t
import threading as th
from pynput import keyboard as kbd
# -- core --
from core.devPort import devPort


class radioSim(object):

   # 9600, 14400, 19200, 38400, 57600, 115200
   # run at 100hz so every 10ms
   # SLEEP_SECS: float = 0.01
   SLEEP_SECS: float = 1.0

   def __init__(self, dev: str, baud: int):
      self.dev: str = dev
      self.baud: int = baud
      self.call_cnt: int = 0
      self.dev_port: devPort = t.Any
      self.__main_loop: th.Thread = t.Any
      self.__kbd_thread: th.Thread = t.Any

   def init(self):
      self.dev_port: devPort = devPort(dev=self.dev, baud=self.baud)
      self.__main_loop: th.Thread = th.Thread(target=self.__main_loop_thread)
      self.__kbd_thread: th.Thread = th.Thread(target=self.__kbd_start)

   def start(self):
      self.__main_loop.start()
      self.__kbd_thread.start()

   def __kbd_start(self):
      with kbd.Listener(on_press=self.__on_key_press,
         on_release=self.__on_key_release) as _l:
         _l.join()

   def __main_loop_thread(self):
      # -- -- -- --
      def __tick():
         try:
            bbuff: bytes = self.__get_next_buff()
            self.dev_port.send_bytes(bbuff)
         except Exception as e:
            print(e)
      # -- -- -- --
      while True:
         __tick()
         time.sleep(radioSim.SLEEP_SECS)

   def __get_next_buff(self) -> bytes:
      buff_str: str = str(uuid.uuid4()).upper() + "\n"
      return buff_str.encode("utf-8")

   def __on_key_press(self, key: kbd.Key):
      pass

   def __on_key_release(self, key: kbd.Key):
      try:
         ai_msg: bytes = self.__get_ai_tag(key)
         self.dev_port.send_bytes(ai_msg)
      except Exception as e:
         print(e)
      finally:
         pass

   def __get_ai_tag(self, key: kbd.Key) -> bytes | None:
      if key == kbd.Key.down:
         ai_buff = "kbd.Key.down"
      elif key == kbd.Key.up:
         ai_buff = "kbd.Key.up"
      elif key == kbd.Key.left:
         ai_buff = "kbd.Key.left"
      elif key == kbd.Key.right:
         ai_buff = "kbd.Key.right"
      else:
         print("other key")
         return None
      # -- -- -- --
      buff: str = f"{str(uuid.uuid1().hex[:16])}_AI:[{ai_buff}]_{str(uuid.uuid1().hex[:16])}"
      return bytes(buff, "utf-8")
