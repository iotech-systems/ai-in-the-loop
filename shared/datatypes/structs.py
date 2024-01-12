
import enum


class aiNavDir(enum.IntEnum):
   FORWARD = 0
   REVERSE = 1


class aiNav(enum.IntEnum):
   AI_NXT_MODE = 0
   AI_PRV_MODE = 1
   AI_NXT_ACTON = 2
   AI_PRV_ACTON = 3
   AI_ON = 4
   AI_OFF = 5
   AI_RUN = 6
   AI_STOP = 7


sysNavKeys: {} = {"Key.up": aiNav.AI_NXT_MODE
   , "Key.down": aiNav.AI_PRV_MODE
   , "Key.left": aiNav.AI_PRV_ACTON
   , "Key.right": aiNav.AI_NXT_ACTON
   , "Key.f2": aiNav.AI_ON
   , "Key.f3": aiNav.AI_OFF
   , "Key.f4": aiNav.AI_RUN
   , "Key.f5": aiNav.AI_STOP}

