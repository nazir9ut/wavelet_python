#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image  # PIL
import numpy
import pylab

from pywt import WaveletPacket2D
import numpy as np
import cv2

im = Image.open("/home/naz/Desktop/src_big_screenshot_11.06.2015.png").convert('L')



arr = numpy.fromstring(im.tostring(), numpy.uint8)
arr.shape = (im.size[1], im.size[0])



wp2 = WaveletPacket2D(arr, 'haar', 'sym', maxlevel=2)



# pylab.imshow(arr, interpolation="nearest", cmap=pylab.cm.gray)


path = ['d', 'v', 'h', 'a']



#mod = lambda x: x
#mod = lambda x: abs(x)
mod = lambda x: numpy.sqrt(abs(x))


print("-----------------")
# print(wp2["a"])
# cv2.imshow("a", wp2.data)
# cv2.imshow("d", mod(wp2["d"].data))


# pylab.figure()
# for i, p2 in enumerate(path):
#     pylab.subplot(2, 2, i + 1)
#     p1p2 = p2
#     print(mod(wp2[p1p2].data).shape)
#     cv2.imshow(p1p2, mod(wp2[p1p2].data))
#     print("----------------------_")
#     pylab.imshow(mod(wp2[p1p2].data), origin='image', interpolation="nearest", cmap=pylab.cm.gray)
#     pylab.title(p1p2)



for p1 in path:
    # pylab.figure()
    for i, p2 in enumerate(path):
        # pylab.subplot(2, 2, i + 1)
        p1p2 = p1 + p2
        # pylab.imshow(mod(wp2[p1p2].data), origin='image',
        #     interpolation="nearest", cmap=pylab.cm.gray)
        cv2.imshow(p1p2, mod(wp2[p1p2].data))
        # pylab.title(p1p2)



# pylab.figure()
# i = 1
# for row in wp2.get_level(2, 'freq'):
#     for node in row:
#         pylab.subplot(len(row), len(row), i)
#         pylab.title("%s=(%s row, %s col)" % (
#         (node.path,) + wp2.expand_2d_path(node.path)))
#
#         pylab.imshow(mod(node.data), origin='image', interpolation="nearest",
#             cmap=pylab.cm.gray)
#
#         cv2.imshow("%s=(%s row, %s col)" % ((node.path,) + wp2.expand_2d_path(node.path)), mod(node.data))
#         i += 1
#
#
#
#
# pylab.show()

cv2.waitKey(0)
cv2.destroyAllWindows()