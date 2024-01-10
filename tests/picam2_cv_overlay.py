#!/usr/bin/env python3

import cv2, time
from picamera2 import Picamera2, MappedArray


picam2 = Picamera2()
colour = (0, 255, 0)
origin = (10, 30)
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 1
thickness = 2


def apply_timestamp(request):
   timestamp = time.strftime("%Y/%m/%d %X")
   with MappedArray(request, "main") as m:
      cv2.putText(m.array, timestamp, origin, font, scale, colour, thickness)
      picam2.pre_callback = apply_timestamp
      # picam2.start(show_preview=True)


picam2.pre_callback = apply_timestamp
picam2.start(show_preview=True)


while True:
   print("Preview.DRM")
   time.sleep(4.0)
