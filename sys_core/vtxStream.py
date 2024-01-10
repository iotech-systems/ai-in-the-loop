import os
import threading as th
import cv2, time, typing as t
from picamera2 import Picamera2, MappedArray, Preview
# -- -- system -- --
from sys_core.vtxOverlay import vtxOverlay


CONF: dict = {"size": (640, 480)}


class vtxStream(object):

   logoimg: str = "_media/logo1.png"
   cam: Picamera2 = t.Any
   cam_conf: dict = t.Any

   def __init__(self, cam_code: str = "PICAM2"):
      self.cam_code: str = cam_code.upper()
      self.vtxoverlay: vtxOverlay = vtxOverlay()
      self.main_thread: th.Thread = th.Thread(target=self.__main_thread)

   def init_cam(self):
      if self.cam_code == "PICAM2":
         vtxStream.cam = Picamera2()
         vtxStream.cam.pre_callback = self.vtxoverlay.update
         vtxStream.cam_conf = vtxStream.cam.create_preview_configuration(CONF)
         vtxStream.cam.configure(vtxStream.cam_conf)
      else:
         pass

   def start(self):
      # -- vtx start --
      vtxStream.cam.start_preview(Preview.DRM)
      vtxStream.cam.start(show_preview=True)
      if os.path.exists(vtxStream.logoimg):
         logo_overlay = cv2.imread(vtxStream.logoimg, cv2.IMREAD_UNCHANGED)
         vtxStream.cam.set_overlay(logo_overlay)
      else:
         print(f"PathNotFound: {vtxStream.logoimg}")
         print(f"cwd: {os.getcwd()}")
         # -- -- -- --
      self.main_thread.start()

   def __main_thread(self):
      while True:
         print("[ vtxStream: __main_thread ]")
         time.sleep(4.0)
