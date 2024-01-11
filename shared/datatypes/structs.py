
import enum


class aiNav(enum.IntEnum):
   AI_NXT_MODE = 0
   AI_PRV_MODE = 1
   AI_NXT_ACTON = 2
   AI_PRV_ACTON = 3
   AI_ARM = 4
   AI_DISARM = 5
   AI_RUN = 6
   AI_STOP = 7


sysNavKeys: {} = {"Key.up": aiNav.AI_NXT_MODE
   , "Key.down": aiNav.AI_PRV_MODE
   , "Key.left": aiNav.AI_PRV_ACTON
   , "Key.right": aiNav.AI_NXT_ACTON
   , "Key.f2": aiNav.AI_ARM
   , "Key.f3": aiNav.AI_DISARM
   , "Key.f4": aiNav.AI_RUN
   , "Key.f5": aiNav.AI_STOP}
