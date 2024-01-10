
import cv2, time
from picamera2 import MappedArray

colour = (0, 255, 0)
dts_origin = (20, 30)
font = cv2.FONT_HERSHEY_SIMPLEX
thickness = 2
scale = 0.8


class vtxOverlay(object):

   def __init__(self):
      pass

   def update(self, req):
      self.__datetime(req)

   def __datetime(self, req):
      timestamp = time.strftime("%Y/%m/%d %X")
      with MappedArray(req, "main") as m:
         cv2.putText(m.array, timestamp, dts_origin, font, scale, colour, thickness)
         # picam2.pre_callback = apply_timestamp
