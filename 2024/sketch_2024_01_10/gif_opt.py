# import pygifsicle
# pygifsicle.optimize('out.gif', destination='out2.gif', options=[
#    # '--lossy=1000',
#     '-method=blend',
#     #'-colors=3',
#     #'-O3',
#   #  '-f',
#     ])

import imageio.v3 as iio
frames = iio.imread("out.gif", index=None)
iio.imwrite('out2.gif', frames[0::2])