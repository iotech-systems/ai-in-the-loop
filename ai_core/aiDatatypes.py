

class aiKillMode(object):

   def __init__(self):
      self.modes: [] = ["KILL-CM", "KILL-SM"]

   def next(self) -> str:
      tmp: str = self.modes.pop()
      self.modes.append(tmp)
      return tmp
