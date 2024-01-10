
import typing as t


class sensStream(object):

   def __init__(self):
      pass

   """
      BMP180 - BST-BMP180-DS000-09 | Rev: 2.5 | April 2013 Bosch Sensortec
      © Bosch Sensortec GmbH reserves all rights even in the event of industrial property 
      rights. We reserve all rights of disposal such as copying and passing on to third
      parties. BOSCH and the symbol are registered trademarks of Robert Bosch GmbH, Germany.
      Note: Specifications within this document are subject to change without notice.
      BMP180 DIGITAL PRESSURE SENSOR
      Pressure range: 300 ... 1100hPa (+9000m ... -500m relating to sea level)
   """
   def baro(self) -> t.Tuple[float, float]:
      # -- meters, hPa
      return 200.00, 989.45

   def temp(self) -> float:
      return 14.6
