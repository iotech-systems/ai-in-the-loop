
import typing as t
from threading import Lock
from collections import deque
from shared.datatypes.structs import aiNavDir


class keyWords(object):
   ON: str = "ON"
   OFF: str = "OFF"
   ARMED: str = "ARMED"
   RDY: str = "RDY"
   ACTIVE: str = "ACTIVE"


class aiModes(object):

   m: [] = ["KILL/cm", "KILL/sm", "SEEK/kill/cm", "TRK/v0", "TRK/v1", "TRK/v2"
      , "TRK/onscr", "RTN/rfHB:OK", "RTN/home"]

   def __init__(self):
      self.values: deque = deque()
      self.values.extend(aiModes.m)
      self.dir: aiNavDir = aiNavDir.FORWARD

   def nxt(self) -> str:
      if self.dir == aiNavDir.REVERSE:
         self.values.reverse()
         self.dir = aiNavDir.FORWARD
      tmp: str = self.values.popleft()
      self.values.append(tmp)
      return tmp

   def prv(self) -> str:
      if self.dir == aiNavDir.FORWARD:
         self.values.reverse()
         self.dir = aiNavDir.REVERSE
      tmp: str = self.values.popleft()
      self.values.append(tmp)
      return tmp

class aiActOn(object):

   m: [] = ["rfHB:err", "key:enter"]

   def __init__(self):
      self.values: deque = deque()
      self.values.extend(aiActOn.m)
      self.dir: aiNavDir = aiNavDir.FORWARD

   def nxt(self) -> str:
      if self.dir == aiNavDir.REVERSE:
         self.values.reverse()
         self.dir = aiNavDir.FORWARD
      tmp: str = self.values.popleft()
      self.values.append(tmp)
      return tmp

   def prv(self) -> str:
      if self.dir == aiNavDir.FORWARD:
         self.values.reverse()
         self.dir = aiNavDir.REVERSE
      tmp: str = self.values.popleft()
      self.values.append(tmp)
      return tmp


class aiTracking(object):

   def __init__(self):
      self.modes: deque = deque()
      self.modes.extend(["TRACK-V0", "TRACK-V1", "TRACK-V2", "ON-SCR-TRACK"])

   def next(self) -> str:
      tmp: str = self.modes.popleft()
      self.modes.append(tmp)
      return tmp


class hbIcons(object):

   bullet = u'\u0095'
   icoLock: Lock = Lock()
   okIco: [] = ["O", "*"]
   wrIco: [] = ["?", "!"]
   erIco: [] = ["X", "-"]

   def __init__(self):
      self.icoOK: deque = deque()
      self.icoOK.extend(hbIcons.okIco)
      self.icoWr: deque = deque()
      self.icoWr.extend(hbIcons.wrIco)
      self.icoEr: deque = deque()
      self.icoEr.extend(hbIcons.erIco)
      self.symbols: [] = [self.icoOK, self.icoWr, self.icoEr]

   def next(self, code: 0 = int) -> str:
      try:
         hbIcons.icoLock.acquire()
         sym: str = self.symbols[code].popleft()
         self.symbols[code].append(sym)
         return sym
      except Exception as e:
         print(e)
         return ""
      finally:
         hbIcons.icoLock.release()
