
import cv2, time, typing as t
from picamera2 import Picamera2, MappedArray


class vtxStream(object):

   picam2: Picamera2 = t.Any
   cam_conf: dict = t.Any

   def __init__(self):
      pass

   def init_cam(self, camstr: str = "PICAM2"):
      if camstr.upper() == "PICAM2":
         vtxStream.picam2 = Picamera2()
         vtxStream.cam_conf = vtxStream.picam2.create_preview_configuration()
         vtxStream.picam2.configure(vtxStream.cam_conf)
      else:
         pass


   def start_picam2(self):
      picam2.start_preview(Preview.DRM)
